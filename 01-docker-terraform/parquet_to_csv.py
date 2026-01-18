import sys
from pathlib import Path
import pyarrow.parquet as pq
import pyarrow.csv as pv


def parquet_to_csv(input_file: str) -> None:
    input_path = Path(input_file)

    if not input_path.is_file():
        print(f"Error: '{input_file}' does not exist or is not a file.")
        return

    output_file = input_path.with_suffix(".csv")

    table = pq.read_table(input_file)
    pv.write_csv(table, str(output_file))

    print(f"Converted '{input_file}' → '{output_file}'")


def main():
    if len(sys.argv) != 2:
        print("Usage: python parquet_to_csv.py <input_file.parquet>")
        sys.exit(1)

    input_file = sys.argv[1]
    parquet_to_csv(input_file)


if __name__ == "__main__":
    main()
