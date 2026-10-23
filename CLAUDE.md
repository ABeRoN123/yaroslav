# Made to Want — CLAUDE.md
Keep this file short: it is loaded on every turn. Details live in docs/ and are read only when needed.

## Talk
- Reply to the owner (Yaroslav) in **Russian**, short. Everything for AIs (prompts, scripts, VO, titles, descriptions) in **English**.
- He is often away: decide reasonable things yourself, report at the end in a short table with links. Ask only before publishing, deleting, or spending many credits.
- Never delete videos/files, never create accounts or enter passwords. Retire videos as "Ограниченный доступ".

## Channel
Made to Want — doodle video essays on how marketing invented our desires. Title "The ___ You Were Told to ___". Long 5–10 min (never >10), 5–6 Shorts per video (25–35 s), about 1 Short/day; publish time is NOT fixed: the owner names it right before scheduling (ask, never assume or save it). Channel: https://www.youtube.com/channel/UCC972vQMbqKBQLeccmoYBOg

## Where things are
- Rules + lessons: docs/rules.md · full pipeline: docs/pipeline_full.md (also the skill `made-to-want-video`)
- Plan/published log: calendar/content-plan.md · ideas: ideas/backlog.md · style: channel/style-guide.md
- One folder per episode: videos/NN-slug/ (story.md, script.md, storyboard.json, status.md, youtube_description.txt, shorts/)
- Scripts: scripts/ (see scripts/README.md). Media stays on his PC in `D:\клод ютуб\NN Title\`, not in git.

## Fixed settings
- Google Flow: Nano Banana 2.1, 16:9, **x1**; video Omni 1.1 Flash, 720p, **6 s**, x1.
- ElevenLabs: Jack John – Conversational and Upbeat, Eleven v4, stability 50, similarity 75, **language English (never Auto)**, text on one line.
- Overlay title/chapter/end-card text BEFORE render; chapter cards ≥2.5 s.

## End of every session
Update videos/NN-slug/status.md (what's done, links, TODO) and calendar/content-plan.md, then commit.

## Reply format (markers + model hint)
Start lines that matter with a colored marker. The owner skims on his phone, so the color tells him where to look:
- 🔴 needs HIS decision or is risky: publishing, deleting, paying or spending many credits, something broke
- 🟡 check with your eyes: frames, timing, shaky facts, anything I'm not sure about
- 🟢 done and verified
- 🔵 info, can be skipped
- 🟣 new: first time we do this (new tool, new trick, new format)
- 💰 cost: tokens, Flow or ElevenLabs credits spent or about to be spent
- 💡 tip: model or economy advice
Use at most one marker per line and don't color everything. Most replies need only 2–5 markers.

When a new task starts (or the task type changes), the first line is a model hint, e.g.
`💡 Модель: Sonnet 5.5 · средний — рутина в браузере`. Pick from docs/economy.md → "Which model". If the current model is fine, write `💡 Модель ок`.
If the session is getting long (many screenshots, >~30 messages, or the task is done), end with
`💡 Пора /compact или новая сессия` and make sure status.md is updated first.

## Connector checklist (before each task)
Right after the model hint, show a small table of connectors for THIS task so the owner can tick them in settings. Take it from docs/economy.md → "Which connectors". Format:

| Коннектор | Сейчас |
|---|---|
| Claude in Chrome | ✅ включить |
| vidIQ | ⛔ выключить |

List only connectors whose state should CHANGE compared to the previous task. If nothing changes, write `🔌 Коннекторы: без изменений`. If a needed connector is missing or not authorized, say so with 🔴.

## Suggest new connectors, skills, GitHub repos (owner decides)
On a real need (repeated manual work, new stage or platform, milestone) suggest a tool, marked 🟣. Check at most once per episode (at the end) or when the owner asks "что нового?". Max 3 rows:

| Что | Тип | Зачем нам | Цена/риск | Ссылка |
|---|---|---|---|---|

Never install, connect or clone anything without his "да". Vet repos/skills first and log every suggestion and answer in docs/tools-wishlist.md (don't re-suggest declined ones). Checklist: docs/economy.md → "Growing the toolset".
