# W43 in class (22.10.2026, Gordan Savičić): paper tasks

Slides: https://ex.yugo.at/hslu/datastorytelling/W43_Slides.html
Rule of the day: **one direction · one aspect of the data · one interaction · one test.**

## 1 · Crazy 6's (on paper, before any chatbot)
- Fold an A4 sheet into six boxes. One minute per box, alone.
- Each box: a sketch + two lines: **"The reader … and then sees …"**
- At least one box is an interaction never seen in a data visualisation.
- Stuck? Take a verb: guess · sort · drag · place yourself · choose · compare · wait · reveal · answer · hold.
- Then vote: two dots each on the most promising boxes (only one on your own sheet).
- 📷 Photo of the sheet → `photos/W43_crazy6.jpg`

## 2 · Prototype card (A5, for the winning box)
Draft for direction A. **Check it against what you wrote on paper and correct it to match.**

```
PROTOTYPE CARD — Adhurim Thaqi (solo)
DIRECTION   A · "Real or AI?" (web)
DATA        "Thinking about your local community, how much are you seeing each of the following
            changes because of AI? People are struggling to tell what's real from what's fake"
            Americans on AI, total, wave 10–14 Sep 2026 (n = 1,083):
            have seen 57 · starting to see 24 · expect soon 9 · don't expect 2 · not sure 7 · no answer 1
            (Release 003, p. 4, July wave: 57 of 100 have seen it)
ACTION      The reader guesses whether one image is real or made by AI,
            and then sees that 57 of 100 Americans have already seen people around them struggle with exactly this.
HYPOTHESIS  A reader who first fails (or hesitates) at the guess will feel that the real-vs-fake problem
            is shared, not a personal weakness.
            We are wrong if readers treat it as a quiz score and don't connect the number to themselves.
ACCEPTANCE  1. Understood without our help
            2. Every number is on the source page
            3. Surprise: something none of us expected
```

## 3 · Build and test (rest of the lesson)
- Build **one HTML file** with an LLM: guardrails → experience (longest part) → one design reference → the data word for word.
  Interaction first, one change per prompt, save `v1.html`, `v2.html` …, check every number against the source.
- Test with a stranger: one sentence of introduction, three minutes of silence, then *"What did you take away?"*
- Write down what they said → it feeds next week's concept refinement.

## Next week (W44, remote)
- Refine the concept with what the test showed.
- Two or three design references, and what you borrow from each.
- The HTML file and **all prompts** in the research documentation.
