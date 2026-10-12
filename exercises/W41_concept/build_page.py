"""Build ../../w41.html (Milestone 1 page) from the three markdown documents.

Run after editing any of the .md files:  python build_page.py
The markdown is embedded as-is and rendered in the browser with marked.js.
"""
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent.parent / "w41.html"

DOCS = [
    ("rebriefing", "Rebriefing", "Have we understood what is being asked?", "rebriefing.md"),
    ("survey", "User survey", "What do the people we design for actually need?", "user-survey.md"),
    ("concept", "Concept", "This is how we solve it, and this is why.", "concept.md"),
]

QUOTE_NOTE = ("> Quotes in this version are working wording and will be replaced "
              "with the final interview notes.\n\n")


def load(name):
    text = (HERE / name).read_text(encoding="utf-8")
    if name == "user-survey.md":
        text = text.replace("## Answers, as close to verbatim as possible\n",
                            "## Answers, as close to verbatim as possible\n" + QUOTE_NOTE, 1)
    return text.replace("</script", "<\\/script")


tabs = "\n".join(
    f'<button role="tab" data-tab="{key}"><b>{i}. {title}</b><span>{q}</span></button>'
    for i, (key, title, q, _) in enumerate(DOCS, 1))
sources = "\n".join(
    f'<script type="text/markdown" id="md-{key}">\n{load(f)}\n</script>' for key, _, _, f in DOCS)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Milestone 1 · Concept</title>
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
nav{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;position:sticky;top:0;background:var(--surface);padding:10px 0;z-index:1}}
nav button{{text-align:left;font:inherit;color:var(--ink);background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 12px;cursor:pointer}}
nav button span{{display:block;color:var(--ink2);font-size:13px;line-height:1.35;margin-top:2px}}
nav button[aria-selected="true"]{{border-color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent)}}
@media (max-width:600px){{nav{{grid-template-columns:1fr}}nav button span{{display:none}}}}
article{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:8px 24px 24px;margin-top:12px;overflow-wrap:anywhere}}
article h1{{font-size:26px}}article h2{{font-size:19px;margin-top:1.8em;padding-top:.6em;border-top:1px solid var(--line)}}
article blockquote{{margin:1em 0;padding:8px 14px;background:var(--soft);border-left:3px solid var(--accent);border-radius:4px;color:var(--ink2)}}
article blockquote p{{margin:.3em 0}}
.tbl{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:1em 0}}
th,td{{border-bottom:1px solid var(--line);padding:7px 8px;text-align:left;vertical-align:top}}
th{{color:var(--ink2);font-weight:600}}
code{{background:var(--soft);padding:1px 5px;border-radius:4px;font-size:.9em}}
li{{margin:.2em 0}}
footer{{color:var(--muted);font-size:13px;margin-top:24px}}
</style>
</head>
<body>
<main>
<p class="kicker"><a href="index.html">Data Storytelling</a> · Americans on AI · Milestone 1</p>
<h1>Rebriefing, user survey, concept</h1>
<p class="lede">Three documents that build on each other. Every decision in the concept traces back to a rebriefing line (R#) or a survey insight (S#); new assumptions are marked [A].</p>
<nav role="tablist">
{tabs}
</nav>
<article id="doc" aria-live="polite"></article>
<footer>Source files: <code>exercises/W41_concept/*.md</code> · rebuild with <code>python build_page.py</code></footer>
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
