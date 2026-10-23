# EP05 — The Color You Were Told to Wear — PUBLISHED 2026-10-22

**https://youtu.be/9eICiQ8ptWE**: 6:48 long, 11 chapters, 120 shots, 15 animations, 12 character cards.

## Production notes
- Flow project: https://flow.google.com/project/35d646dd-a4f8-4100-a019-630f96c0ed96, made with Nano Banana 2.1 at x1.
- Character cards are renamed in Flow as "REF <key> <name>" so the ingredient picker search finds them.
- VO: 11 files, English, Jack John v4.
- Chapters:
  - 0:00 The 1918 rule
  - 0:27 Everyone in white
  - 1:22 Pink is for boys
  - 2:08 Nobody agreed
  - 2:54 The rule arrives
  - 3:37 The pause
  - 4:07 The sonogram sale
  - 4:49 Pink everything
  - 5:38 Why it still works
  - 6:22 Ending
- Thumbnail: "PINK WAS FOR BOYS. IN 1918."
- PC folder: D:\клод ютуб\05 The Color You Were Told to Wear\

## Shorts (13:00 Warsaw; "Видео по теме" = 9eICiQ8ptWE)
| # | Title | ID | When |
|---|---|---|---|
| 1 | In 1918, pink was for boys | 7GWzG_GI9iY | 23 Oct |
| 2 | Little boys used to wear white dresses | 1PnoK6xzzBU | 24 Oct |
| 3 | Stores couldn't agree on pink or blue | HID3p8b545E | 25 Oct |
| 4 | Prenatal tests made baby clothes pink and blue | a8_Rf0JFMN0 | 26 Oct |
| 5 | The pink tax is real | io7W8RhtfW0 | 27 Oct |
| 6 | Gender reveal parties started in 2008 | yDJbnoffRzQ | 28 Oct |

TODO: add an end screen on the long video.

## Lessons from this episode
- People without a character card need the people/style sentence in the prompt (PEOPLE_EXTRA in build.py), otherwise Nano Banana draws realistic small faces.
- The prompt line "Every face has two perfectly round eyes of exactly the same size, both looking in the same direction" plus "no other people" fixes eye defects.
- Flow grid order is not reliable after a batch, so map new tiles to shots by their auto titles. The grid is virtualized: search by setting the 2nd input via the native value setter plus an input event.
- Animate a frame via the tile menu "Дополнительные параметры" → "Анимировать". For wide shots add "Locked-off static shot, the camera does not move, zoom or cut".
- Video duration resets to 8 s after a reload, so set 6 s again.
- The ElevenLabs UI language may be English or Polish. The download button is labelled "Download" or "Pobierz", and the first one is the newest.
- Flow downloads sometimes sit in Downloads as GUID .tmp files for a while before they get renamed.
- The built-in browser has no file upload, so YouTube uploads need Claude in Chrome.
