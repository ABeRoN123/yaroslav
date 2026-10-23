import json,subprocess,re
SB=json.load(open('sb.json'))['shots']
CH=['Hook','Title','Everyone in white','Pink is for boys','Nobody agreed','The rule arrives','The pause','The sonogram sale','Pink everything','Why it still works','Ending']
chmap={c:i for i,c in enumerate(CH)}
import os
files=sorted(f[:-4] for f in os.listdir('vo'))
GAP=0.6
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]))
def sil(f):
    o=subprocess.run(['ffmpeg','-i',f,'-af','silencedetect=n=-38dB:d=0.18','-f','null','-'],capture_output=True,text=True).stderr
    s=[float(x) for x in re.findall(r'silence_start: ([\d.]+)',o)];e=[float(x) for x in re.findall(r'silence_end: ([\d.]+)',o)]
    return list(zip(s,e))
T=[];off=0;audio=[]
for ci,fn in enumerate(files):
    f=f'vo/{fn}.mp3';D=dur(f);S=sil(f)
    # trim leading silence
    lead=S[0][1] if S and S[0][0]<0.05 else 0
    sh=[x for x in SB if chmap[x['chapter']]==ci]
    L=[len(x['vo']) for x in sh];tot=sum(L)
    speech=[(a,b) for a,b in zip([lead]+[e for s,e in S],[s for s,e in S]+[D]) if b>a]
    sp_tot=sum(b-a for a,b in speech)
    def ch2t(frac):
        tgt=frac*sp_tot;acc=0
        for a,b in speech:
            if acc+(b-a)>=tgt: return a+(tgt-acc)
            acc+=b-a
        return D
    mids=[((s+e)/2,e-s) for s,e in S if s>0.05 and e<D-0.05]
    K=len(sh); rate=(D-lead)/tot; exp=[l*rate for l in L]
    import math
    # DP over candidate boundaries
    C=[lead]+[m for m,_ in mids]+[D]; W=[0]+[w for _,w in mids]+[0]
    N=len(C); INF=1e18
    dp=[[INF]*N for _ in range(K+1)]; bp=[[0]*N for _ in range(K+1)]
    dp[0][0]=0
    for k in range(1,K+1):
        for j in range(1,N):
            if k<K and j==N-1: continue
            if k==K and j!=N-1: continue
            for i in range(j):
                if dp[k-1][i]>=INF: continue
                d=C[j]-C[i]; e=exp[k-1]
                c=((d-e)/max(e,1.0))**2 - (0.3*W[j] if j<N-1 else 0)
                if d<0.7: c+=50
                v=dp[k-1][i]+c
                if v<dp[k][j]: dp[k][j]=v; bp[k][j]=i
    idx=[N-1]
    for k in range(K,0,-1): idx.append(bp[k][idx[-1]])
    idx=idx[::-1]; bounds=[C[i] for i in idx[:-1]]
    for i,x in enumerate(sh):
        s0=bounds[i];s1=bounds[i+1] if i+1<len(sh) else D
        T.append({'n':x['n'],'start':off+s0-(lead if i==0 else 0),'s0':off+s0,'s1':off+s1,'text':x['vo']})
    audio.append((f,lead,D)); off+=(D-lead)+GAP
# make start of first shot of each chapter = chapter start; ensure contiguous
for i in range(1,len(T)): pass
json.dump(T,open('timing.json','w'),indent=0)
# build vo track
inputs=[];fc='';k=0
for f,lead,D in audio:
    inputs+=['-i',f];fc+=f'[{k}:a]atrim=start={lead:.3f},asetpts=PTS-STARTPTS,apad=pad_dur={GAP}[a{k}];';k+=1
fc+=''.join(f'[a{i}]' for i in range(k))+f'concat=n={k}:v=0:a=1[o]'
subprocess.run(['ffmpeg','-v','error','-y',*inputs,'-filter_complex',fc,'-map','[o]','-ar','44100','-b:a','192k','vo.mp3'],check=True)
print('total',off, len(T))
for x in T: print(x['n'],round(x['start'],2),round(x['s1']-x['s0'],2),x['text'][:50])
