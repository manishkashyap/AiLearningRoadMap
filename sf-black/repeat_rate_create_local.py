import argparse
import itertools
import json
import math
from pathlib import Path

from convert import INPUT_FILE, OUTPUT_FILE, csv_to_jsonl


SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_DB_PATH = SCRIPT_DIR / "data_drill_down.duckdb"
SUMMARY_JSON = SCRIPT_DIR / "summary.json"
SEGMENTS_JSONL = SCRIPT_DIR / "segments.jsonl"

FEATURE_COLUMNS = [
    "First_order_best_category",
    "First_order_best_sub_catgeory",
    "FirstOrderCity",
    "FirstOrderCityTier",
    "First_order_OrderPlatform",
    "First_order_campaign_medium",
    "First_order_campaign_source",
    "First_order_campaign_term",
    "First_order_referrer_type",
    "OrderTiming",
    "DiscountUsageSegment",
    "WeekdayWeekendPreference",
]
NUMERATOR_COLUMN = "repeated_users_segment"
DENOMINATOR_COLUMN = "total_users_segment"
EMPTY_VALUE = "___EMPTY"
MIN_SUPPORT = 0.02
MAX_SEGMENTS = 1000
MAX_LOCAL_ORDER = 5
MUTUALLY_EXCLUSIVE_GROUPS = [
    {"First_order_best_category", "First_order_best_sub_catgeory"},
    {"FirstOrderCity", "FirstOrderCityTier"},
]


def ensure_jsonl(force: bool = False) -> None:
    if OUTPUT_FILE.exists() and not force:
        return

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Expected source CSV at {INPUT_FILE}. "
            "Place ss_transposed_capped_sample.csv beside this script."
        )

    csv_to_jsonl(INPUT_FILE, OUTPUT_FILE)


def run_significant_factors_engine() -> bool:
    try:
        from cli.black.util import import_to_db
        from repeat_rate_create import run_analysis
    except ModuleNotFoundError as exc:
        print(
            "Significant Factors runtime unavailable "
            f"({exc.name}); using local compatible analysis."
        )
        return False

    import_to_db(SCRIPT_DIR)
    run_analysis(SCRIPT_DIR)
    print(f"Wrote Significant Factors database to {DEFAULT_DB_PATH}")
    return True


def load_rows() -> list[dict]:
    ensure_jsonl()

    rows = []
    with OUTPUT_FILE.open("r", encoding="utf-8") as jsonl_file:
        for line in jsonl_file:
            row = json.loads(line)
            row[NUMERATOR_COLUMN] = int(row[NUMERATOR_COLUMN])
            row[DENOMINATOR_COLUMN] = int(row[DENOMINATOR_COLUMN])
            rows.append(row)

    return rows


def valid_feature_combo(combo: tuple[str, ...]) -> bool:
    combo_set = set(combo)
    return not any(group <= combo_set for group in MUTUALLY_EXCLUSIVE_GROUPS)


def iter_feature_combos(max_order: int):
    for order in range(1, max_order + 1):
        for combo in itertools.combinations(FEATURE_COLUMNS, order):
            if valid_feature_combo(combo):
                yield combo


def z_value(summary_numerator: int, summary_denominator: int, numerator: int, denominator: int) -> float:
    rest_denominator = summary_denominator - denominator
    if denominator == 0 or rest_denominator <= 0:
        return 0.0

    rest_numerator = summary_numerator - numerator
    segment_rate = numerator / denominator
    rest_rate = rest_numerator / rest_denominator
    pooled_rate = summary_numerator / summary_denominator
    variance = pooled_rate * (1 - pooled_rate) * (1 / denominator + 1 / rest_denominator)

    if variance <= 0:
        return 0.0

    return (segment_rate - rest_rate) / math.sqrt(variance)


