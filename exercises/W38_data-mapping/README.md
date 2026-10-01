# W38 · Data Mapping mini-project (homework → reviewed in W40)

Source: script W38 §05 + "Datasets — Data Mapping mini-project" (visualcontext.net).

## Task
In how many ways can the same dataset be mapped?
1. Your group picks **one** of the four datasets in `data/` (everyone in the group uses the same one).
2. Sketch **4–6 different mappings** of it — on paper or with an LLM. Quantity before quality.
   Any data dimension may go on any visual property: position, size, colour, shape, angle, texture, repetition …
3. **At least one** mapping deliberately **breaks a convention** (time right→left, quantity as lightness, inverted y-axis …). What happens to legibility?
4. Photograph them → `sketches/` + process documentation. Bring the sheets to W40 (they go on the wall and are read **without explanation**).

## The datasets (personal weekly data, "Dear Data" style)
| File | Rows | Dimensions | Friction point |
|---|---|---|---|
| `01_Coffee-Week.csv` | 23 | Day, Time, Place, Type, Volume_ml, Reason, Company (binary), Enjoyment_1_5, Note | Volume and enjoyment are both "more is more" — don't put both on size |
| `02_Journeys.csv` | 22 | Day, Start_time, Destination, Mode, Duration_min, Distance_km, Weather, Mood_1_5, Detours, Note | Duration & distance correlate, but not always — combining them hides the outliers (the 38-min walk home) |
| `03_Messages.csv` | 26 | Day, Time, Channel, Sender_group, Type, Emojis, Characters, Replied (binary), Reply_time_min | |
| `04_Waste.csv` | 22 | Day, Item, Material, Weight_g, Place, Disposal, Avoidable (binary), Note | |

## Data type → suitable channel
| Type | What it can do | Suitable channels |
|---|---|---|
| Nominal (category, no order) | distinguish | hue, shape, texture, position in groups |
| Ordinal (rank) | order | lightness, saturation, stepped size, stroke weight |
| Quantitative (number with zero) | compare, calculate | length, position, area, angle |
| Temporal | order, show intervals | position on an axis, spirals, clock forms |
| Binary (yes/no) | mark | outline, dot, filled/empty |

**Most common mistake:** a category without order on a channel that asserts order (e.g. transport mode as size).

## If you use an LLM
Give it the CSV, name the columns + data types, ask for **eight clearly different mappings**
("dimension → channel" + SVG sketch) and **explicitly ask for broken conventions** (LLMs default to bar/line/pie).
Then check each one:
- Which dimension sits on which channel — does the type fit (no category on size)?
- Does the picture claim something that is not in the data?
- Is it legible without a legend — and if not, is that defensible?

## Questions to answer for W40
- Which mappings are legible immediately — because the mapping is clear, or because the pattern is familiar?
- What gets lost in your compression? Who decided — and does the graphic make that loss visible?
- Where would you have wanted interactivity to see more?

## My mappings
| # | Dimension → channel | Convention broken? | Legible without legend? |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
