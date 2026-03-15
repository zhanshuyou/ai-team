#!/usr/bin/env python3
"""
Report Generator — Reads CSV/Excel data and generates summary reports.

Usage:
    python report-generator.py <input_file> [--output <output_file>] [--format md|csv]

Example:
    python report-generator.py sales_data.csv --output report.md --format md
"""

import argparse
import sys
from pathlib import Path

def read_data(file_path: str) -> list[dict]:
    """Read data from CSV or Excel file."""
    path = Path(file_path)

    if path.suffix == '.csv':
        import csv
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    elif path.suffix in ('.xlsx', '.xls'):
        try:
            import openpyxl
            wb = openpyxl.load_workbook(path, read_only=True)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                return []
            headers = [str(h) for h in rows[0]]
            return [dict(zip(headers, row)) for row in rows[1:]]
        except ImportError:
            print("Error: openpyxl is required for Excel files. Install with: pip install openpyxl")
            sys.exit(1)
    else:
        print(f"Error: Unsupported file format '{path.suffix}'. Use .csv or .xlsx")
        sys.exit(1)


def generate_summary(data: list[dict]) -> dict:
    """Generate basic summary statistics."""
    if not data:
        return {"row_count": 0, "columns": []}

    columns = list(data[0].keys())
    summary = {
        "row_count": len(data),
        "columns": columns,
        "column_count": len(columns),
    }

    # Attempt numeric summaries
    numeric_summaries = {}
    for col in columns:
        values = []
        for row in data:
            try:
                values.append(float(row[col]))
            except (ValueError, TypeError):
                continue
        if values:
            numeric_summaries[col] = {
                "min": min(values),
                "max": max(values),
                "mean": sum(values) / len(values),
                "count": len(values),
            }
    summary["numeric_columns"] = numeric_summaries
    return summary


def format_markdown(summary: dict) -> str:
    """Format summary as Markdown report."""
    lines = ["# Data Summary Report", ""]
    lines.append(f"- **Total rows**: {summary['row_count']}")
    lines.append(f"- **Total columns**: {summary['column_count']}")
    lines.append(f"- **Columns**: {', '.join(summary['columns'])}")
    lines.append("")

    if summary.get("numeric_columns"):
        lines.append("## Numeric Column Statistics")
        lines.append("")
        lines.append("| Column | Min | Max | Mean | Count |")
        lines.append("|--------|-----|-----|------|-------|")
        for col, stats in summary["numeric_columns"].items():
            lines.append(
                f"| {col} | {stats['min']:.2f} | {stats['max']:.2f} | "
                f"{stats['mean']:.2f} | {stats['count']} |"
            )
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate summary reports from data files")
    parser.add_argument("input", help="Input file path (CSV or Excel)")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")
    parser.add_argument("--format", "-f", choices=["md", "csv"], default="md", help="Output format")
    args = parser.parse_args()

    data = read_data(args.input)
    summary = generate_summary(data)
    report = format_markdown(summary)

    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()
