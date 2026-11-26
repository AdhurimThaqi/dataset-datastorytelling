# Sprint 3 · v7: Real or AI? as a full game (12.11.2026, polished 19.11.2026) · v8 (26.11.2026)

**Open it:** [`v8.html`](v8.html), the current version · [`v7.html`](v7.html), the version from the 19.11 coaching (kept unchanged). Both need the `img/` folder next to them; they work offline except for the font.

## v8: what changed after the coaching (19.11)
| Feedback (coaching) | v8 |
|---|---|
| 7 levels are too many | **5 levels:** 🌄 Real or AI? (6 pictures: 2 easy, then 4 in 🧨 hard mode at ×1.5; a toast marks the switch) · ✍️ Texts · 🎯 The number · ⚡ True or false · 🫵 Your turn. 8 pictures and texts instead of 10, about 4 minutes. |
| "More or fewer": unclear what "fewer" means | **Removed.** Its five "seen in your community" numbers are still in "Sources and all numbers". The "Data nerd" badge went with it (7 badges now). |
| Add clicking as well as dragging | The **AI / REAL buttons and 💡 Hint now work when tapped or clicked.** In v7 they had no click handler, so only swipe and keys worked. |
| Leaderboard: only on the device | Still no server (nothing is uploaded), but the **challenge link does more:** it carries your points per level. Your friend gets a **head-to-head per level** at the end and a **"Send to …" reply link**. When you open it you see who won and can play the rematch on the same pictures. Every score that reaches you by link goes on your device's leaderboard, marked 🔗. On a phone, **Share** opens the system share sheet (WhatsApp, Messages, …) with a ready-made message. |

Leaderboard key is now `realOrAI.board.v8`: v8 has fewer pictures, so v7 scores would not compare.
Checked 26.11: `check.py` 149 checks, 0 mismatches. Played through three times in headless Edge at 390×844 (touch): player A, then B from A's link, then A opening B's reply. All 5 levels, the head-to-head and the 🔗 board entries worked, with no script errors and no sideways scrolling. Still to do: try it on a real phone.

---

# v7 (the version before)
## What changed from v6
| Feedback (lecturer) | v7 |
|---|---|
| You always have to scroll and click "Next" | Each screen fits the window. After an answer the result card slides over the picture and the game **moves on by itself** (tap or Space to skip, "Pause" to read). Swipe right = real, left = AI on a phone; ← / → keys on a laptop. |
| The sides are empty: use them, better UI/UX | **3-column game layout** on a laptop: **player card** on the left (score, streak 🔥, rank, the 7 levels with ✅/❌ per answer, badges) · **stage** in the middle · **field notes + leaderboard** on the right. *(19.11: the side panels are now slim pillars, see below.)* Phone: top bar + a bottom sheet for notes and the leaderboard. Light and dark mode. |
| Gamification is good, but only at the beginning | **7 levels**, points everywhere: speed bonus, streak bonus, a hint costs 40, ×1.5 in hard mode. **8 badges** (Eagle eye, Lightning, On fire, Bullseye, Data nerd, Fact-checker, Mind reader, No hints) and a rank title (Doom-scroller → AI whisperer). |
| Learn something while playing with the data | The data part is now games: **guess the number** (slider over 100 dots → the 57), **more or fewer** (5 "seen in your community" items from the same survey), **true or false** (claims about AI risks and families, sometimes with a wrong number), **predict America** (your own answer, then guess how many are concerned / say "coming anyway"). Every answer adds a **clue or fact** to the field notes, and the end screen shows "What you learned". |
| Competing, a leaderboard | **Leaderboard** (top 10 in this browser, not a global ranking, good for pass-the-phone tests) and a **"Challenge a friend" link**: same pictures, same questions, and your score shown as the score to beat (live race bar while they play). No server, nothing is sent anywhere. |
| Pictures too easy to tell apart | **Hard mode:** 8 photoreal AI pictures made for this prototype (gpt-image-2.5, gemini-3.1-flash-image) of the same valleys as the real photos (Val Bavona, Verzasca, Lauterbrunnen, Foroglio), prompted to look like ordinary phone photos (haze, signposts, power poles, a car mirror). Plus 9 real photos that *look* fake (mist, long exposure, turquoise water, heavy editing). **All 35 pictures** are cropped, resized and compressed the same way and renamed `p01…p35`, so the file name, size or format give nothing away. The warm-up keeps the older, easier pool from v6. |

