# Three directions — v1 (20.10.2026)

Milestone 2 (W43, 22.10): "at least three different designs, as hand sketches".
Test from the W42 script: **would each one start with a different first sketch?**
- **A** starts with a phone screen.
- **B** starts with a floor plan seen from above.
- **C** starts with a table and chairs.
→ Three different first sketches, not three versions of one chart.

Success criteria (from `../W40_interviews/criteria.md`), used below as **C1–C3, ★**:
- **C1:** say whether "people like them" are more or less worried than average
- **C2:** find a moment that matches their own experience with AI
- **C3:** repeat the main finding in their own words
- **★ (surprise):** notice that younger people feel more able to shape AI than older people

All numbers below come from the latest NORC wave (10–14 Sep 2026, n = 1,083, ±4.1 pts). The pilot wave is excluded.
To reproduce them, run `python data_cut.py`.
Subgroup margins of error are estimated: 18–34 ±9.4, 35–49 ±8.1, 50–64 ±8.2, 65+ ±7.2 pts [A: same design effect as the full sample].

---

## A · "Real or AI?" — web flow (our concept v1)
Wireframe: `wireframes/A.svg`

- **Context → format:** web, phone in portrait first → **interactive prototype**.
- **The path:**
  1. guess real or AI
  2. reveal: about 4 in 5 see people struggling with real vs. fake
  3. answer the sentiment question yourself
  4. your dot among 1,000 US dots, then by age
  5. the turn: second question, "inevitable"
  6. one sentence to take home
- **Data cut:**
  - `ai_community_impact`, item "struggling to tell what's real from what's fake": have seen 57.1 + starting 24.4 = 81.5 %; not sure 6.9 %
  - `ai_sentiment`: excited 21.4, concerned 68.8, none 9.1, no answer 0.7 %
  - `ai_agency`: can shape 17.4, inevitable 67.5, neither 14.0, no answer 1.0 %
  - subgroups: total + 4 age bands; party/race only behind a toggle
  - latest wave only
- **Mapping rules:**
  - one respondent share → dots out of 1,000 (1 dot ≈ 1 in 1,000)
  - answer → position in the row (very excited → very concerned, then none, then no answer)
  - answer category → grey value (no red/green)
  - visitor → the one outlined dot
  - age band → regrouping of the same dots
  - 2nd question → the same dots re-sorted (not the same people)
- **Who leads:** alternating. The author leads 1, 2, 5 and 6; the visitor leads 3 and 4.
- **If someone clicks nothing:** after 8 s it autoplays 1 → 2 → 5 → 6 with total numbers only. The key message still gets through.
- **Serves:**
  - **C1** (strong: own dot + age)
  - **C2** (strong: hook)
  - **C3** (close sentence)
  - **★** (step 5, 18–34: 26.7 % vs 65+: 8.1 % "can shape"; the gap of 18.5 pts is bigger than the combined margin of ±11.8)
- **Risks:**
  - It's the most "familiar" format, close to the Pew quiz (move 4). It may feel like a test.
  - The hook image needs rights and has to be neutral. A real-vs-AI quiz can drift into "gotcha".
  - The visitor answering can be mistaken for being *in* the data. → Label: "you are not part of this survey".
- **What we'd reject:**
  - scoring the guess (right/wrong)
  - storing answers
  - a trend line over waves (no real movement, R18)
  - showing party by default (R14)

## B · "Stand where you feel" — exhibition
Wireframe: `wireframes/B.svg`

