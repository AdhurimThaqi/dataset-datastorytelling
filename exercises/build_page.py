"""Build ../exercises.html (Exercises & process) from the weekly exercise markdown files.

Run after editing any of the source .md files:  python exercises/build_page.py
Same look as w41.html / w43.html; the markdown is embedded as-is and rendered with marked.js.
"""
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent
OUT = ROOT / "exercises.html"
GH = "https://github.com/AdhurimThaqi/dataset-datastorytelling/blob/main/"
GH_TREE = "https://github.com/AdhurimThaqi/dataset-datastorytelling/tree/main/"


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def w38():
    text = read("solutions/W38_mapping/README.md")
    text = text[text.index("## The six mappings"):]  # drop the intro lines meant for "your group"
    sketches = sorted((ROOT / "solutions/W38_mapping/sketches").glob("*.svg"))
    imgs = "\n\n".join(
        f"### {f.stem.split('_', 1)[0]} · {f.stem.split('_', 1)[1].replace('_', ' ')}\n\n"
        f"[![{f.stem}](solutions/W38_mapping/sketches/{f.name})](solutions/W38_mapping/sketches/{f.name})"
        for f in sketches)
    return ("# W38 · Data mapping (dataset: 01_Coffee-Week.csv)\n\n"
            "> **Made with AI:** these six mappings were generated with Claude (the LLM route the brief allows), "
            "not drawn by hand.\n\n" + text + "\n\n## The six images\n\n" + imgs)


def w39():
    return ("# W39 · Data exploration\n\n"
            "**[See the dataset overview: Americans on AI →](ai.html)**\n\n"
            + read("solutions/W39_data/context_method.md") + "\n\n---\n\n" + read("solutions/W39_data/findings.md"))


def w40():
    parts = [read("exercises/W40_interviews/criteria.md")] + [
        read(f"exercises/W40_interviews/interviews/interview-0{i}.md") for i in (1, 2, 3)]
    return ("# W40 · Interviews\n\n"
            "**[How the interviews fed the user survey (Milestone 1) →](w41.html#survey)**\n\n"
            + "\n\n---\n\n".join(parts))


FILES = [
    ("Survey data (all waves, all subgroups)", "exercises/W39_data/survey_all_waves_all_subgroups.csv", GH),
    ("Survey data with methodology notes", "exercises/W39_data/data.json", GH),
    ("Course notebook", "exercises/W39_data/HSLU_Data_Storytelling_Analysis.ipynb", GH),
    ("W39 analysis script", "solutions/W39_data/analysis.py", GH),
    ("W38 mapping script", "solutions/W38_mapping/mappings.py", GH),
    ("Interview guide", "exercises/W40_interviews/interview-guide.md", GH),
    ("Interviews 01–03", "exercises/W40_interviews/interviews", GH_TREE),
    ("Milestone 1 sources (W41)", "exercises/W41_concept", GH_TREE),
    ("Milestone 2 sources (W43)", "exercises/W43_prototyping", GH_TREE),
    ("Process log", "exercises/process-log.md", GH),
]


def files():
    rows = "\n".join(f"| {name} | [`{path}`]({base}{path}) |" for name, path, base in FILES)
    return ("# Files\n\nThe source files behind this page and the milestones, on GitHub.\n\n"
            "| What | File |\n|---|---|\n" + rows + "\n\n"
            "> **Course material:** the four W38 datasets (`exercises/W38_mapping/data/`) and the notebook "
            "`HSLU_Data_Storytelling_Analysis.ipynb` come from the lecturers, not from me.")


DOCS = [
    ("log", "Process log", "Week by week", lambda: read("exercises/process-log.md")),
    ("w38", "W38 · Mapping", "Six ways to draw one week", w38),
    ("w39", "W39 · Data", "Context, method, findings", w39),
    ("w40", "W40 · Interviews", "Criteria + three interviews", w40),
    ("files", "Files", "Data, code, sources", files),
]


def load(fn):
    return fn().replace("§", "section ").replace("</script", "<\\/script")


tabs = "\n".join(
    f'<button role="tab" data-tab="{key}"><b>{i}. {title}</b><span>{q}</span></button>'
    for i, (key, title, q, _) in enumerate(DOCS, 1))
sources = "\n".join(
    f'<script type="text/markdown" id="md-{key}">\n{load(fn)}\n</script>' for key, _, _, fn in DOCS)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Exercises & process</title>
