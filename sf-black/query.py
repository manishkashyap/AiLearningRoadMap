import argparse
import json
import pathlib

import tabulate


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
EMPTY_VALUE = "___EMPTY"


def pct(x):
    return f"{x * 100.:.2f}%"


def load_duckdb_outputs(db_path: pathlib.Path):
    if not db_path.exists():
        return None

    try:
        import duckdb
    except ModuleNotFoundError:
        return None

    db = duckdb.connect(str(db_path))

    summary_row = db.execute("SELECT * FROM summary").fetchone()
    summary_columns = [description[0] for description in db.description]
    summary = dict(zip(summary_columns, summary_row))

    segment_rows = db.execute(
        "SELECT * FROM segments WHERE score > 0 ORDER BY ABS(impact) DESC"
    ).fetchall()
    segment_columns = [description[0] for description in db.description]
    segments = [dict(zip(segment_columns, row)) for row in segment_rows]

    db.close()
    return summary, segments


def load_json_outputs(summary_path: pathlib.Path, segments_path: pathlib.Path):
    if not summary_path.exists() or not segments_path.exists():
        return None

    with summary_path.open("r", encoding="utf-8") as summary_file:
        summary = json.load(summary_file)

    segments = []
    with segments_path.open("r", encoding="utf-8") as segments_file:
        for line in segments_file:
            segments.append(json.loads(line))

    segments.sort(key=lambda segment: abs(segment["impact"]), reverse=True)
    return summary, segments


def print_report(summary: dict, insights: list[dict], limit: int | None) -> None:
    if limit is not None:
        insights = insights[:limit]

    summary_metric = summary["summary_metric"]
    summary_count = summary["summary_count"]

    print("Summary Metric: ", pct(summary_metric))
    print("Summary Segment Count: ", summary_count)

    data = [
        ["segment", "metric", "segment_size", "metric_change"]
    ]

    for item in insights:
        feature = {}
        for column in FEATURE_COLUMNS:
            column_value = item[column]
            if column_value == EMPTY_VALUE:
                continue

            feature[column] = column_value

        feature_string = "\n".join([f'{k}: "{v}"' for k, v in feature.items()])

        segment_metric = item["order_repeat_rate"]
        segment_metric_delta = segment_metric - summary_metric
        segment_metric_change = pct((segment_metric - summary_metric) / summary_metric)
        if segment_metric_delta > 0:
            segment_metric_change = f"+{segment_metric_change}"

        segment_count = item["count"]
        segment_size = pct(segment_count / summary_count)

        data.append(
            [feature_string, pct(segment_metric), segment_size, segment_metric_change]
        )
        data.append([tabulate.SEPARATING_LINE])

    print(tabulate.tabulate(data, headers="firstrow", tablefmt="psql"))


if __name__ == "__main__":
    script_dir = pathlib.Path(__file__).resolve().parent

    parser = argparse.ArgumentParser(
        description="Print Significant Factors repeat-rate segments."
    )
    parser.add_argument(
        "--db-path",
        type=pathlib.Path,
        default=script_dir / "data_drill_down.duckdb",
        help="Path to the DuckDB file created by repeat_rate_create_local.py.",
    )
    parser.add_argument(
        "--summary-path",
        type=pathlib.Path,
        default=script_dir / "summary.json",
        help="Path to local fallback summary JSON.",
    )
    parser.add_argument(
        "--segments-path",
        type=pathlib.Path,
        default=script_dir / "segments.jsonl",
        help="Path to local fallback segments JSONL.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=50,
        help="Maximum number of segments to print. Use 0 to print all.",
    )
    args = parser.parse_args()

    outputs = load_duckdb_outputs(args.db_path)
    if outputs is None:
        outputs = load_json_outputs(args.summary_path, args.segments_path)

    if outputs is None:
        raise FileNotFoundError(
            "Expected either a DuckDB analysis database or local JSON outputs. "
            "Run python3 sf-black/repeat_rate_create_local.py first."
        )

    limit = None if args.limit == 0 else args.limit
    print_report(*outputs, limit=limit)