- **Context → format:** exhibition, a floor projection plus two walls → **animatic** (the documented sequence of the room's states).
- **The path:**
  1. attract loop
  2. step onto the excited ↔ concerned scale, and 1,000 dots form piles
  3. "348 of 1,000 stand here with you"
  4. the crowd splits into age lanes
  5. the floor flips to "can shape ↔ coming anyway"
  6. a room next to a country
- **Data cut:**
  - `ai_sentiment`, 6 answer codes as dots per 1,000: very excited 47, somewhat excited 167, somewhat concerned 348, very concerned 339, none 91, no answer 7
  - `ai_agency`: can shape 174, inevitable 675, neither 140, no answer 10
  - 4 age bands for the lanes. Concerned per 100: 18–34: 61 · 35–49: 66 · 50–64: 74 · 65+: 76
- **Mapping rules:**
  - answer → floor position (the scale in the original order)
  - share → pile size (dots per 1,000)
  - visitor's body → a ring of light
  - "none of these" → a separate zone **of the same size**
  - age → lane
  - 2nd question → the floor flips and the dots re-sort (no crosstab, so no dot "moves with" a person)
  - visitors' own positions → a tally on a **separate** wall, never merged into the US dots (brief §05)
- **Who leads:** the audience leads with their body, inside an authored loop that the author runs.
- **What a non-participant gets:** a passer-by who never steps on still sees the loop 1 → 2 → 4 → 5 with the US numbers.
  People in company can talk about each other's spots.
- **Serves:**
  - **C1** (strong, physical: "I stand here")
  - **★** (lanes + flip)
  - **C3** (medium: the message has to be written on the wall)
  - **C2** (weak: there's no real-vs-fake moment yet → could be added as a wall text at the entrance)
- **Risks:**
  - Standing on "very concerned" in public can feel exposing. → Several spots at once, "none of these" has equal size, nothing recorded.
  - Hardware: projector + tracking (depth camera) is hard to test by W48. A paper floor + a moderator is enough for the user test.
  - The room tally might be read as data. → "not representative" label, reset daily.
  - The format is exhibition-only, while O1 (web vs. exhibition) is still open.
- **What we'd reject:**
  - counting visitors into the US numbers
  - photos or names
  - a leaderboard of spots
  - fake "movement" of the same dots between the two questions

## C · "Dinner table" — branched animatic
Wireframe: `wireframes/C.svg`

- **Context → format:** an exhibition screen at a real table (or a web video), with one choice → **branched animatic**.
- **The path:**
  1. the table: four diners, one per age band, plus an empty chair for "you"
  2. the shared moment: everyone has seen fakes
  3. choice: sit next to 18–34 or 65+
  4. that diner's numbers (4a / 4b)
  5. the branches merge: the real gap, then the key message
- **Data cut:**
  - `ai_community_impact` real-fake "seen" per age band: 18–34: 81.9 · 35–49: 79.2 · 50–64: 84.1 · 65+: 81.0 % (no real gap, so it's the shared moment)
  - `ai_sentiment` + `ai_agency` for 18–34 (n = 203) and 65+ (n = 340):
    - concerned: 60.6 vs 76.4
    - excited: 25.3 vs 16.3
    - none: 12.3 vs 7.3
    - can shape: 26.7 vs 8.1
    - inevitable: 58.4 vs 73.6
- **Mapping rules:**
  - subgroup → one character (seat)
  - the character's line → their group's numbers, said as "x in 100"
  - the branch → a subgroup filter
  - the highlighted seat → whom you follow
  - a gap is only spoken as a difference if it's bigger than the combined margin of error. Otherwise the line is "about the same" (e.g. 18–34 vs 35–49 on "can shape": 26.7 vs 22.5, under the ±12.4 margin)
- **Who leads:** the author, with one audience choice in the middle.
- **What a non-chooser gets:** no choice for 8 s → it plays 18–34, then 65+, then the shared ending. The full message comes through.
- **Serves:**
  - **C2** (strong: the dinner table and the shared fake-video moment, interview 01 "say something smart at dinner")
  - **C3** (strong: the message is literally said at a table, so it's easy to retell)
  - **★** (the two diners turn to each other: 27 vs 8)
  - **C1** (medium: you pick a seat, but you don't place yourself)
- **Risks:**
  - Characters can become stereotypes ("the old one is scared"). → Clearly fictional, every line is a group share, not a personal opinion. No faces, no names. Party/race are never characters (R14).
  - Invented dialogue can be mistaken for real quotes. → Visible label "fictional characters, real survey numbers".
  - It's the most writing-heavy direction (script + voice/timing).
  - Only two branches stay within what the small subgroups can carry.
- **What we'd reject:**
  - a party-politics dinner (Dem vs. Rep as characters)
  - using real interview quotes as character lines
  - a "who's right?" ending

---

## Sketches we tried and did not take (add yours in class)
- *Placeholder:* trend line of "concerned" over 6 waves. Rejected: the moves are inside the margin of error (65.6 → 71.9 → 68.8 %, R18).
- *Placeholder:* map of the US. Rejected: no regional data in the CSV.
- → Add every Design Studio sketch here (one line each: what it was + why not), and photograph it (`photos/`).
