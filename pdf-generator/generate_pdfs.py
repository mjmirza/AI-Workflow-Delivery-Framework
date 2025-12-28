#!/usr/bin/env python3
"""
Enterprise PDF Generator for Workflow Automation Delivery Framework
Created by: Mirza Iqbal
Contact: mirza.iqbal@next8n.com
Website: https://next8n.com

Generates professional, enterprise-grade PDF documents from markdown files.
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Optional

try:
    import markdown
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.toc import TocExtension
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    from jinja2 import Template
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


# Configuration
COMPANY_NAME = "next8n"
COMPANY_WEBSITE = "https://next8n.com"
AUTHOR_NAME = "Mirza Iqbal"
AUTHOR_EMAIL = "mirza.iqbal@next8n.com"
VERSION = "2.0"


# Enterprise CSS Styling
ENTERPRISE_CSS = """
@page {
    size: A4;
    margin: 2cm 2.5cm 2.5cm 2.5cm;

    @top-center {
        content: string(document-title);
        font-size: 9pt;
        color: #666;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    @bottom-left {
        content: "next8n.com";
        font-size: 8pt;
        color: #999;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    @bottom-center {
        content: "Confidential";
        font-size: 8pt;
        color: #999;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }

    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 8pt;
        color: #999;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
}

@page :first {
    @top-center { content: none; }
    @bottom-left { content: none; }
    @bottom-center { content: none; }
    @bottom-right { content: none; }
}

* {
    box-sizing: border-box;
}

body {
    font-family: 'Helvetica Neue', 'Segoe UI', Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #333;
    max-width: 100%;
}

/* Cover Page */
.cover-page {
    page-break-after: always;
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    margin: -2cm -2.5cm;
    padding: 2cm 2.5cm;
}

.cover-logo {
    font-size: 48pt;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 20px;
    color: #e94560;
}

.cover-title {
    font-size: 28pt;
    font-weight: 600;
    margin: 30px 0 15px 0;
    color: #fff;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.cover-subtitle {
    font-size: 14pt;
    color: #aaa;
    margin-bottom: 40px;
}

.cover-meta {
    margin-top: 60px;
    font-size: 10pt;
    color: #888;
}

.cover-meta p {
    margin: 5px 0;
}

.cover-badge {
    display: inline-block;
    background: #e94560;
    color: white;
    padding: 8px 20px;
    border-radius: 4px;
    font-size: 10pt;
    font-weight: 600;
    margin-top: 30px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Table of Contents */
.toc {
    page-break-after: always;
    padding: 40px 0;
}

.toc h2 {
    color: #1a1a2e;
    border-bottom: 3px solid #e94560;
    padding-bottom: 10px;
    margin-bottom: 30px;
}

.toc ul {
    list-style: none;
    padding: 0;
}

.toc li {
    padding: 8px 0;
    border-bottom: 1px dotted #ddd;
}

.toc a {
    color: #333;
    text-decoration: none;
}

/* Headers */
h1 {
    string-set: document-title content();
    color: #1a1a2e;
    font-size: 24pt;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 3px solid #e94560;
    page-break-after: avoid;
}

h2 {
    color: #16213e;
    font-size: 18pt;
    font-weight: 600;
    margin-top: 30px;
    margin-bottom: 15px;
    padding-bottom: 8px;
    border-bottom: 2px solid #0f3460;
    page-break-after: avoid;
}

h3 {
    color: #0f3460;
    font-size: 14pt;
    font-weight: 600;
    margin-top: 25px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h4, h5, h6 {
    color: #333;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
    page-break-after: avoid;
}

/* Paragraphs */
p {
    margin: 12px 0;
    text-align: justify;
    orphans: 3;
    widows: 3;
}

/* Links */
a {
    color: #e94560;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Lists */
ul, ol {
    margin: 15px 0;
    padding-left: 25px;
}

li {
    margin: 8px 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

thead {
    background: #1a1a2e;
    color: white;
}

th {
    padding: 12px 15px;
    text-align: left;
    font-weight: 600;
    text-transform: uppercase;
    font-size: 9pt;
    letter-spacing: 0.5px;
}

td {
    padding: 10px 15px;
    border-bottom: 1px solid #ddd;
}

tr:nth-child(even) {
    background: #f8f9fa;
}

tr:hover {
    background: #e8f4f8;
}

/* Code Blocks */
pre {
    background: #1a1a2e;
    color: #e8e8e8;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.5;
    margin: 20px 0;
    page-break-inside: avoid;
}

code {
    font-family: 'Monaco', 'Consolas', 'Courier New', monospace;
    font-size: 9pt;
}

p code, li code {
    background: #f4f4f4;
    padding: 2px 6px;
    border-radius: 3px;
    color: #e94560;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid #e94560;
    background: #f8f9fa;
    padding: 15px 20px;
    margin: 20px 0;
    font-style: italic;
    color: #555;
}

blockquote p {
    margin: 0;
}

/* Horizontal Rules */
hr {
    border: none;
    border-top: 2px solid #e94560;
    margin: 40px 0;
}

/* Checkboxes */
.checklist {
    list-style: none;
    padding-left: 0;
}

.checklist li {
    padding-left: 30px;
    position: relative;
}

.checklist li:before {
    content: "[ ]";
    position: absolute;
    left: 0;
    color: #0f3460;
    font-weight: bold;
}

/* Info Boxes */
.info-box {
    background: #e8f4f8;
    border-left: 4px solid #0f3460;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
}

.warning-box {
    background: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
}

.danger-box {
    background: #f8d7da;
    border-left: 4px solid #dc3545;
    padding: 15px 20px;
    margin: 20px 0;
    border-radius: 0 8px 8px 0;
}

/* Section Breaks */
.section-break {
    page-break-before: always;
}

/* Footer */
.document-footer {
    margin-top: 60px;
    padding-top: 20px;
    border-top: 2px solid #ddd;
    font-size: 9pt;
    color: #666;
    text-align: center;
}

/* Print Optimizations */
@media print {
    body {
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
}
"""


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
</head>
<body>
    <!-- Cover Page -->
    <div class="cover-page">
        <div class="cover-logo">next8n</div>
        <h1 class="cover-title">{{ title }}</h1>
        <p class="cover-subtitle">{{ subtitle }}</p>
        <div class="cover-badge">Enterprise Edition</div>
        <div class="cover-meta">
            <p><strong>Version:</strong> {{ version }}</p>
            <p><strong>Date:</strong> {{ date }}</p>
            <p><strong>Author:</strong> {{ author }}</p>
            <p><strong>Contact:</strong> {{ email }}</p>
        </div>
    </div>

    <!-- Table of Contents -->
    <div class="toc">
        <h2>Table of Contents</h2>
        {{ toc }}
    </div>

    <!-- Document Content -->
    <div class="content">
        {{ content }}
    </div>

    <!-- Footer -->
    <div class="document-footer">
        <p>Workflow Automation Delivery Framework | {{ company }} | {{ website }}</p>
        <p>This document is confidential and intended for authorized use only.</p>
    </div>
</body>
</html>
"""


class EnterprisePDFGenerator:
    """Generates enterprise-grade PDF documents from markdown files."""

    def __init__(self, base_path: str, output_path: str):
        self.base_path = Path(base_path)
        self.output_path = Path(output_path)
        self.output_path.mkdir(parents=True, exist_ok=True)
        self.font_config = FontConfiguration()

        # Initialize markdown converter
        self.md = markdown.Markdown(
            extensions=[
                'tables',
                'fenced_code',
                'toc',
                'nl2br',
                'sane_lists',
                'smarty',
            ],
            extension_configs={
                'toc': {
                    'title': 'Table of Contents',
                    'toc_depth': 3,
                }
            }
        )

    def clean_markdown(self, content: str) -> str:
        """Clean and preprocess markdown content."""
        # Remove badge images from content (keep only for README)
        content = re.sub(r'\[!\[.*?\]\(.*?\)\]\(.*?\)', '', content)
        content = re.sub(r'!\[.*?\]\(https://img\.shields\.io.*?\)', '', content)

        # Convert checkbox lists
        content = re.sub(r'- \[ \]', '- [ ]', content)
        content = re.sub(r'- \[x\]', '- [x]', content)

        # Clean up extra whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)

        return content.strip()

    def extract_title(self, content: str) -> tuple:
        """Extract title and subtitle from markdown content."""
        lines = content.strip().split('\n')
        title = "Document"
        subtitle = "Workflow Automation Delivery Framework"

        for line in lines[:10]:
            if line.startswith('# '):
                title = line[2:].strip()
                break
            elif line.startswith('## ') and title == "Document":
                subtitle = line[3:].strip()

        return title, subtitle

    def convert_to_html(self, markdown_content: str) -> tuple:
        """Convert markdown to HTML and extract TOC."""
        self.md.reset()
        html_content = self.md.convert(markdown_content)
        toc = getattr(self.md, 'toc', '')
        return html_content, toc

    def generate_pdf(self, markdown_file: Path, output_name: Optional[str] = None) -> Path:
        """Generate a PDF from a markdown file."""
        print(f"  Processing: {markdown_file.name}")

        # Read markdown content
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Clean and process
        content = self.clean_markdown(content)
        title, subtitle = self.extract_title(content)
        html_content, toc = self.convert_to_html(content)

        # Create HTML document
        template = Template(HTML_TEMPLATE)
        full_html = template.render(
            title=title,
            subtitle=subtitle,
            content=html_content,
            toc=toc,
            version=VERSION,
            date=datetime.now().strftime("%B %d, %Y"),
            author=AUTHOR_NAME,
            email=AUTHOR_EMAIL,
            company=COMPANY_NAME,
            website=COMPANY_WEBSITE,
        )

        # Generate PDF
        output_name = output_name or markdown_file.stem
        output_file = self.output_path / f"{output_name}.pdf"

        html_doc = HTML(string=full_html, base_url=str(self.base_path))
        css = CSS(string=ENTERPRISE_CSS, font_config=self.font_config)

        html_doc.write_pdf(
            output_file,
            stylesheets=[css],
            font_config=self.font_config,
        )

        print(f"    Generated: {output_file.name}")
        return output_file

    def generate_all(self) -> list:
        """Generate PDFs for all markdown files in the framework."""
        generated = []

        # Define document categories
        categories = {
            'checklists': 'Checklists',
            'guides': 'Guides',
            'processes': 'SOPs',
            'templates': 'Templates',
            'diagrams': 'Diagrams',
        }

        # Process README first
        readme = self.base_path / 'README.md'
        if readme.exists():
            print("\nGenerating README...")
            generated.append(self.generate_pdf(readme, '00-README-Overview'))

        # Process each category
        for folder, category in categories.items():
            folder_path = self.base_path / folder
            if folder_path.exists():
                print(f"\nGenerating {category}...")
                md_files = sorted(folder_path.glob('*.md'))
                for md_file in md_files:
                    try:
                        prefix = f"{folder.upper()}-"
                        output_name = f"{prefix}{md_file.stem}"
                        generated.append(self.generate_pdf(md_file, output_name))
                    except Exception as e:
                        print(f"    Error processing {md_file.name}: {e}")

        return generated

    def generate_combined_pdf(self, output_name: str = "Complete-Framework") -> Path:
        """Generate a single combined PDF with all documents."""
        print("\nGenerating Combined Framework Document...")

        all_content = []
        categories = {
            '.': ['README.md'],
            'diagrams': None,
            'checklists': None,
            'guides': None,
            'processes': None,
            'templates': None,
        }

        for folder, specific_files in categories.items():
            folder_path = self.base_path / folder if folder != '.' else self.base_path

            if specific_files:
                files = [folder_path / f for f in specific_files if (folder_path / f).exists()]
            else:
                files = sorted(folder_path.glob('*.md')) if folder_path.exists() else []

            for md_file in files:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                content = self.clean_markdown(content)
                all_content.append(f"\n\n---\n\n{content}")

        combined_content = "\n".join(all_content)
        html_content, toc = self.convert_to_html(combined_content)

        template = Template(HTML_TEMPLATE)
        full_html = template.render(
            title="Workflow Automation Delivery Framework",
            subtitle="Complete Documentation Package",
            content=html_content,
            toc=toc,
            version=VERSION,
            date=datetime.now().strftime("%B %d, %Y"),
            author=AUTHOR_NAME,
            email=AUTHOR_EMAIL,
            company=COMPANY_NAME,
            website=COMPANY_WEBSITE,
        )

        output_file = self.output_path / f"{output_name}.pdf"

        html_doc = HTML(string=full_html, base_url=str(self.base_path))
        css = CSS(string=ENTERPRISE_CSS, font_config=self.font_config)

        html_doc.write_pdf(
            output_file,
            stylesheets=[css],
            font_config=self.font_config,
        )

        print(f"  Generated: {output_file.name}")
        return output_file


def main():
    """Main entry point."""
    print("=" * 60)
    print("Enterprise PDF Generator")
    print("Workflow Automation Delivery Framework")
    print(f"Version {VERSION} | {COMPANY_NAME}")
    print("=" * 60)

    # Determine paths
    script_dir = Path(__file__).parent
    base_path = script_dir.parent
    output_path = base_path / 'generated-pdfs'

    print(f"\nBase Path: {base_path}")
    print(f"Output Path: {output_path}")

    # Initialize generator
    generator = EnterprisePDFGenerator(base_path, output_path)

    # Generate individual PDFs
    print("\n" + "=" * 60)
    print("Generating Individual Documents...")
    print("=" * 60)

    generated_files = generator.generate_all()

    # Generate combined PDF
    print("\n" + "=" * 60)
    print("Generating Combined Document...")
    print("=" * 60)

    combined = generator.generate_combined_pdf()
    generated_files.append(combined)

    # Summary
    print("\n" + "=" * 60)
    print("Generation Complete!")
    print("=" * 60)
    print(f"\nTotal PDFs Generated: {len(generated_files)}")
    print(f"Output Directory: {output_path}")
    print("\nGenerated Files:")
    for f in generated_files:
        size_kb = f.stat().st_size / 1024
        print(f"  - {f.name} ({size_kb:.1f} KB)")

    print("\n" + "=" * 60)
    print(f"Created by {AUTHOR_NAME} | {AUTHOR_EMAIL}")
    print(f"Website: {COMPANY_WEBSITE}")
    print("=" * 60)


if __name__ == "__main__":
    main()
