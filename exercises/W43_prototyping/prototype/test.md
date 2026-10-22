# Test: "Real or AI?" (v1 → v3)

**From the prototype card**
- **Hypothesis:** a reader who first fails (or hesitates) at the guess will feel that the real-vs-fake problem is shared, not a personal weakness.
- **We are wrong if** readers treat it as a quiz score and don't connect the number to themselves.

## How (about 5 minutes per person)
1. Say one sentence only: *"This is a small prototype about AI. Please go through it and think out loud."*
2. Hand over the phone with the newest version open (`v3.html`). **Stay silent for 3 minutes.** Don't help, don't explain.
3. Then ask:
   - "What did you take away?"
   - "What was the number at the end?" (Does the 57 stick?)
   - "Did it feel like a quiz, or like it was about you?"
   - "Was anything unclear?"
4. Two minutes later, ask again: "Which number do you still remember?"

## Acceptance (from the card)
1. Understood without my help
2. Every number is on the source page
3. Surprise: something none of us expected

## Notes

| | Tester 1 | Tester 2 | Tester 3 |
|---|---|---|---|
| Who (age, AI use) | | | |
| Score / longest pause | | | |
| Said out loud while using it | | | |
| "What did you take away?" | | | |
| Number remembered (right away / after 2 min) | | | |
| Quiz or about them? | | | |
| Unclear | | | |
| Surprise | | | |

**What I change in v2 because of this:**

---

## Test 0 · lecturer, in class, 22.10.2026 (v1)
- **Verdict:** "It's good."
- **Liked:** the time pressure (v1 measured the seconds and showed them after each answer).
- **Change:** make the time pressure more obvious.
- **Done in v2:** a visible 5-second countdown, a shrinking bar, and "time's up = not sure" (see `prompts.md`, prompt 3).

## Review 1 · me, 22.10.2026 (v2)
- **The end screen:** the picture tiles and the 100 dots are too cramped.
- **The time:** still not obvious enough; it should be its own element, and funny.
- **Done in v3:**
  - a clock bar with lines that change every second, a burning fuse and a 3-2-1 screen
  - the end is split into "Your result" → "Show me →" → "The number" (see `prompts.md`, prompt 4)
