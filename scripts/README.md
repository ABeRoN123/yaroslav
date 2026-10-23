# Scripts (Python 3 + ffmpeg + OpenCV + Pillow). Run from an episode work folder with:
k/kadr_NNN.jpg (frames), anim/anim_NNN.mp4 (animations), vo/*.mp3 (chapter VO in order), sb.json (= storyboard.json).

- storyboard/build.py — builds storyboard.json / char_cards.json / vo_chapters.txt from scene list + character cards + STYLE/CROWD rules (ep05 version, edit the SHOTS/CARDS for a new episode).
- long/ep5_timing.py — silencedetect + DP maps shots onto VO → timing.json + vo.mp3 (chapter list taken from storyboard order; files = sorted vo/). Pad vo.mp3 ~2.5 s so the end card holds.
- long/overlay.py — writes title / chapter-card / end-card / ad text onto frames (k/ → kt/). Run BEFORE render.
- long/ep5_render.py — smoothzoom stills + scaled anims → MPEG-TS concat → final.mp4 (1920×1080, 25 fps, crf 27). Set `anims` to the animated shot numbers. ~12 min for 120 shots on 2 CPUs.
- long/smoothzoom.py — jitter-free Ken Burns (never use ffmpeg zoompan).
- shorts/ep5_shorts.py + videos/05-color/shorts/shorts_def.py — newest: one VO file per short (vo/shortK.mp3), builds all shorts.
- shorts/build_shorts.py + ep4_shorts_def.py — ep4 variant (`python build_shorts.py K`, VO sh/sK_vo.mp3).
- Verify output: `ffmpeg -v error -i final.mp4 -f null -` and a contact sheet (`fps=1/10,scale=320:-1,tile=8x5`).
