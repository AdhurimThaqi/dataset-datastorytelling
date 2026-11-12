# Sprint 3 · v7: Real or AI? as a full game (12.11.2026)

**Open it:** [`v7.html`](v7.html) (needs the `img/` folder next to it; works offline except for the font)

## What changed from v6
| Feedback (lecturer) | v7 |
|---|---|
| You always have to scroll and click "Next" | Each screen fits the window. After an answer the result card slides over the picture and the game **moves on by itself** (tap or Space to skip, "Keep open" to read). Swipe right = real, left = AI on a phone; ← / → keys on a laptop. |
| The sides are empty: use them, better UI/UX | **3-column game layout** on a laptop: **player card** on the left (score, streak 🔥, rank, the 7 levels with ✅/❌ per answer, badges) · **stage** in the middle · **field notes + leaderboard** on the right. Tablet: 2 columns + a top bar. Phone: top bar + a bottom sheet for notes and the leaderboard. Light and dark mode. |
| Gamification is good, but only at the beginning | **7 levels**, points everywhere: speed bonus, streak bonus, a hint costs 40, ×1.5 in hard mode. **8 badges** (Eagle eye, Lightning, On fire, Bullseye, Data nerd, Fact-checker, Mind reader, No hints) and a rank title (Doom-scroller → AI whisperer). |
| Learn something while playing with the data | The data part is now games: **guess the number** (slider over 100 dots → the 57), **more or fewer** (5 "seen in your community" items from the same survey), **true or false** (claims about AI risks and families, sometimes with a wrong number), **predict America** (your own answer, then guess how many are concerned / say "coming anyway"). Every answer adds a **clue or fact** to the field notes, and the end screen shows "What you learned". |
| Competing, a leaderboard | **Leaderboard** (top 10 on this device, good for pass-the-phone tests) and a **"Challenge a friend" link**: same pictures, same questions, and your score shown as the score to beat (live race bar while they play). No server, nothing is sent anywhere. |
| Pictures too easy to tell apart | **Hard mode:** 8 photoreal AI pictures made for this prototype (gpt-image-2.5, gemini-3.1-flash-image) of the same valleys as the real photos (Val Bavona, Verzasca, Lauterbrunnen, Foroglio), prompted to look like ordinary phone photos (haze, signposts, power poles, a car mirror). Plus 9 real photos that *look* fake (mist, long exposure, turquoise water, heavy editing). **All 35 pictures** are cropped, resized and compressed the same way and renamed `p01…p35`, so the file name, size or format give nothing away. The warm-up keeps the older, easier pool from v6. |

Honesty rules still apply: "too close to call" in more-or-fewer when two items are within the margin of error, the age gap only called a gap if it beats the combined margin of error, true-or-false always shows the real number after the answer.

## Files
| File | What |
|---|---|
| `template.html` | The page, **without numbers**: edit this one |
| `prepare_images.py` | Downloads the Commons pictures, crops/compresses every picture the same way, writes `img/p01…p35.jpg` and `pool.json` (answer, credit, licence, "how to tell" per picture) |
| `img/originals/` | The 8 generated AI pictures at full size (proof of origin; not used by the page) |
| `build.py` | Writes `v7.html` with the numbers from the CSV + `pool.json` |
| `check.py` | Every number in `v7.html` against the CSV: `149 checks … 0 mismatches` |

**Review shortcuts:** `?step=warm|hard|text|boss|hilo|tf|you|turn|end` · `?theme=dark|light` · `?limit=8` (seconds per picture) · `?reset` (forget which pictures you've seen). Review shortcuts never save to the leaderboard.

## Status (12.11.2026)
- ✅ `check.py`: 149 checks, 0 mismatches
- ✅ full playthrough in headless Edge at 1440×900, 1024×768 (dark) and 390×844 (touch, with a swipe): all 7 levels to the end, no script error, no sideways scrolling, challenge link reproduces the same pictures
- ⏳ on a real phone
- ⏳ testers: is it too long now (~5 min)? Is hard mode *too* hard?
