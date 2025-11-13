import csv
from pathlib import Path


def dump_schema_counts():
    p = Path("01_schema")
    rows = []
    for f in p.glob("*.csv"):
        if not f.is_file():
            continue
        with f.open("r", encoding="utf-8") as fh:
            count = max(sum(1 for _ in fh) - 1, 0)
        rows.append((f.name, count))
    out = Path("02_data") / "schema_counts.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["file", "rows"])
        w.writerows(rows)
    print(f"Saved {out}")


if __name__ == "__main__":
    dump_schema_counts()
