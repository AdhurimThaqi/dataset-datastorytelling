# Concept — draft v0 (data-based; revise after the 3 interviews)

> Everything marked *(assumption)* is not yet backed by an interview. After W40, keep what a quote supports, change the rest.

**Working title:** *Where do you stand?*

1. **Who is it for?** Young adults 20–35 who use AI regularly but haven't settled their opinion *(assumption — confirm in interviews)*.
2. **What should they know or do afterwards?** Know where people like them stand on AI, see that worry is the majority view — and notice
   the gap between being worried and feeling able to do anything about it.
3. **Key message (one sentence):** *Most Americans are worried about AI — and most of them believe it is coming anyway.*
4. **Points of connection:**
   - their own answer: the visitor first answers the survey's main question themselves (as in *You Draw It*)
   - their own group: age, gender, party → "people like you" (NYT *Jobless Rate for People Like You*)
   - their own experience: "struggling to tell real from fake" — 82 % already see it *(likely shared by our target group)*
5. **Who leads?** Alternating, like *The Fallen of World War II*: an authored opening (the big picture) → the visitor takes over
   (answer, pick your group, explore) → authored ending (the tension "worried but powerless").
   Why: the author guarantees the main message lands; the visitor's own choices create relevance.
6. **What does someone get who clicks nothing?** The authored path still plays: "Two in three are worried. Two in three say it's inevitable." + one strong visual.
7. **How will we know it worked?** (goal → signal → metric)
   - Find your place → visitor locates their group → ≥ 4 of 5 test users manage it without help
   - Understand the tension → they can repeat the key message in their own words → ≥ 3 of 5
   - Surprise → they name something unexpected about another group → ≥ 3 of 5
8. **Context:** web first (reach, easy to test); exhibition variant possible — e.g. visitors physically stand on a floor scale
   "excited ↔ concerned" and see the survey distribution projected around them *(fits an immersive-tech angle, decide with group)*.
9. **Data & currency:** `ai_sentiment` + `ai_agency` as the backbone, `ai_community_impact` (real vs fake) as the hook, subgroups for comparison.
   Text uses rounded wording ("two in three"), numbers pull from the latest wave, pilot wave excluded → stays valid when new waves arrive.
10. **Prototype scope:** interactive web prototype (Figma or HTML) with real data for the latest wave; trend and other questions only described.
11. **Risks & assumptions:**
    - US data, Swiss audience → is "people like you" still relevant if the visitor isn't American? *(ask in interviews!)*
    - Party labels (Dem/Rep) mean little to Swiss visitors → maybe use age/gender only
    - Subgroup sample sizes are small → differences can be noise; show uncertainty
    - Asking the visitor's party/age can feel intrusive → make it optional

## Abstraction ladder
- ↑ Why? → A charged debate becomes accessible: people can place their own attitude in relation to others.
- ↑ Why? → So that people feel less alone with worries, and can discuss AI on the basis of facts instead of headlines.
- **Problem statement:** "We show how Americans feel about AI."
- ↓ How? → The visitor answers the sentiment question, then sees their own group compared to the total and to the opposite group.
- ↓ How? → One screen: dot plot of 12 groups, "you" highlighted; then the "inevitable" question flips the picture.
→ We work on the "How?" rung directly below the problem statement.
