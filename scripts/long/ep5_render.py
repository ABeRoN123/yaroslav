import json,subprocess,os,smoothzoom
from concurrent.futures import ThreadPoolExecutor
T=json.load(open('timing.json'));FR=25
total=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0','vo.mp3']))
anims={1,7,8,13,19,29,36,45,57,71,85,94,97,103,119}
starts=[round(x['start']*FR) for x in T]+[round(total*FR)]
os.makedirs('seg',exist_ok=True);os.makedirs('ts',exist_ok=True)
def job(i):
    x=T[i];n=x['n'];D=starts[i+1]-starts[i];out=f'seg/s{n:03d}.mp4'
    if os.path.exists(f'ts/s{n:03d}.ts'): return n
    if n in anims:
        vf=f"fps={FR},scale=1920:1080:flags=lanczos,setsar=1,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={D}"
        if n==8:
            cmd=['ffmpeg','-v','error','-y','-i',f'anim/anim_{n:03d}.mp4','-loop','1','-i','title.png','-filter_complex',f"[0:v]{vf}[b];[1:v]format=rgba,fade=in:st=0.1:d=0.4:alpha=1[t];[b][t]overlay=shortest=1",'-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FR),'-frames:v',str(D),out]
        else:
            cmd=['ffmpeg','-v','error','-y','-i',f'anim/anim_{n:03d}.mp4','-vf',vf,'-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FR),out]
        subprocess.run(cmd,check=True)
    else:
        smoothzoom.render(f'k/kadr_{n:03d}.jpg',out,D,z=0.045 if n%2 else 0.035,fps=FR,crf=18)
    subprocess.run(['ffmpeg','-v','error','-y','-i',out,'-c','copy','-bsf:v','h264_mp4toannexb','-f','mpegts',f'ts/s{n:03d}.ts'],check=True)
    return n
with ThreadPoolExecutor(2) as ex: list(ex.map(job,range(len(T))))
cat='concat:'+'|'.join(f'ts/s{x["n"]:03d}.ts' for x in T)
subprocess.run(['ffmpeg','-v','error','-y','-i',cat,'-i','vo.mp3','-map','0:v','-map','1:a','-c:v','libx264','-preset','slow','-crf','27','-tune','animation','-pix_fmt','yuv420p','-r','25','-c:a','aac','-b:a','192k','-shortest','-movflags','+faststart','final.mp4'],check=True)
print('DONE')
