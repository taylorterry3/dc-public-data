#!/usr/bin/env python

import markdown
from pathlib import Path
from tqdm import tqdm

# CSS for styling the HTML output
CSS = """
<style>
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        line-height: 1.6;
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
        background-color: #f5f5f5;
    }
    .container {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    h1 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.5rem;
    }
    h2 {
        color: #34495e;
        margin-top: 2rem;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    th, td {
        padding: 0.75rem;
        text-align: left;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f8f9fa;
        font-weight: 600;
    }
    tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    img {
        max-width: 100%;
        height: auto;
        margin: 1rem 0;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
"""


def get_html_template(content):
    """Return the complete HTML document with the given content."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ward Arrest Analysis Report</title>
    {CSS}
</head>
<body>
<div class="container">
{content}
</div>
</body>
</html>"""


def convert_md_to_html(md_file: Path) -> None:
    """Convert a markdown file to HTML with styling."""
    # Read markdown content
    md_content = md_file.read_text()

    # Convert to HTML
    html_content = markdown.markdown(md_content, extensions=["tables", "fenced_code"])

    # Create complete HTML document
    html_output = get_html_template(html_content)

    # Write HTML file
    html_file = md_file.parent / f"{md_file.stem}.html"
    html_file.write_text(html_output)


def main():
    # Get all markdown files in the wards directory
    reports_dir = Path("../reports/wards")
    md_files = list(reports_dir.glob("*.md"))

    print(f"Converting {len(md_files)} reports to HTML...")

    # Convert each file
    for md_file in tqdm(md_files, desc="Converting reports"):
        convert_md_to_html(md_file)

    print("HTML reports have been generated in the reports/wards directory.")


if __name__ == "__main__":
    main()