## Polish after the coaching (19.11.2026)
| Feedback (coaching + two outside reviews) | Change |
|---|---|
| The side panels take attention away from the game | While you play, both sides are **slim pillars** (score, streak, level dots, newest badge · notes count, best score). **Hover** (short delay so it doesn't flicker), keyboard focus or a tap **opens** the full panel over the game; 📌 keeps it open. The start screen opens only the leaderboard, the end screen opens both. Same on laptop and tablet; the phone keeps the top bar + bottom sheet. |
| Start screen, round types, scoring are unclear | Each level splash shows its **type** (image / text / data challenge, knowledge check, your opinion) and **how points work**. After every picture or text the card shows the **breakdown** (e.g. `100 right + 32 speed + 40 streak 🔥`, or "0 points · your 3 streak is reset"). |
| It's not clear you can drag the card | The first two warm-up pictures and the first text show **"👆 Drag / Swipe the picture: ← AI · Real →"** (Swipe on touch, Drag with a mouse); the first picture also wiggles once. It disappears on the first touch or answer. Keyboard hints only on devices with a keyboard. |
| Survey questions are vague, "Americans" vs Swiss | The boss question names population, subject and measure ("Out of 100 US adults, how many have already seen…") and shows the survey's own wording. Boss, more-or-fewer and true-or-false all say **"Survey of US adults"**, with dates and n. |
| Levels feel disconnected | **Story bridges** on the level splashes link the picture game to the survey ("That was hard for you. Is it hard in real life too?…"), with extra reading time before the countdown. |
| The end screen only shows a score | New **"You vs. US adults"**: your hit rate, boss guess, prediction, feeling and view, each next to the real survey number. |
| Answer card moves on too fast | Longer (6.5 s pictures, 9 s texts); **⏸ Pause → Next ▶** with matching screen-reader labels; it also waits while the mouse or keyboard focus is on the card. |
| Accessibility | Phone sheet: ✕ button, Esc closes it, a closed sheet can't be tabbed into, focus moves in and back. Picture alt text says what is shown and never gives away the answer. Sound button says whether sound is on. Name field explains it's saved only in this browser. |
| Bugs found on the phone | Text cards couldn't be swiped (the text box was a scroll box, so the browser took the sideways swipe); fixed. A toast left a small blob at the top; fixed. |

Not done on purpose: fewer emoji across the whole UI (design decision still open).

Honesty rules still apply: "too close to call" in more-or-fewer when two items are within the margin of error, the age gap only called a gap if it beats the combined margin of error, true-or-false always shows the real number after the answer.

## Files
| File | What |
|---|---|
| `template.html` | The page, **without numbers**: edit this one |
| `prepare_images.py` | Downloads the Commons pictures, crops/compresses every picture the same way, writes `img/p01…p35.jpg` and `pool.json` (answer, credit, licence, "how to tell" per picture) |
| `img/originals/` | The 8 generated AI pictures at full size (proof of origin; not used by the page) |
| `build.py` | Writes `v8.html` with the numbers from the CSV + `pool.json` (v7.html is kept as it was) |
| `check.py` | Every number in `v8.html` against the CSV: `149 checks … 0 mismatches` |

**Review shortcuts (v8):** `?step=pics|text|boss|tf|you|turn|end` (v7: `warm|hard|text|boss|hilo|tf|you|turn|end`) · `?theme=dark|light` · `?limit=8` (seconds per picture) · `?reset` (forget which pictures you've seen). Review shortcuts never save to the leaderboard.

## Status (19.11.2026)
- ✅ `check.py`: 149 checks, 0 mismatches
- ✅ full playthrough in headless Edge at 1440×900, 1024×768 (dark) and 390×844 (touch, with a swipe): all 7 levels to the end, no script error, no sideways scrolling, challenge link reproduces the same pictures
- ✅ 19.11: pillars, phone sheet, drag hint, splash bridges and end screen checked in headless Chrome at desktop and 390 px phone width; no script errors
- ⏳ swipe on texts on a real phone (fixed, not yet confirmed on a device)
- ⏳ user test with 5 people on phone, tablet and laptop: is it too long (~5 min)? Is hard mode *too* hard? Do people find the drag and the pillars without help?
