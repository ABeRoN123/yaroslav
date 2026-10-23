import json,subprocess,re,os,smoothzoom
from PIL import Image,ImageDraw,ImageFont
FT='/usr/share/fonts/opentype/inter/InterDisplay-Black.otf'
import sys
K=int(sys.argv[1]); A=f'sh/s{K}_vo.mp3'; FR=25
o=subprocess.run(['ffmpeg','-i',A,'-af','silencedetect=n=-40dB:d=0.5','-f','null','-'],capture_output=True,text=True).stderr
S=list(zip(map(float,re.findall(r'silence_start: ([\d.]+)',o)),map(float,re.findall(r'silence_end: ([\d.]+)',o))))
big=sorted([x for x in S if x[1]-x[0]>1.5])
TOT=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',A]))
spans=[];st=0
for a,b in big: spans.append((st,a));st=b
spans.append((st,TOT)); spans=[(0,TOT)]
anims={1,7,18,32,35,41,62,69,73,80,90,105,112,120,130,133,141}
exec(open('sh/shorts_def.py').read())
o2=subprocess.run(['ffmpeg','-i',A,'-af','silencedetect=n=-38dB:d=0.18','-f','null','-'],capture_output=True,text=True).stderr
S2=list(zip(map(float,re.findall(r'silence_start: ([\d.]+)',o2)),map(float,re.findall(r'silence_end: ([\d.]+)',o2))))
def sil(a,b):
    return [((s+e)/2,e-s) for s,e in S2 if s>a+0.05 and e<b-0.05]
def ts(t): return f"0:{int(t//60):02d}:{t%60:05.2f}"
os.makedirs('sh/shorts',exist_ok=True)
SH=SH[K-1:K]
for k,((a,b),(title,slug,segs)) in enumerate(zip(spans,SH),K):
    a=max(0,a-0.05); b=b+0.1; D=b-a
    L=[len(t) for t,_ in segs]; rate=D/sum(L); exp=[l*rate for l in L]; K=len(segs)
    C=[a]+[m for m,_ in sil(a,b)]+[b]; W=[0]+[w for _,w in sil(a,b)]+[0]; N=len(C); INF=1e18
    dp=[[INF]*N for _ in range(K+1)]; bp=[[0]*N for _ in range(K+1)]; dp[0][0]=0
    for kk in range(1,K+1):
        for j in range(1,N):
            if (kk<K)==(j==N-1): continue
            for i in range(j):
                if dp[kk-1][i]>=INF: continue
                d=C[j]-C[i]; e=exp[kk-1]; c=((d-e)/max(e,1))**2-(0.3*W[j] if j<N-1 else 0)+(50 if d<0.6 else 0)
                if dp[kk-1][i]+c<dp[kk][j]: dp[kk][j]=dp[kk-1][i]+c; bp[kk][j]=i
    idx=[N-1]
    for kk in range(K,0,-1): idx.append(bp[kk][idx[-1]])
    bounds=[C[i]-a for i in idx[::-1]]
    # visual segments
    tsl=[]
    fb=[round(x*FR) for x in bounds]; fb[-1]=round(D*FR)
    for i,(t,n) in enumerate(segs):
        F=fb[i+1]-fb[i]; out=f'sh/shorts/k{k}_{i:02d}.mp4'
        if n in anims:
            vf=f"fps={FR},scale=1920:1080,setsar=1,tpad=stop_mode=clone:stop_duration=60,trim=end_frame={F}"
            subprocess.run(['ffmpeg','-v','error','-y','-i',f'anim/anim_{n:03d}.mp4','-vf',vf,'-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-r',str(FR),out],check=True)
        else:
            src=f'kt/kadr_{n:03d}.jpg' if os.path.exists(f'kt/kadr_{n:03d}.jpg') else f'k/kadr_{n:03d}.jpg'
            smoothzoom.render(src,out,F,z=0.06,fps=FR,crf=18)
        subprocess.run(['ffmpeg','-v','error','-y','-i',out,'-c','copy','-bsf:v','h264_mp4toannexb','-f','mpegts',out+'.ts'],check=True)
        tsl.append(out+'.ts')
    # background + title
    bg=Image.new('RGB',(1080,1920),(31,38,43));d=ImageDraw.Draw(bg);y=250
    for i,line in enumerate(title.split('|')):
        sz=92
        while True:
            f=ImageFont.truetype(FT,sz);w=d.textlength(line,font=f)
            if w<=960: break
            sz-=2
        d.text(((1080-w)/2,y),line,font=f,fill=(255,255,255) if i==0 else (255,214,92));y+=sz+18
    ff=ImageFont.truetype(FT,44);w=d.textlength('MADE TO WANT',font=ff);d.text(((1080-w)/2,1760),'MADE TO WANT',font=ff,fill=(170,180,186))
    bg.save(f'sh/shorts/bg{k}.png')
    ass="""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Inter ExtraBold,92,&H005CD6FF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,6,2,8,60,60,1290,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    for i,(t,n) in enumerate(segs):
        words=t.replace('"','').split();ch=[];cur=[]
        for w_ in words:
            cur.append(w_)
            if len(' '.join(cur))>=13 or re.search(r'[.,:;?!]$',w_): ch.append(' '.join(cur));cur=[]
        if cur: ch.append(' '.join(cur))
        t0=bounds[i]+0.05;t1=bounds[i+1]-0.1;Lc=sum(len(c) for c in ch);acc=t0
        for c in ch:
            dd=(t1-t0)*len(c)/Lc;ass+=f"Dialogue: 0,{ts(acc)},{ts(acc+dd)},Cap,,0,0,0,,{c}\n";acc+=dd
    open(f'sh/shorts/c{k}.ass','w').write(ass)
    out=f'sh/shorts/short_{k}_{slug}_ep4.mp4'
    fc=(f"[1:v]scale=1080:608:flags=lanczos,setsar=1[v];[0:v][v]overlay=0:560,ass=sh/shorts/c{k}.ass,format=yuv420p[o];"
        f"[2:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.1,afade=t=out:st={D-0.3:.2f}:d=0.3[aa]")
    subprocess.run(['ffmpeg','-v','error','-y','-loop','1','-framerate','25','-i',f'sh/shorts/bg{k}.png','-i','concat:'+'|'.join(tsl),'-i',A,
        '-filter_complex',fc,'-map','[o]','-map','[aa]','-t',f'{D:.3f}','-c:v','libx264','-preset','medium','-crf','21','-r','25','-c:a','aac','-b:a','160k','-movflags','+faststart',out],check=True)
    print('done',k,round(D,1),out,flush=True)
