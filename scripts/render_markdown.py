import markdown2
import os
from pathlib import Path

# Add custom CSS for better table formatting
css = """
<style>
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 10px 0;
        font-size: 0.9em;
    }
    th, td {
        padding: 4px 8px;
        text-align: left;
        border: 1px solid #ddd;
    }
    th {
        background-color: #f5f5f5;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    tr:hover {
        background-color: #f5f5f5;
    }
    td:last-child {
        text-align: right;
        font-family: monospace;
    }
    img {
        max-width: 100%;
        height: auto;
        display: block;
        margin: 20px auto;
    }
    h1 {
        color: #333;
        border-bottom: 2px solid #eee;
        padding-bottom: 10px;
    }
    h2 {
        color: #444;
        margin-top: 30px;
    }
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        line-height: 1.4;
        color: #333;
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }
</style>
"""


def render_markdown(markdown_file, output_file):
    # Read markdown content
    with open(markdown_file, "r") as f:
        markdown_content = f.read()

    # Convert markdown to HTML
    html_content = markdown2.markdown(
        markdown_content, extras=["tables", "fenced-code-blocks", "header-ids"]
    )

    # Wrap HTML content with CSS
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>{Path(markdown_file).stem}</title>
        {css}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Write HTML to file
    with open(output_file, "w") as f:
        f.write(full_html)


def main():
    # Get the reports directory
    reports_dir = Path("reports/wards")

    # Process each markdown file
    for markdown_file in reports_dir.glob("ward_*_report.md"):
        output_file = markdown_file.with_suffix(".html")
        print(f"Converting {markdown_file} to {output_file}")
        render_markdown(markdown_file, output_file)


if __name__ == "__main__":
    main()
