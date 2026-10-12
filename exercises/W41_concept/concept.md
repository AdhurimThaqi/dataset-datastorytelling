# Concept — v1 (12.10.2026)

**Working title:** *Worried, but it's coming anyway*

## 1 · Starting point (three sentences)
- Two in three Americans are concerned about AI, and just as many think it is inevitable. That share has barely moved since June. (R17, R18)
- Interactive Things builds the platform that shows *all* of this data, so what's missing is a way in for people who would never open a dashboard. (R1, R8, R20)
- Our users are young Swiss adults who use AI every week but haven't sorted out what they think about it. They don't need more numbers. They need to know whether their feeling is "normal". (R6, R9)

## 2 · Target group and their task
- **Who:** students and young professionals in Switzerland, 20–35, weekly AI users, opinion not settled. (R6)
- **Their task:** "Find out whether how I feel about AI is normal, and have one sentence I can use when the topic comes up." (R6, S5)
- **Secondary:** 50+ rarely-users get the same path. The age comparison gives them their own reference point. (R7, S3)

## 3 · Key message (one sentence, no judgement about AI)
> **Most people are worried about AI, and most of them think it's coming anyway. People under 35 are the most likely to think it can still be shaped.**
- Why this message: it is the strongest tension in the data (R17, S2), and it stays true across all waves (R13, R18).
- The second half is the "surprise" for our users (R10c, S3). **Check after every new wave** that the age gap is still bigger than the margin of error. (R12)

## 4 · How it works (the path)
Who leads: **alternating**. The author opens and closes, and the visitor acts in the middle.
Why: the message lands even without interaction, and the visitor's own answer makes it relevant. (R10b, S4)
1. **Hook, authored:** "Real or AI?" One image or quote. The visitor guesses, then sees "4 in 5 Americans say people around them struggle with exactly this." (S1)
2. **You answer, visitor:** the survey's own sentiment question (excited ↔ concerned), with "none of these" as an option. The answer is not stored. "None of these" counts as a full answer, because people often feel both. (R11, R12, R15, S6)
3. **You vs. them, visitor:** your answer next to the US distribution, then by age group. Party and race are available behind a toggle but not shown by default. The core moment: "you're not alone, most people feel this". (R9, R14, S3, S4, S7)
4. **The turn, authored:** the second question ("can society still shape it, or is it inevitable?"). The visitor answers, then sees that most of the worried also say "inevitable", but the young less so. (R17, S2, S3)
5. **Close, authored:** the key message as one sentence to take home, plus the note "US data, latest wave, updated every two weeks". (R13, S5)
- **If someone clicks nothing:** steps 1, 4 and 5 still play as an animatic with the total numbers. The core message gets through. ("If I need to click a lot I'll stop" — P3) (R2, R10b)

## 5 · Data basis
- **Used:**
  - `ai_sentiment` and `ai_agency`: the backbone
  - `ai_community_impact` → "real vs fake": the hook
  - subgroups: total + 4 age bands (party and race only behind the toggle)
  (R16, R17, R14)
- **Latest wave only.** Numbers are read from the CSV at build time. Pilot wave excluded. Text uses rounded phrasing generated from the numbers ("two in three"). (R12, R13)
- **Visible uncertainty:** "none / not sure / no answer" are shown as their own band. Gaps under ~5 pts between subgroups are not shown as differences. (R12)
- **Not used:** trends over waves (no real movement, R18), `ai_family_impact`, `ai_regulation`, `ai_risks` (R20, focus).

## 6 · Design guard rails
- Neutral colours for excited vs. concerned. No red = bad / green = good. (R11)
- The visitor's own answer is shown as one dot among many, not as a "score". (R11) [A: we assume "people like you" without party labels still feels personal → test in W48]
- Every number has "US adults, [wave date]" next to it. Nothing suggests these are Swiss opinions. (R9, R13)
- Works on a phone in portrait first, then on an exhibition screen. (R15) [A: web-first until O1 is answered]

## 7 · How we know it worked (goal → signal → metric, W48 user test, 5 people from R6)
- Find your place → they point to their own age group and say "more / less worried than average" → **≥ 4 of 5** without help. (R10a)
- Understand the tension → they retell the key message in their own words → **≥ 3 of 5**. (R10b, S2, S5)
- Surprise → they name the age gap on "can be shaped" (or another real difference) as unexpected → **≥ 3 of 5**. (R10c, S3)
- Swap these for the criteria from `../W40_interviews/criteria.md` once the interviews exist.

## 8 · Scope of the prototype
- **Built:** an interactive web prototype (HTML + D3/Plotly or Figma) with the 5 steps, real data from the latest wave, and a click-nothing autoplay. (R2, R15)
- **Only described:**
  - exhibition variant: visitors stand on a floor scale "excited ↔ concerned" and the distribution is projected around them [A: fits our immersive-tech angle, depends on O1]
  - automatic update when a new wave arrives (R13, O3)
- **Not built:** dashboard, all questions, accounts, saving answers. (R20)

## 9 · Risks and open questions
- **The interviews are a draft fill-in.** If the real notes contradict S1 (hook), S3 (age axis) or S4 (bridge), steps 1 and 3 change.
- **Small subgroup samples:** in the latest wave, 18–34 has only n = 203 (65+: 340, Black non-Hispanic: 122, from `data.json`). That means roughly ±7 pts or more per group.
  The age gap on "can be shaped" (~19 pts) holds, but smaller gaps may not. → Re-check every wave. (R12)
- **The message could flip:** if a future wave closes the age gap, the second half of the key message disappears. → The first half stands on its own. (R13)
- **Asking the visitor's opinion can feel like a test.** → "None of these" option, nothing is stored, no right answer. (R11)
- **US-only data for a Swiss audience (O4).** If the client wants a US audience, step 6 guard rails and the hook change.
- **Open:** O1 (web vs exhibition), O2 (branding), O3 (new waves) → see rebriefing.

## Abstraction ladder
- ↑ Why? → So people can discuss AI based on what others actually think, not on headlines.
- ↑ Why? → So that someone worried about AI knows they're in the majority, and that "inevitable" is a belief, not a fact.
- **Problem statement:** *We show people where their feeling about AI stands, and that worry and resignation usually come together.*
- ↓ How? → The visitor answers the two survey questions themselves and sees their answer inside the US distribution, by age.
- ↓ How? → One screen per question: a dot field of 1,000 people, the visitor's dot highlighted, and the "inevitable" answer re-colours the same dots.
