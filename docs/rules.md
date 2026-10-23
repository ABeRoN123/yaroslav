# Made to Want — working rules (merge into CLAUDE.md)

Imported 2026-10-23 from the claude.ai project "Юруб", where episodes 1–5 were made.

## Who / how to talk
- Owner: Yaroslav, lives in Poland (Europe/Warsaw). Works physical rotating shifts (a month of days, a month of nights). During the day he writes from his phone; computer work happens in the evening. He is often away or asleep, so make reasonable decisions yourself and report at the end with links.
- **Talk to him in Russian.** Everything meant for AIs (image and animation prompts, scripts, VO text) is **in English**.
- Never create accounts, enter passwords or permanently delete anything. He deletes videos himself. To retire a video, set it to "Ограниченный доступ".
- Ask before accepting any terms or consent dialogs. Post to TikTok only when he says so.

## The channel
- **Made to Want**: https://www.youtube.com/channel/UCC972vQMbqKBQLeccmoYBOg (an old channel that was renamed).
- Hand-drawn doodle video essays about how marketing invented our desires. Tagline: "Who decided what you want?"
- Title pattern: "The ___ You Were Told to ___".
- Long videos run 5–10 min and must never go over 10. There are also ~5–6 Shorts per video.
- Target pace: 3 long videos a week plus 1 Short a day (an aspiration; real pace is about one long video every 2–3 days).
- **Shorts: one per day.** Publish time is not fixed: the owner names it right before scheduling (past batches used different times). Ask, never assume.
- Long videos go out when he says. His note: aim at a US audience, 11:00–14:00 New York (≈17:00–20:00 Warsaw).

## Tools and accounts he uses
- **Google Flow** (flow.google.com): Nano Banana 2.1 images at 16:9, **x1 = one image per prompt** (x2 uses up too much). Animations use Omni 1.1 Flash, 720p, 6 s, x1. Turn the "Агент" switch off.
- **ElevenLabs** (paid, ~120k characters/month): voice "Jack John – Conversational and Upbeat", Eleven v4, stability 50%, similarity 75%. **Language = English, NEVER Auto** (Auto once produced Polish in a short). Generate one file per chapter, or one per short, with the text pasted as ONE line.
- **YouTube Studio**: uploads go through Claude in Chrome (his logged-in Chrome). Files bigger than 10 MB are split into 9 MB parts, which helper `<input type=file>` elements reassemble via JS Blob, then compare the sha256.
- Storage on his PC: `D:\клод ютуб\NN Title\` with subfolders `кадры\`, `анимации\`, `озвучка\`, `shorts\`, plus the final mp4 (sometimes as parts with `join_video.bat`), .srt, thumbnail and youtube_description.txt. Shared folders: `D:\клод ютуб\_персонажи\` (character_bible.txt, character sheets) and `D:\клод ютуб\_инструменты\` (scripts).

## Must-do checklist per long video (lessons learned)
1. Verify the facts with sources before writing → story.md. Hedge shaky claims ("reportedly").
2. The hook states the twist in the first sentence. Write numbers as words in the VO.
3. Storyboard: one shot per VO sentence or phrase, ~4–6 s each. Animate only the strongest moments (~15 per 10 min).
4. Make a character card per main character first and attach it as a reference for every shot. People without a card need the people/style sentence in the prompt.
5. Add the CROWD sentence only to prompts that really show several people. On single-figure scenes, such as an ad page, it adds random crowds.
6. Flow filters:
   - Bare legs drawn without a body get blocked as "sexual", so show a whole clothed character instead.
   - Naming a real person in an animation prompt triggers the "famous people" block, so say "the man".
   - Omni invents explosions or bursts in "pop up / transfer" actions, so say what must NOT happen.
7. **Text overlays BEFORE render (forgotten in ep4 v1, and the video had to be redone):**
   - title card text;
   - every chapter card ("CHAPTER N" + title, Inter Display Black);
   - long ad or quote text on blank banners;
   - the end card "MADE TO WANT / who decided what you want?".
   See scripts/ep4_long/overlay.py.
8. After timing, check that **every chapter card is on screen for ≥2.5 s**. In ep4 a DP misalignment made chapter 5 flash for 1 s.
9. QA every frame for complete faces (one mouth, two equal eyes, a nose), crowds drawn in the same style as the heroes, colored hair, and no blank papers.
10. After publishing:
    - set "Видео по теме" on each Short to the long video;
    - Short descriptions include "Full story: <link>";
    - update the status doc.

## Visual style
See channel/style-guide.md.
