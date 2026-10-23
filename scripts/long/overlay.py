from PIL import Image,ImageDraw,ImageFont
FB='/usr/share/fonts/opentype/inter/InterDisplay-Black.otf'
FX='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
INK=(43,50,56);AMB=(201,125,40);WH=(255,255,255)
def fit(d,txt,font,maxw,sz):
    while True:
        f=ImageFont.truetype(font,sz)
        if d.textlength(txt,font=f)<=maxw or sz<12: return f
        sz-=2
def block(n,lines,box,align='c',colors=None):
    im=Image.open(f'k_orig/kadr_{n}.jpg').convert('RGB');W,H=im.size
    x0,y0,x1,y1=[int(v*s) for v,s in zip(box,(W,H,W,H))]
    d=ImageDraw.Draw(im);bw=x1-x0;bh=y1-y0;fonts=[];hs=[]
    for t,font,szf in lines:
        f=fit(d,t,font,bw,int(bh*szf));fonts.append(f);bb=d.textbbox((0,0),t,font=f);hs.append(bb[3]-bb[1])
    gap=int(bh*0.06);tot=sum(hs)+gap*(len(hs)-1);y=y0+(bh-tot)//2
    for i,(t,font,szf) in enumerate(lines):
        f=fonts[i];bb=d.textbbox((0,0),t,font=f);w=bb[2]-bb[0]
        x=x0+(bw-w)//2 if align=='c' else x0
        d.text((x-bb[0],y-bb[1]),t,font=f,fill=(colors[i] if colors else INK));y+=hs[i]+gap
    im.save(f'k/kadr_{n}.jpg',quality=95)
block('010',[('THE HAIR',FB,.4),('YOU WERE TOLD TO SHAVE',FB,.4)],(0.1,0.1,0.9,0.45),'c',[INK,AMB])
block('011',[('CHAPTER ONE',FX,.16),('A PROBLEM',FB,.32),('NOBODY COULD SEE',FB,.32)],(0.5,0.12,0.96,0.52),'l',[WH,INK,INK])
block('028',[('CHAPTER TWO',FX,.18),('THE RAISED ARM',FB,.38)],(0.06,0.32,0.56,0.62),'l',[WH,INK])
block('058',[('CHAPTER THREE',FX,.16),('A FACE WITH',FB,.32),('NO BEARD',FB,.32)],(0.06,0.28,0.56,0.7),'l',[(240,214,140),WH,WH])
block('070',[('CHAPTER FOUR',FX,.16),('THE DANGEROUS',FB,.32),('DECADE',FB,.32)],(0.47,0.3,0.95,0.68),'l',[WH,INK,INK])
block('099',[('CHAPTER FIVE',FX,.2),('THE LEGS',FB,.46)],(0.06,0.2,0.6,0.5),'l',[AMB,INK])
block('123',[('CHAPTER SIX',FX,.16),('WHY IT',FB,.32),('STILL WORKS',FB,.32)],(0.06,0.28,0.6,0.7),'l',[WH,INK,INK])
block('144',[('MADE TO WANT',FB,.5),('who decided what you want?',FX,.22)],(0.1,0.3,0.72,0.62),'c',[INK,AMB])
block('037',[('SUMMER DRESS AND',FB,.22),('MODERN DANCING COMBINE',FB,.22),('TO MAKE NECESSARY THE',FB,.22),('REMOVAL OF OBJECTIONABLE HAIR',FB,.22)],(0.255,0.355,0.745,0.585),'c',[(110,60,40)]*4)