def build_local_outputs(max_order: int, min_support: float, max_segments: int):
    rows = load_rows()
    summary_numerator = sum(row[NUMERATOR_COLUMN] for row in rows)
    summary_denominator = sum(row[DENOMINATOR_COLUMN] for row in rows)
    summary_metric = summary_numerator / summary_denominator
    min_count = summary_denominator * min_support

    summary = {
        "summary_numerator": summary_numerator,
        "summary_denominator": summary_denominator,
        "summary_count": summary_denominator,
        "summary_metric": summary_metric,
    }

    candidates = []
    for combo in iter_feature_combos(max_order):
        grouped = {}
        for row in rows:
            key = tuple(row[column] for column in combo)
            numerator, denominator = grouped.get(key, (0, 0))
            grouped[key] = (
                numerator + row[NUMERATOR_COLUMN],
                denominator + row[DENOMINATOR_COLUMN],
            )

        for key, (numerator, denominator) in grouped.items():
            if denominator < min_count:
                continue

            metric = numerator / denominator
            metric_delta = metric - summary_metric
            if metric_delta == 0:
                continue

            support = denominator / summary_denominator
            impact = metric_delta * support
            z = z_value(summary_numerator, summary_denominator, numerator, denominator)
            score = abs(impact) * max(abs(z), 1.0)

            segment = {column: EMPTY_VALUE for column in FEATURE_COLUMNS}
            for column, value in zip(combo, key):
                segment[column] = value

            segment.update(
                {
                    "repeat_customers": numerator,
                    "total_customers": denominator,
                    "order_repeat_rate": metric,
                    "count": denominator,
                    "risk_ratio": metric / summary_metric if summary_metric else None,
                    "impact": impact,
                    "z": z,
                    "score": score,
                }
            )
            candidates.append(segment)

    best_by_population = {}
    for segment in candidates:
        key = (
            segment["repeat_customers"],
            segment["total_customers"],
            round(segment["order_repeat_rate"], 12),
        )
        existing = best_by_population.get(key)
        if existing is None or segment_order(segment) < segment_order(existing):
            best_by_population[key] = segment

    candidates = remove_redundant_segments(list(best_by_population.values()))
    candidates.sort(key=lambda segment: segment["score"], reverse=True)
    return summary, candidates[:max_segments]


def segment_order(segment: dict) -> int:
    return sum(1 for column in FEATURE_COLUMNS if segment[column] != EMPTY_VALUE)


def segment_features(segment: dict) -> dict:
    return {
        column: segment[column]
        for column in FEATURE_COLUMNS
        if segment[column] != EMPTY_VALUE
    }


def is_subset_segment(base: dict, candidate: dict) -> bool:
    base_features = segment_features(base)
    candidate_features = segment_features(candidate)
    return all(candidate_features.get(column) == value for column, value in base_features.items())


def is_materially_same_population(base: dict, candidate: dict) -> bool:
    base_count = base["count"]
    candidate_count = candidate["count"]
    count_delta = abs(candidate_count - base_count) / max(base_count, candidate_count)
    metric_delta = abs(candidate["order_repeat_rate"] - base["order_repeat_rate"])
    return count_delta <= 0.03 and metric_delta <= 0.005


def remove_redundant_segments(candidates: list[dict]) -> list[dict]:
    ordered = sorted(candidates, key=lambda segment: (segment_order(segment), -segment["score"]))
    selected = []

    for candidate in ordered:
        if any(
            is_subset_segment(existing, candidate)
            and is_materially_same_population(existing, candidate)
            for existing in selected
        ):
            continue
        selected.append(candidate)

    return selected


def write_json_outputs(summary: dict, segments: list[dict]) -> None:
    with SUMMARY_JSON.open("w", encoding="utf-8") as summary_file:
        json.dump(summary, summary_file, ensure_ascii=False, indent=2)
        summary_file.write("\n")

    with SEGMENTS_JSONL.open("w", encoding="utf-8") as segments_file:
        for segment in segments:
            segments_file.write(json.dumps(segment, ensure_ascii=False) + "\n")


