# W38 · Data Mapping — solution (dataset: 01_Coffee-Week.csv)

Made via the "LLM route" (allowed by the brief), generated with `mappings.py` → `sketches/*.svg`, overview in `index.html`.
⚠️ Your group must use **the same dataset** — if they picked another one, change `SRC` in `mappings.py` and adapt.
For the wall in class, print the SVGs or redraw them by hand (the brief values the paper route: every mark = a decision).

## The six mappings
| # | Dimension → channel | Convention broken? | Legible without legend? |
|---|---|---|---|
| 1 Timetable | time of day → x · day → y · volume → circle area · place → hue · enjoyment → opacity | no | mostly — calendar pattern is familiar; colours need the legend |
| 2 Coffee clock | time → angle (24 h) · day → ring · volume → size · type → hue | partly (clock instead of axis) | yes for "when" (the empty night is obvious), no for exact times |
| 3 Bars per day | total volume → bar length · each cup → segment (time order) · type → hue | no | yes — most familiar form, but only answers "how much" |
| 4 Cups (Dear Data) | one glyph per coffee · volume → cup height · type → hue · enjoyment → steam lines · company → dashed outline | no, invented glyph | no — needs "how to read it", but carries 5 dimensions per mark |
| 5 Broken time | time → x **reversed (right→left)** · day → y **Mon at bottom** · volume → **lightness** · enjoyment → size | **yes, 3×** | no — everyone reads left→right first and gets the days upside down |
| 6 Broken category | reason → **size** (alphabetical) | **yes — the classic mistake** | it *looks* legible, but it lies: size invents a ranking ("Waking up" > "Break") that isn't in the data |

Data types used (see exercise README): Day = temporal/ordinal · Time = temporal · Place, Type, Reason = nominal · Volume_ml = quantitative ·
Company = binary · Enjoyment_1_5 = ordinal.
Friction point avoided in #1–#4: volume and enjoyment are both "more is more", so they never share the same channel.

## Answers to the W38 questions
**Which mappings are immediately legible — clarity of mapping or familiarity of pattern?**
#3 (bars) and #1 (timetable) are read fastest, but mainly because of *familiarity* (bar chart, calendar), not because the mapping is better.
#2 works through a learned pattern from another domain (the clock). #4 is the clearest *mapping* (every channel carries meaning)
but needs its rule explained — like Boris Müller's poetry poster.

**What gets lost in the compression, and who decides?**
We decided. #3 throws away time of day, place, reason and mood to answer one question. #1 drops reason and company.
None of the graphics shows that something is missing — only #4 keeps almost everything, at the price of legibility.
The "Note" column (free text) is lost everywhere, and that's where the human story is ("best cup of the week", "tasted burnt").

**Where would interactivity help?**
Hover on a mark to read the note · filter by reason ("only coffees for tiredness") · toggle between #1 and #3 (when vs how much).

**What happened when breaking conventions (#5, #6)?**
#5: the graphic becomes a puzzle — correct data, wrong first reading. Quantity as lightness is almost impossible to compare.
#6: the most dangerous one, because it still looks clean. It shows the W38 rule: *size is a channel for quantities, not categories.*
