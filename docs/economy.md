# Economy guide: which model, how to save tokens (read when choosing a model)

## Which model
| Task | Model · effort | Why |
|---|---|---|
| Topic choice, fact check, script, storyboard, thumbnail claim, hard bug | **Opus 5.5 · средний** (высокий only for the script/storyboard of a new episode) | quality matters, it decides the whole video |
| QA of frames/animations against the checklist | Opus 5.5 · средний | needs a careful eye |
| Browser routine: Flow generation, ElevenLabs, downloads, YouTube upload & scheduling, "Видео по теме" | **Sonnet 5.5 · средний** | many steps, simple decisions, lots of screenshots → Opus would be expensive |
| Render, shorts build, running scripts, file moves, zips | Sonnet 5.5 · низкий/средний | mechanical |
| Status/plan updates, renaming, small text edits, short questions | **Haiku 5.5** | trivial |
Rule of thumb: thinking/creative → Opus; doing/clicking → Sonnet; tiny → Haiku. Only raise effort when the result was weak.

## Which connectors (MCP) per task
Every enabled connector costs tokens on every message. Enable only what the current task needs.
| Task | ✅ Needed | ⛔ Turn off |
|---|---|---|
| Topic, fact check, script, storyboard | none (built-in web search is enough) | Chrome, built-in browser, PC link, vidIQ, Docs |
| Competitors, keywords, title/thumbnail ideas, channel analytics | vidIQ | Chrome, built-in browser, Docs |
| Flow frames / animations, ElevenLabs VO | browser (Claude in Chrome or built-in browser), PC link (to save files to D:\клод ютуб) | vidIQ, Docs |
| Render, shorts build, zips, moving files | PC link | browsers, vidIQ, Docs |
| YouTube upload, scheduling, "Видео по теме", end screens | Claude in Chrome (file upload works only there), PC link | built-in browser, vidIQ, Docs |
| Docs to keep/share (plans, reports) | Claude Docs | browsers, vidIQ |
| Status/plan updates in the repo | none | everything |
GitHub (the repo) stays connected always. "PC link" = the session is linked to his computer through the Claude desktop app.

## How to save tokens
1. One task = one session. Finish → update videos/NN/status.md → commit → close. A new session reads CLAUDE.md + status.md and continues.
2. Every message re-reads the whole chat, so long chats get more expensive with each message. Use /compact or start fresh.
3. Turn off MCP connectors you don't need right now (vidIQ, Docs, …); enable them only for that task. Each connector costs tokens on EVERY message.
4. Give concrete orders, not discussions: "Make 6 shorts for 06 from story.md" instead of 10 back-and-forth messages.
5. Don't paste big files or logs into the chat; let Claude read the file and reply with the conclusion.
6. Screenshots are the most expensive thing. Prefer DOM/text checks; take a screenshot only to verify something visual.
7. Browser stages (Flow, ElevenLabs, YouTube): do them as short separate sessions, one stage each.
8. Keep CLAUDE.md short; long instructions live in docs/ and skills (loaded only when needed).

## Growing the toolset (connectors, skills, GitHub repos)
When to look (cheap triggers, not every task):
- the same manual step was done 3+ times (e.g. downloads from Flow, scheduling shorts) → look for a skill/script/connector that automates it;
- a new stage or platform starts (TikTok/Instagram posting, end screens, analytics reports, music, subtitles in other languages);
- a milestone: monetization, 1k subs, a second channel (castles, Samosbor), team help;
- the owner asks "что нового?" / "что подключить?".
Where to look: the connector directory in claude.ai settings, the org/Anthropic skill catalog, GitHub (search "claude skill <topic>", "mcp server <service>").
Ideas worth checking as the channel grows: YouTube Data/Analytics API connector (stats without screenshots), TikTok/Instagram posting, a subtitles/translation skill (Spanish/Portuguese versions of shorts), a thumbnail A/B helper, an ffmpeg/video-editing MCP, a music/SFX library.
Safety checklist before suggesting: active repo (commits in the last months), real users (stars/issues), clear license, read SKILL.md / main code; no secrets requested, no unknown network calls. Prefer official connectors over random repos.
Format of the suggestion: 🟣 + the table from CLAUDE.md, max 3 rows, then wait for "да/нет". Log it in docs/tools-wishlist.md:
| Дата | Что | Тип | Решение | Заметка |
