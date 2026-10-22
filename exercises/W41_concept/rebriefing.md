# Rebriefing — v1 (12.10.2026)

## Task
- **R1 · In our words:** "Americans on AI" turns US public opinion on AI into percentages every two weeks. We design *one* way into that data
  that lets a non-expert feel where public opinion stands, and where they stand themselves.
- **R2 · Format:** animatic, branched animatic, or interactive prototype, plus a short justification of our decisions. Web or exhibition.
- **R3 · Frame:** solo project (Adhurim Thaqi; the brief says groups of 2–3, solo to be confirmed with the lecturers), HSLU I.BA_DAS, final presentation to Interactive Things on **17.12.2026**. We make a prototype, not a product.

## Client vs. end users (not the same)
- **R4 · Client:** Interactive Things (Zurich), which builds the official platform. **Data owner:** Athena Insights (fieldwork: NORC).
- **R5 · End users:** people who are not AI or data experts. Lecturers review the work but are not the users.

## Target groups, in priority order
1. **R6 · Primary:** students and young professionals in Switzerland (20–35) who use AI tools every week but haven't settled their opinion.
   They want to know whether their unease or enthusiasm is "normal".
2. **R7 · Secondary:** people over 50 who rarely use AI and are mostly worried. They want to know whether they're alone with it.
3. **R8 · Not our focus:** researchers, journalists, policy people. They need the full data platform, which Interactive Things already builds.
- ⚡ **R9 · Our reading:** the audience we can reach and test with is **Swiss**, not American. The data is about Americans.
  We treat that gap as part of the task: comparing yourself to a foreign public, not pretending to be part of it.

## Success criterion: how Interactive Things sees it worked
- **R10:** In the W48 user test, people from the primary group can do three things without help: (a) say where "people like them" stand,
  (b) repeat the main finding in their own words, (c) name one thing that surprised them.
  The final wording comes from the interviews (`../W40_interviews/criteria.md`).

## Non-negotiable guard rails
- **R11 · Neutral towards AI:** no "AI is good / bad" framing. The survey is designed as a neutral instrument, and our design has to be too.
- **R12 · Honest with the data:**
  - "Not sure", "None of these" and "No answer" stay visible (up to ~29 % on some items).
  - The pilot wave (12.06, Prolific, other method) is left out or clearly marked.
  - Differences smaller than the margin of error (±3–4 pts, more for subgroups) are not shown as change or as a gap.
- **R13 · Stays valid for future waves:** a new wave arrives every two weeks. Text uses rounded wording ("two in three", not "68.8 %"),
  numbers are pulled from the latest wave, and no claim depends on a fixed date.
- **R14 · Uncomfortable but true:** party (Dem/Rep) and race/ethnicity subgroups exist in the data. If we show them, we show them without ranking groups as "better" or "worse".
- **R15 · Technical:** data only from the official CSV/JSON. The prototype must run in a browser or on one exhibition station. No backend we can't maintain.

## Data basis
- **R16:** Americans on AI, 7 waves (12.06–10.09.2026), n ≈ 1,000–2,400 per wave, 6 questions / 20 items, 12 subgroups
  (total, gender, party, 4 age bands, 3 race/ethnicity groups). Weighted %, full sample as base.
- **R17 · What the data actually says** (latest wave, see `solutions/W39_data/findings.md`):
  - about 2 in 3 are concerned, about 1 in 5 are excited
  - about 2 in 3 say AI is inevitable, fewer than 1 in 5 think society can shape it
  - about 4 in 5 see people struggling to tell real from fake
  - **barely any movement across waves**
- ⚡ **R18 · Our reading:** the honest headline is **stability, not change**. A tracker invites "what moved this week?" stories,
  but the moves are within the margin of error. We will not build a "trend" story the data doesn't carry.

## Collaboration
- **R19:** Feedback in class from Alain (concept / UX), Gordan (feasibility), Fiona (data). Interactive Things gives feedback at the final presentation.
  Within the group the group decides; when we can't agree, the lecturer of that week decides *(to confirm)*.

## Explicitly not part of the work
- **R20:**
  - a dashboard or full data platform (Interactive Things builds that)
  - all 6 questions × 12 subgroups × 7 waves (we pick)
  - data from other countries or our own survey
  - production-ready code, accounts or tracking
  - making a statement about whether AI is good

## Open points (addressee · deadline)
- **O1:** Does Interactive Things prefer web or exhibition? → Alain · 15.10
- **O2:** Are we allowed to use the name / branding "Americans on AI"? → Alain / Interactive Things · 15.10
- **O3:** Will new waves arrive during the semester, and in the same format? → Fiona · 15.10
- **O4:** Is it OK to address a Swiss audience with US data (R9), or does the client expect a US audience? → Alain · 15.10
- **O5:** Grades vs. "no grades" (the course script and the module description contradict each other) → Alain · 15.10

## Cross-check against the briefing
- [x] Client and end users named separately (R4, R5)
- [x] All target groups covered and prioritised (R6–R8)
- [x] Objective in our own words (R1)
- [x] Content guard rails named, incl. uncomfortable ones (R11–R14)
- [x] Data basis + handling of updates (R13, R16)
- [x] Contacts, feedback points, decision paths (R19; decision path to confirm)
- [x] What is not part of the work (R20)
- [x] How the agency will see it worked (R10)
- [x] Every open question has an addressee and a deadline (O1–O5)
