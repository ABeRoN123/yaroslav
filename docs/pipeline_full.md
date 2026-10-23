
# Made to Want — video production pipeline

Channel: **Made to Want** (YouTube + TikTok). Hand-drawn doodle video essays about how marketing invented our desires. Tagline: "Who decided what you want?" Talk to the user in **Russian**; everything for AIs (prompts, scripts, VO) in **English**.

Target pace: **3 long videos per week** (Mon/Wed/Fri) + **1 short per day**.

## 0. Start of every new chat
- The user starts a NEW chat in the project "Юруб" for each task (to save tokens). First read the project docs: `epNN_*/status.md` (what is published / scheduled / TODO), story.md, storyboard.json, vo_chapters.txt, shorts_vo.txt, char_cards.json.
- Check the PC folder `D:\клод ютуб\NN Title\` before generating anything — another chat may already have made VO, frames or animations. Never redo finished work.
- At the end of a task write/update `epNN_*/status.md` in the project (links, schedule, TODO).

## Storage (user's PC, via device bridge)
- Root: `D:\клод ютуб\`
- One folder per video: `D:\клод ютуб\NN Title\` with `кадры\` (kadr_001.jpg… or one kadry_NNN.zip), `анимации\` (anim_NNN.mp4), `озвучка\` (vo_01_hook.mp3…, shorts_vo.mp3), `shorts\`, plus final mp4, .srt, thumbnail, youtube_description.txt.
- Shared: `D:\клод ютуб\_персонажи\` (character sheets, character_bible.txt, per-video cards), `D:\клод ютуб\_инструменты\` (smoothzoom.py; latest pipeline: ep3_timing.py, ep3_render.py, ep3_shorts.py, ep3_overlay.py; older render.py, shorts.py, align3.py, srt.py).

## Getting files out of the browser without the user
- Any browser download (blob `<a download>` or Flow's Скачать) lands in `C:\Users\tabar\Downloads` as a GUID `.tmp` file **with full content even if the user never confirms the save prompt** (or under its real name if confirmed). So: download, `device_list_dir` Downloads, match new files by size / mtime order, `device_stage_files` them, rename in the container. Keep a list of download order.
- **Flow frames, fastest:** `img[data-media-id]` → its `src` (same-origin flow.google.com/asb/… URL, 1376×768 jpg). Front the tab (background tabs don't lazy-load), scroll the grid to map media-id → src, `fetch()` the picked ones, build a store-only ZIP in JS (CRC32 + local/central headers) and download ONE zip.
- Flow video files can't be fetched by JS (CORS) — use the tile menu (can be clicked via JS): in `flow-video-tile` click `more_vert` → Скачать → 720p. Files are named after the clip title → map titles to shots. Never use an `<a>` to the video URL (navigates the pane away). Close the "Видео скачано" toast before the next tile.
- ElevenLabs: after each generation click the first `button[aria-label="Pobierz"]`; file names carry the generation timestamp — map by it and by duration.
- Keep the number of downloads small (each pops a prompt; many prompts once crashed the app). If the user says not to download yet, generate only and leave downloads for later.
- Commit results back with `device_commit_files` (stagedPath under /mnt/user-data/outputs/). Reliable only up to ~20 MB per file; bigger → split into ≤19 MB parts + a `join_video.bat` (`copy /b part_00 + part_01 + … "name.mp4"`).

## 1. Topic & script
- Real, verifiable marketing history (names, dates, ads). Verify facts with web search before writing. Save the verified outline with sources as `epNN_*/story.md`.
- Title pattern: "The ___ You Were Told to ___".
- Structure: cold-open hook that states the twist in the FIRST sentence → title → chapters → "why it still works" → callback ending → "Made to Want."
- Length: default ~5 min (~800 words); when the user asks for a long video, up to ~9.5 min (~1450 words, 6–7 chapters). Never over 10 min.
- Long-form retention is only 23–30%: the first 30 seconds matter most.
- Write numbers as words in the VO text. Hedge shaky claims ("reportedly", "one study found").

## 2. Storyboard
- One shot per VO sentence or phrase, ~4–6 s each (≈80 shots per 5 min, ≈140 per 9.5 min). Mark only the strongest moments for animation (8–10 per 5 min, ~15–17 per 10 min).
- Each shot: number, chapter, VO line, scene description, characters, animation prompt (if any).
- Build it with a Python script (build.py) that assembles prompts = scene + character descriptions + CROWD rule + STYLE, and writes storyboard.json, char_cards.json and vo_chapters.txt (one line per chapter).
- Append the CROWD sentence only to scenes that really have several people — on single-figure scenes (a vintage ad page, a diagram) it makes Nano Banana add random crowds.
- Flow's video filters: disembodied bare legs get blocked as "sexual" — show a whole clothed character shaving instead; naming a real person in an animation prompt triggers the "famous people" block — say "the man".
- Vary framing: close-up / medium / wide, plus infographic shots.
- Publish the storyboard as an HTML artifact for review.

## 3. Frame quality rules (user's checklist — apply to every prompt and check every frame)
1. **Crowds match the heroes.** Background people have the same big round heads, faces (2 eyes, nose, mouth), clothes and proportions as main characters; smaller only by perspective, never simplified, faceless or silhouettes. Append the CROWD sentence to every prompt with people.
2. **Papers are never blank.** Short text (1–4 words, a number, a headline) goes straight into the prompt in quotes and Nano Banana letters it. Long text is overlaid in the edit. Other pages show neat gray scribble lines, never gibberish letters.
3. **Colored hair.** Brown, black, auburn, blonde, chestnut; gray only for elders; never plain white hair. Never white clothes + white hair together (looks uncolored).
4. **Fingers:** reject only obvious deformities.
5. **Complete faces:** exactly one mouth, two equal eyes, a nose — on everyone, including distant figures. Main defect of earlier videos.
6. **Same character, same look** across shots: outfit, colors, hairstyle. Generate a character card per main character first and attach it as a reference when generating their shots.
7. **Era-correct** clothes, props, furniture, cars for the year of the shot; no phones or plastic in the past.
8. **YouTube-safe:** no nudity; bathroom/shaving scenes only by hint (robe, foam, razor).
9. **Emotion matches the VO line.**
10. **Continuity:** same character side, background and wall color between consecutive shots of one scene.
11. **Real people** (historical figures, celebrities) in channel style, recognisable by one detail, no photo-portrait attempts.
12. **No stray logos or random text.**
- QA: after generating, build a contact sheet of all frames, check each against this list, regenerate defects before showing the user.

## 4. Characters (read `_персонажи\character_bible.txt`)
- Big round white head, two equal fairly large round eyes with dot pupils, tiny one-line nose, ONE small unbroken mouth fully inside the face, real clothed body (not stick figure), round hands.
- Women: same + 3 tiny eyelashes; 10 numbered hairstyles in mtw_woman_hairstyles.jpg.
- Use cream/ivory + colored accents instead of all-white outfits (Kellogg: cream suit, butter-yellow vest, amber bow tie, gray hair) and a contrasting wall.

## 5. Frames in Google Flow (flow.google.com, built-in browser)
- Image: Nano Banana 2.1, 16:9, x2 (0 credits). Turn OFF "Агент".
- Insert prompt via execCommand('insertText') into the contenteditable; start with a REAL click on the arrow. Space submissions ~8 s apart.
- Tile order ≠ creation order. The grid is virtualized: scroll and collect `img[alt^=Карточка]` srcs, then show an overlay contact sheet built with createElement (innerHTML is blocked by TrustedHTML).
- Full-res: replace `=s1600-rw` with `=d`.
- Animation: Video → Кадры, Omni 1.1 Flash, 720p; 6 s = 10 credits, 8 s = 12. Pick the first frame via the "Первый" picker (has a search box). Blocked generations are refunded.
- Credits: avatar → "N бонусов Google Flow" (one.google.com/ai/activity).

## 6. Voiceover (ElevenLabs, paid ~120k chars/month)
- Voice **Jack John – Conversational and Upbeat**, Eleven v4, stability 50%, similarity 75%, speed 1.0.
- **Language = English ("Angielski") — NEVER Auto.** Auto once voiced a sentence of a short in Polish.
- One chapter per file. The editor generates only the FIRST paragraph block — put text on ONE line. One file per short is safest (joining all shorts with ` [long pause] ` and splitting by silences also works).

## 7. Assembly (container, ffmpeg + Python)
- 1920×1080, 25 fps. Stills via **smoothzoom.py** (never zoompan — it jitters).
- ep3_timing.py: per chapter, silencedetect (-38 dB, 0.18 s) + DP assigning shot boundaries to silences matching char-proportional durations; chapters joined with 0.6 s gaps → timing.json + vo.mp3.
- ep3_render.py: anims scaled + padded, MPEG-TS concat, one encode libx264 crf 27 -tune animation preset slow, AAC 192k → ~26 MB / 5 min, ~56 MB / 9.5 min. Container has 2 CPUs: a 144-shot render takes 30–40 min. Verify decode with `ffmpeg -v error -f null -`. SRT from timing.json.

## 8. Shorts (ep3_shorts.py)
- 1080×1920 dark bg, 2-line hook title (white + yellow, Inter Display Black), 16:9 clip at y=560, yellow captions, footer MADE TO WANT. 25–35 s, own VO (English!), each sentence mapped to a shot, fact-first hook, ends on the MADE TO WANT end card. ~6–7 per video.

## 9. Publishing
### Upload without the user (no OS file dialog)
- Use **Claude in Chrome** (the user's Chrome is logged into the channel). `file_upload` accepts only files from the working directory (e.g. /home/claude/up/), max 10 MB per call.
- Shorts/thumbnail: Создать → Добавить видео → `find` the dialog's file input → `file_upload` (or helper `<input type=file>` elements).
- Big video: `split -b 9000000` in /home/claude, upload parts into helper inputs, in JS `new Blob([p0,p1,p2])` → `new File(...,'Title.mp4',{type:'video/mp4'})`, compare SHA-256 with the container, open the dialog (`#upload-icon`), put the File into `ytcp-uploads-dialog input[name=Filedata]` via DataTransfer + dispatch `change`.
- Thumbnail: `find` the file input in the "Значок" section, `file_upload` the jpg.
### Fields
- Long video: title, description (hook, summary, chapters, previous episode link, tagline, #history #marketing #psychology), tags (real typing, comma-separated), Образование, `VIDEO_MADE_FOR_KIDS_NOT_MFK`, `VIDEO_HAS_ALTERED_CONTENT_NO`, "Нет, в видео нет прямой рекламы", thumbnail, `#step-badge-3` → PUBLIC or schedule (as the user says) → `#done-button`; confirm the "Проверка видео ещё продолжается" popup.
- Shorts: title = hook + " #shorts"; description = hook line + "Full story: <link>" + tagline + hashtags; same flags; one per day **at 13:00 Warsaw**. Date: `#second-container-expand-button` → date dropdown → pick the day in the calendar; time: click the time field, ctrl+a, type "13:00", Enter, verify by zoom (sometimes needs a retry); done → ОК.
- Set "Видео по теме" on each short (works even while the long video is still scheduled): edit page → "Видео по теме" dropdown → the video's `ytcp-entity-card` → `ytcp-button#save`.
- Retiring an old video: edit page → Параметры доступа → **explicitly click the "Ограниченный доступ" radio** → ОК → Сохранить, then re-check the list (one careless click once made an old short public). Never delete — the user deletes.
- Thumbnail: generate in Flow (characters on the right, empty plain left half), add a 2–3 line claim in Inter Display Black on the left.
- TikTok (TikTok Studio web, one video per upload): only when the user says so; caption with hashtags incl. #learnontiktok, ~20:00; scheduling needs the user's consent to TikTok's storage prompt — ask first. The Draft.js caption box duplicates text with execCommand; check and fix.

## Rules
- Never create accounts, enter passwords, or permanently delete — ask the user.
- Ask before accepting terms/consent dialogs.
- The user works shifts and is often away or asleep — make reasonable decisions yourself and report at the end in a short table with links.
- If the computer isn't linked to the chat, do everything that doesn't need it (script, storyboard, prompts) and leave generation for when it is.