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

## Notes · 3 testers, week of 22.10.2026 (v3)

| | Tester 1 | Tester 2 | Tester 3 |
|---|---|---|---|
| Who (age, AI use) | not recorded | not recorded | not recorded |
| Score / longest pause | not recorded | not recorded | not recorded |
| Said out loud while using it | not recorded | not recorded | not recorded |
| "What did you take away?" | positive; liked the idea | positive; liked the idea | positive; liked the idea |
| Number remembered (right away / after 2 min) | yes, remembered the 57 | yes, remembered the 57 | yes, remembered the 57 |
| Quiz or about them? | not a quiz; a fun game challenge | not a quiz; a fun game challenge | not a quiz; a fun game challenge |
| Unclear | nothing, everything was clear | nothing, everything was clear | nothing, everything was clear |
| Surprise | not recorded | not recorded | not recorded |

**Summary**
- **Positive overall.** All three testers liked the idea.
- **The timing works.** Testers named the time pressure as what they liked, which confirms the lecturer's comment from Test 0.
- **It's fun and clear.** It felt like fun, and all three understood it without help (acceptance point 1 ✅).
- **The number sticks.** All three still remembered the 57 two minutes later.
- **Not a quiz.** It didn't feel like a quiz at all, more like a fun game challenge. So the "we are wrong if" case on the prototype card (people treat it as a quiz score) didn't happen.
- **The issue: it gets predictable.** After playing it several times, testers knew the answers, because there are only four pictures and always the same ones. Replaying the guess loses its point.

**What I change in v4 because of this:**
- A bigger pool of pictures, with a random selection each round, so a second play is not a repeat.
- **Done in v4 (29.10.2026):** 16 pictures (8 real, 8 AI). Every round draws 2 real + 2 AI, with no repeats until the pool is used up (see `prompts.md`, prompt 5).

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
