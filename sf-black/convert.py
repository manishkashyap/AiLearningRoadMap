import csv
import json
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_FILE = SCRIPT_DIR / "ss_transposed_capped_sample.csv"
OUTPUT_FILE = SCRIPT_DIR / "data.jsonl"


def convert_value(value: str):
    """Convert numeric-looking values while keeping percentages as strings."""
    if value is None:
        return None

    value = value.strip()

    if value == "":
        return "___UNKNOWN"

    if 'unavailable' in value.lower() or 'not available' in value.lower():
        return "___UNKNOWN"

    if value.endswith("%"):
        return value

    try:
        return int(value)
    except ValueError:
        pass

    try:
        return float(value)
    except ValueError:
        return value


def csv_to_jsonl(input_file: Path, output_file: Path) -> None:
    with input_file.open("r", encoding="utf-8-sig", newline="") as csv_file, \
            output_file.open("w", encoding="utf-8") as jsonl_file:

        reader = csv.DictReader(csv_file)

        for row in reader:
            cleaned_row = {
                key: convert_value(value)
                for key, value in row.items()
            }

            jsonl_file.write(
                json.dumps(cleaned_row, ensure_ascii=False) + "\n"
            )


if __name__ == "__main__":
    csv_to_jsonl(INPUT_FILE, OUTPUT_FILE)
    print(f"Converted {INPUT_FILE} to {OUTPUT_FILE}")
