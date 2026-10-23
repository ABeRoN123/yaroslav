
## Update 2026-10-21 — RE-RELEASED (v2)
User watched the 21 Oct release and DELETED Wkm7vsQ9tmI because of:
1. Chapter cards had no on-screen titles (ep3 had an overlay step — overlay.py — that was missed in ep4).
2. Chapter five card flashed for ~1 s (timing DP put the boundary inside "Chapter five. | The legs.").
3. Anim 80 (US map with cabinets): the wave is great, but at ~4 s a burst/explosion of cabinets from the middle — unwanted.
4. Some characters slightly off-canon (user: acceptable).

Fixes (container /home/claude/ep4):
- overlay.py (Inter Display Black / Inter ExtraBold) writes text onto k/kadr_NNN.jpg from k_orig/: 10 title "THE HAIR / YOU WERE TOLD TO SHAVE", chapter cards 11, 28, 58, 70, 99, 123 ("CHAPTER N" + title), 37 ad banner text (the 1915 ad quote), 144 "MADE TO WANT / who decided what you want?".
- timing.json: shot 100 start 387.05, shot 101 start 389.57 (chapter 5 card now ~2.6 s).
- anim_080: first 4.0 s of the original only, slowed ×1.27 → 5.08 s (no burst). Original kept as k_orig/anim_080_orig.mp4.
- New final.mp4 9:30, sha256 de4cde20…

Published v2: https://youtu.be/k6960-UIr5s — PUBLIC 21 Oct 2026 ~19:45, same title/description/chapters/thumbnail, tags.
PC: video_part_00..02 replaced with v2 (run join_video.bat); анимации\anim_080.mp4 replaced; кадры\с текстом\ has the 9 frames with text.

## Ep3 shorts — duplicates
The old ep3 shorts (Auto-language VO) were made PUBLIC again by the time the user checked, and got 800–1300 views each. So the new English copies were set to Ограниченный (private): Kwsfi9t6mi4, 35L8ep5qbQU, ml72NPk9XgU, z6k-qo50sRE, NtMZTl7tJ5Q. Public ep3 shorts now: AT2WSgRF9ng (new bacon&eggs), a7kPA4GpS-Y, --zoG_6fPJ0, DqjE_WwsMoQ, z3f6sQlkHuo, _Yqg89rAdvs.

## Ep4 shorts (DONE 2026-10-21)
Scripts: container /home/claude/ep4/sh/shorts_def.py (also on PC озвучка\ as VO short1..5_vo_en.mp3, videos in shorts\). VO English (Angielski), Jack John, v4.
Shorts slot is now **16:00 Warsaw** (user: other batches sit at 17:00 and 18:00).
| # | Title | ID | When |
|---|---|---|---|
| 1 | Shaving armpits started with a 1915 ad | nDkS8uqFz5k | public 21 Oct ~20:10 |
| 2 | The first women's razor was a men's razor | B-WtYptObvo | 22 Oct 16:00 |
| 3 | In the 1920s, women removed hair with X-rays | 5l0ILdRCFN4 | 23 Oct 16:00 |
| 4 | A 1930s hair removal cream made with rat poison | WM2UaqXGRgA | 24 Oct 16:00 |
| 5 | Leg shaving went mainstream because of a war | azR_9uSUe9c | 25 Oct 16:00 |
All five: "Видео по теме" = The Hair You Were Told to Shave (k6960-UIr5s); description links Full story.

## TODO
1. Lesson for every video: run the text-overlay step (chapter titles, title card, end card, long ad text) before rendering, and check every chapter card lasts ≥2.5 s.
# EP04 — The Hair You Were Told to Shave — PUBLISHED (v2)
- Video: https://youtu.be/k6960-UIr5s (public 21 Oct 2026 ~19:45). v1 Wkm7vsQ9tmI was deleted by the user: chapter cards had no on-screen titles, chapter-5 card flashed ~1 s, anim 80 had an unwanted burst.
- 144 shots, 17 animations, 9 character cards, 8 VO chapters (~9:30). Thumbnail "SHAVING WAS AN AD.".
- Flow project: https://flow.google.com/project/e14fac1d-f283-4f01-af57-037232871137 · storyboard review: https://claude.ai/artifact/SormBdE1wiXJzfjjo2aJod
- Fixes in v2: overlay.py text on frames 10 (title), 11/28/58/70/99/123 (chapter cards), 37 (1915 ad quote), 144 (end card); chapter-5 card ≥2.5 s; anim_080 trimmed to first 4 s and slowed ×1.27.
- Shorts (16:00 Warsaw, "Видео по теме" = k6960-UIr5s): nDkS8uqFz5k (21 Oct), B-WtYptObvo (22), 5l0ILdRCFN4 (23), WM2UaqXGRgA (24), azR_9uSUe9c (25).
- Flow notes: animation of a frame with bare disembodied legs was blocked as "sexual" → frame replaced with a clothed woman shaving her lower leg; naming King Gillette triggered "famous people" block → "the man".
- PC: D:\клод ютуб\04 The Hair You Were Told to Shave\ (video_part_00..02 + join_video.bat, кадры\, кадры\с текстом\, анимации\, озвучка\, shorts\).
