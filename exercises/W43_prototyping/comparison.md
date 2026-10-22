# Comparing A / B / C

> **This is a recommendation for the group to decide.** It is not a decision. Discuss it in class on 22.10, then fill in the "Decision" line at the bottom.

**Scale:** ●●● strong · ●● partly · ● weak.
**Criteria:** from `../W40_interviews/criteria.md`.

## Against our success criteria

| Criterion | A · Real or AI? (web) | B · Stand where you feel (exhibition) | C · Dinner table (branched animatic) |
|---|---|---|---|
| **C1:** say whether "people like them" are more or less worried than average | ●●● own dot + age tabs, with an explicit "more / less / about the same" sentence | ●●● physical: "I stand here", then age lanes | ●● you pick a seat but never place yourself |
| **C2:** find a moment that matches their own AI experience | ●●● the real-or-AI hook *is* the shared experience (81.5 %) | ● no real-vs-fake moment yet (it could be added at the entrance) | ●●● the fake video at the table and the dinner conversation |
| **C3:** repeat the main finding in their own words | ●● one closing sentence | ●● wall text, easy to miss in a group | ●●● the message is literally said at a table |
| **★ Surprise:** young people feel more able to shape AI | ●● step 5, bars by age | ●●● the younger lane lights up on the flip | ●●● two diners face each other: 27 vs 8 |
| **Non-clicker / passer-by** | autoplay 1 → 2 → 5 → 6 | loop of the room states | default branch after 8 s |
| **Guard rails** (neutral, no party default, uncertainty visible) | ✅ quiz feel = risk | ✅ exposure in public = risk | ⚠️ stereotype risk, labelled as fictional |

## Feasibility for week 44 (implementation plan) and the W48 user test

| | A | B | C |
|---|---|---|---|
| **Hand-in format** (brief section 06) | interactive prototype | animatic | branched animatic |
| **Tech** | 1 HTML page, plain JS/SVG; data as JSON generated from the CSV. **The AI draft already runs.** | projector + floor tracking (depth camera / pressure mats), or Wizard-of-Oz with paper. Animatic = video of the room states. | video/animation tool (Figma, After Effects, or HTML with 2 branches). Script, voice, timing. |
| **New waves** (R13) | rebuild = run `build.py` | re-render the animatic | re-record the lines with new numbers |
| **Effort until W51** | low–medium | high (hardware, space) | medium (writing-heavy) |
| **Testable in W48 with 5 people from R6** | ✅ online or on a phone, alone | ⚠️ needs a room; paper floor + moderator possible | ✅ play the video, ask them to retell |
| **Dependency on open points** | O1 (web vs. exhibition), O2 (name/branding) | O1 (must be exhibition) | O1 (either works), O2 |
| **Biggest unknown** | Does answering feel like a test? | Do people dare to stand on "very concerned" in public? | Do invented characters feel like real voices / stereotypes? |

## Recommendation (for the group to decide)

- **Take A into W44 as the main direction.**
  - It covers all three criteria + the surprise (no ● anywhere).
  - It matches concept v1 and fits the web context.
  - It can be tested in W48 without a room.
  - A working draft with verified numbers already exists (`ai-draft/`).
- **Borrow from C:**
  - the "dinner table" framing for step 6, so it's easier to retell (C3 is A's weakest point)
  - C's rule "only speak a gap if it beats the margin of error", which A already uses in the tab text
- **Keep B as the "only described" exhibition variant** (concept section 8). Its "348 of 1,000 stand here with you" line can be A's step-4 sentence.
- **Reconsider if:**
  - O1 comes back as "exhibition". → Then B (or C on a table screen) becomes the main direction, and A turns into its web companion.
  - The hand-sketch critique on 22.10 shows people prefer C's retelling.
- **Before W44:** settle the closing wording.
  - "Under 35 are the *most* likely to think it can be shaped" (concept v1) isn't supported: 18–34 vs 35–49 is inside the margin.
  - Use "younger adults are more likely than older adults" instead (see `ai-draft/checks.md` section 2).

**Decision (group, date):** _______________________
