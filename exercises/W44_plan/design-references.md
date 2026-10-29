# Design references: what we borrow from each

Three references, one per part of the story: the **hook**, the **guess before the reveal**, and **you vs. a representative survey**.
→ Add a screenshot of each to the Google Doc.

## 1 · "Which Face Is Real?": for the hook (step 1)
- **What:** a web game by Jevin West and Carl Bergstrom (University of Washington, *Calling Bullshit* project). Each round shows a real photo next to an AI-generated face, and you click the real one.
- **Link:** https://www.whichfaceisreal.com/
- **We borrow:**
  - **a big pool, drawn at random**, so every round is new. That's the fix for our test finding ("predictable after several plays").
  - right after each answer, show **what it was** and **a short explanation**
- **We don't borrow:**
  - endless rounds. Ours stops after 4, because the guess is the way *into* the data, not the goal.
  - faces of people. We keep landscapes, so no real person's face is used.

## 2 · NYT The Upshot, "You Draw It: How Family Income Predicts Children's College Chances" (2015): for guess → reveal (steps 1–2)
- **What:** the reader draws the line they *expect* first, then the real data line appears over their guess.
- **Link:** https://www.nytimes.com/interactive/2015/05/28/upshot/you-draw-it-how-family-income-affects-childrens-college-chances.html
- **We borrow:**
  - **commit first, then see the data:** your own guess makes the real number stick
  - the reveal compares **your answer with the real one** on the same screen
- **We don't borrow:** drawing a line. Our guess is a two-button choice (Real / AI) that you can make with your thumb in 5 seconds.

## 3 · Pew Research Center, "Political Typology Quiz": for you vs. America (steps 3–4)
- **What:** you answer the survey's questions and see which of nine groups you fit. The quiz is compared with a nationally representative survey of more than 10,000 US adults.
- **Link:** https://www.pewresearch.org/politics/quiz/political-typology/
- **We borrow:**
  - **the survey's own question, word for word**, so your answer can really be compared
  - **placing you inside a representative sample**, not inside a comment section (interview 2: *"whether the people commenting represent the wider population"*)
- **We don't borrow:**
  - many questions and a label for you. We ask one question and show your dot among 1,000.
  - no political groups. Party is not our default view (guard rail).

---
**Checked on 29.10.2026:** the links and descriptions of 1 and 3 were checked online. Reference 2 (NYT) couldn't be opened automatically, so please open the link once to check it.