<style>
:root{{--surface:#fcfcfb;--panel:#fff;--ink:#0b0b0b;--ink2:#52514e;--muted:#8a8984;--line:#e6e5e0;--accent:#2a78d6;--soft:#f3f2ee}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--surface:#1a1a19;--panel:#222221;--ink:#fff;--ink2:#c3c2b7;--muted:#8f8e86;--line:#34332f;--accent:#3987e5;--soft:#2a2a28}}}}
:root[data-theme="dark"]{{--surface:#1a1a19;--panel:#222221;--ink:#fff;--ink2:#c3c2b7;--muted:#8f8e86;--line:#34332f;--accent:#3987e5;--soft:#2a2a28}}
body{{margin:0;background:var(--surface);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}}
main{{max-width:820px;margin:auto;padding:32px 16px 80px}}
a{{color:var(--accent)}}
.kicker{{color:var(--ink2);font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin:0}}
h1{{margin:.2em 0 .3em;line-height:1.15}}
.lede{{color:var(--ink2);margin:0 0 24px}}
nav{{display:grid;grid-template-columns:repeat({len(DOCS)},1fr);gap:10px;position:sticky;top:0;background:var(--surface);padding:10px 0;z-index:1}}
nav button{{text-align:left;font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 12px;cursor:pointer}}
nav button span{{display:block;color:var(--ink2);font-size:13px;line-height:1.35;margin-top:2px}}
nav button[aria-selected="true"]{{border-color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent)}}
@media (max-width:600px){{nav{{grid-template-columns:1fr 1fr}}nav button span{{display:none}}}}
article{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 24px 24px;margin-top:12px;overflow-wrap:anywhere}}
article h1{{font-size:26px}}article h2{{font-size:19px;margin-top:1.8em;padding-top:.6em;border-top:1px solid var(--line)}}
article blockquote{{margin:1em 0;padding:8px 14px;background:var(--soft);border-left:3px solid var(--accent);border-radius:4px;color:var(--ink2)}}
article blockquote p{{margin:.3em 0}}
article img{{width:100%;height:auto;border:1px solid var(--line);border-radius:6px;background:#fff}}
article pre{{background:var(--soft);padding:12px;border-radius:8px;overflow-x:auto;font-size:13px;white-space:pre-wrap}}
.tbl{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:1em 0}}
th,td{{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}}
th{{color:var(--ink2);font-weight:600}}
code{{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:.9em}}
pre code{{background:none;padding:0}}
li{{margin:.2em 0}}
footer{{color:var(--muted);font-size:13px;margin-top:24px}}
</style>
</head>
<body>
<main>
<p class="kicker"><a href="index.html">Data Storytelling</a> · Americans on AI · Exercises</p>
<h1>Exercises & process</h1>
<p class="lede">The weekly exercises behind the milestones, and how the project developed week by week. Solo project, HSLU I.BA_DAS, autumn 2026. AI use is named where it happened.</p>
<nav role="tablist">
{tabs}
</nav>
<article id="doc" aria-live="polite"></article>
<footer>Source files: <code>exercises/</code> and <code>solutions/</code> · rebuild with <code>python exercises/build_page.py</code></footer>
</main>
{sources}
<script src="https://cdnjs.cloudflare.com/ajax/libs/marked/12.0.2/marked.min.js"></script>
<script>
const doc = document.getElementById('doc');
const buttons = [...document.querySelectorAll('nav button')];
function show(key, push) {{
  if (!document.getElementById('md-' + key)) key = buttons[0].dataset.tab;
  doc.innerHTML = marked.parse(document.getElementById('md-' + key).textContent);
  doc.querySelectorAll('table').forEach(t => {{ const w = document.createElement('div'); w.className = 'tbl'; t.replaceWith(w); w.appendChild(t); }});
  buttons.forEach(b => b.setAttribute('aria-selected', b.dataset.tab === key));
  if (push) history.replaceState(null, '', '#' + key);
}}
buttons.forEach(b => b.addEventListener('click', () => {{ show(b.dataset.tab, true); window.scrollTo({{top: 0}}); }}));
show(location.hash.slice(1), false);
</script>
</body>
</html>
"""

OUT.write_text(html, encoding="utf-8")
print(f"wrote {OUT}")