def write_duckdb_outputs(summary: dict, segments: list[dict]) -> bool:
    try:
        import duckdb
    except ModuleNotFoundError:
        return False

    db = duckdb.connect(str(DEFAULT_DB_PATH))
    db.execute("DROP TABLE IF EXISTS summary")
    db.execute("DROP TABLE IF EXISTS segments")
    db.execute(
        """
        CREATE TABLE summary (
            summary_numerator BIGINT,
            summary_denominator BIGINT,
            summary_count BIGINT,
            summary_metric DOUBLE
        )
        """
    )
    db.execute(
        "INSERT INTO summary VALUES (?, ?, ?, ?)",
        [
            summary["summary_numerator"],
            summary["summary_denominator"],
            summary["summary_count"],
            summary["summary_metric"],
        ],
    )

    feature_columns_sql = ", ".join(f'"{column}" VARCHAR' for column in FEATURE_COLUMNS)
    db.execute(
        f"""
        CREATE TABLE segments (
            {feature_columns_sql},
            repeat_customers BIGINT,
            total_customers BIGINT,
            order_repeat_rate DOUBLE,
            count BIGINT,
            risk_ratio DOUBLE,
            impact DOUBLE,
            z DOUBLE,
            score DOUBLE
        )
        """
    )

    insert_columns = FEATURE_COLUMNS + [
        "repeat_customers",
        "total_customers",
        "order_repeat_rate",
        "count",
        "risk_ratio",
        "impact",
        "z",
        "score",
    ]
    placeholders = ", ".join("?" for _ in insert_columns)
    db.executemany(
        f"INSERT INTO segments VALUES ({placeholders})",
        [[segment[column] for column in insert_columns] for segment in segments],
    )
    db.close()
    return True


def run_local_analysis(max_order: int, min_support: float, max_segments: int) -> None:
    summary, segments = build_local_outputs(max_order, min_support, max_segments)
    write_json_outputs(summary, segments)
    wrote_duckdb = write_duckdb_outputs(summary, segments)

    print(f"Wrote local summary to {SUMMARY_JSON}")
    print(f"Wrote local segments to {SEGMENTS_JSONL}")
    if wrote_duckdb:
        print(f"Wrote local DuckDB database to {DEFAULT_DB_PATH}")
    else:
        print("duckdb is not installed; query.py will read the JSON outputs instead.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run SignificantFactorsEngine, falling back to local analysis when unavailable."
    )
    parser.add_argument(
        "--force-convert",
        action="store_true",
        help="Regenerate data.jsonl from ss_transposed_capped_sample.csv before importing.",
    )
    parser.add_argument(
        "--engine",
        choices=["auto", "significant-factors", "local"],
        default="auto",
        help="Choose the real Significant Factors runtime or the local compatible analysis.",
    )
    parser.add_argument(
        "--max-order",
        type=int,
        default=MAX_LOCAL_ORDER,
        help="Maximum number of dimensions in a local fallback segment.",
    )
    parser.add_argument(
        "--min-support",
        type=float,
        default=MIN_SUPPORT,
        help="Minimum local fallback segment support as a fraction of total users.",
    )
    parser.add_argument(
        "--max-segments",
        type=int,
        default=MAX_SEGMENTS,
        help="Maximum local fallback segments to write.",
    )
    args = parser.parse_args()

    ensure_jsonl(force=args.force_convert)

    if args.engine in {"auto", "significant-factors"}:
        ran_engine = run_significant_factors_engine()
        if ran_engine:
            return
        if args.engine == "significant-factors":
            raise ModuleNotFoundError(
                "Could not import the Significant Factors runtime dependencies. "
                "Install or expose cli.black, magickpi, src.magickpi, and duckdb."
            )

    run_local_analysis(args.max_order, args.min_support, args.max_segments)


if __name__ == "__main__":
    main()
