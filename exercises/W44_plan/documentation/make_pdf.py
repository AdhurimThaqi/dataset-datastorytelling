"""Build the W44 submission PDFs from the Markdown files in this folder.

Run:  python make_pdf.py
Needs: pip install markdown · Microsoft Edge or Google Chrome (prints the HTML to PDF, headless).
Writes 01_implementation-plan.pdf, 02_sprint-plan.pdf and 03_research-appendix.pdf next to this script.
"""
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import markdown

HERE = Path(__file__).parent
EX = HERE.parent.parent  # exercises/
PROTO = EX / "W43_prototyping" / "prototype"

CSS = """
@page{size:A4;margin:16mm 16mm 18mm}
*{box-sizing:border-box}
body{font:10.5pt/1.45 "Segoe UI",system-ui,sans-serif;color:#0b0b0b;margin:0}
h1{font-size:22pt;line-height:1.1;margin:0 0 4pt;letter-spacing:-.01em}
h1+p{color:#52514e;font-size:9.5pt;margin:0 0 14pt;padding-bottom:10pt;border-bottom:2px solid #0b0b0b}
h2{font-size:13.5pt;margin:16pt 0 6pt;padding-top:6pt;border-top:1px solid #e6e5e0;break-after:avoid}
h3{font-size:11pt;margin:12pt 0 4pt;break-after:avoid}
p{margin:4pt 0}
table{border-collapse:collapse;width:100%;margin:6pt 0 10pt;font-size:9.5pt;break-inside:auto}
th,td{border-bottom:1px solid #e6e5e0;padding:5pt 6pt;text-align:left;vertical-align:top}
th{background:#f3f2ee;font-weight:700}
tr{break-inside:avoid}
img{display:block;max-width:100%;margin:6pt auto 10pt;break-inside:avoid}
img[src$=".jpg"]{max-height:64mm;border-radius:6pt}
code{font:9pt Consolas,monospace;background:#f3f2ee;padding:0 3pt;border-radius:3pt}
pre{font:7.6pt/1.4 Consolas,monospace;background:#f3f2ee;padding:8pt 10pt;border-radius:6pt;white-space:pre-wrap;break-inside:auto}
pre code{background:none;padding:0}
blockquote{margin:6pt 0;padding:4pt 10pt;border-left:3px solid #d9531e;color:#52514e}
ul,ol{margin:4pt 0;padding-left:16pt}
a{color:inherit}
.part{break-before:page}
.part:first-of-type{break-before:auto}
"""


def page(title, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
            f"<style>{CSS}</style></head><body>{body}</body></html>")


def normalize(text):
    """GitHub-style Markdown → what Python-Markdown expects: 4-space sub-lists, a blank line before lists/tables."""
    out, fence = [], False
    for line in text.split("\n"):
        if line.startswith("```"):
            fence = not fence
        if not fence:
            line = re.sub(r"^ {1,3}(?=(- |\d+\. ))", "    ", line)          # sub-list indent → 4 spaces
            prev = out[-1] if out else ""
            if re.match(r"^(\||- |\d+\. )", line) and prev.strip() and not re.match(r"^(\||\s*- |\s*\d+\. )", prev):
                out.append("")
        out.append(line)
    return "\n".join(out)


def md(text):
    return markdown.markdown(normalize(text), extensions=["tables", "fenced_code"])


def browser():
    for p in [r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Google\Chrome\Application\chrome.exe",
              shutil.which("msedge"), shutil.which("chrome"), shutil.which("google-chrome")]:
        if p and Path(p).exists():
            return p
    raise SystemExit("No Edge or Chrome found to print the PDF.")


def to_pdf(html_file, pdf_file, tries=3):
    # own throw-away profile, so it doesn't clash with a browser window that's already open;
    # headless Edge sometimes hangs after printing, so a hung run is killed and retried
    for attempt in range(1, tries + 1):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as profile:
            pdf_file.unlink(missing_ok=True)
            try:
                subprocess.run([browser(), "--headless=new", "--disable-gpu", "--no-first-run", "--no-pdf-header-footer",
                                f"--user-data-dir={profile}", f"--print-to-pdf={pdf_file}", html_file.resolve().as_uri()],
                               check=True, capture_output=True, timeout=60)
            except subprocess.TimeoutExpired:
                if not (pdf_file.exists() and pdf_file.stat().st_size):
                    print(f"  {pdf_file.name}: browser hung (try {attempt}/{tries})")
                    continue
        print("wrote", pdf_file.name)
        return
    raise SystemExit(f"Could not print {pdf_file.name}")


def build(name, title, body):
    html = HERE / f"{name}.html"
    html.write_text(page(title, body), encoding="utf-8")
    to_pdf(html, HERE / f"{name}.pdf")
    html.unlink()  # the PDF is the hand-in; the Markdown is the source


def appendix():
    parts = [
        ("Concept refinement: what the W43 test showed", EX / "W44_plan" / "concept-refinement.md"),
        ("User test of the prototype (v1 → v4)", PROTO / "test.md"),
        ("All prompts for the prototype", PROTO / "prompts.md"),
    ]
    head = ("# Research appendix\n\n**Worried, but it's coming anyway** · Adhurim Thaqi · W44 · 29.10.2026 · "
            "The prototype itself: https://adhurimthaqi.github.io/dataset-datastorytelling/"
            "exercises/W43_prototyping/prototype/v4.html (source: `exercises/W43_prototyping/prototype/v4.html`)\n")
    body = md(head)
    for label, f in parts:
        text = re.sub(r"^# .*\n", "", f.read_text(encoding="utf-8"), count=1)   # drop the file's own title
        text = re.sub(r"^## ", "### ", text, flags=re.M)                      # one level down under the part title
        body += f'<section class="part">{md(f"## {label}" + chr(10) + chr(10) + text)}</section>'
    return body


if __name__ == "__main__":
    build("01_implementation-plan", "Implementation plan", md((HERE / "01_implementation-plan.md").read_text(encoding="utf-8")))
    build("02_sprint-plan", "Sprint plan", md((HERE / "02_sprint-plan.md").read_text(encoding="utf-8")))
    build("03_research-appendix", "Research appendix", appendix())
