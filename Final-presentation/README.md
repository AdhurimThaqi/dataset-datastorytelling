# Final presentation · 17.12.2026 · Interactive Things

| File | What |
|---|---|
| `slides.html` | The deck in the browser. → / Space next, ← back, **F** fullscreen, **N** speaker notes. Slide 2 opens the live room. Print it (Ctrl+P) for one slide per page |
| `Real-or-AI_final-presentation.pptx` | The same 13 slides in PowerPoint, with speaker notes, fade transitions and build-in animations (they run by themselves) |
| `Real-or-AI_final-presentation.pdf` | Backup without animations |
| `build_deck.py` | Fills my slide template with the content and exports the PDF: `python Final-presentation/build_deck.py path/to/template.pptx` (the template isn't in the repo) |
| `img/` | Phone screenshots of v8, the QR code for room HSLU, and the favicon (the ? logo on the cover and the last slide) |

The design comes from my own template (Syne + Outfit, cyan gradient). The numbers match what v8 shows,
and v8's numbers come from the official CSV (`check.py`: 149 checks, 0 mismatches).

**On the day:** open `slides.html` (or the PowerPoint), and on slide 2 open the live room (`live.html?room=hslu`, press F).
Give the audience about four minutes, show the top 10, then go on. The day before, open the live page once,
because free Supabase projects pause after about a week without use.
