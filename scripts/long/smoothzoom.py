"""Smooth push-in for still images (no jitter): sub-pixel affine warp per frame (OpenCV), eased, piped to ffmpeg."""
import subprocess, sys, cv2, numpy as np
def ease(t): return t*t*(3-2*t)*0.35 + t*0.65
def render(src, out, frames, z=0.045, fps=25, W=1920, H=1080, crf=19):
    im = cv2.cvtColor(cv2.imread(src), cv2.COLOR_BGR2RGB)
    ih, iw = im.shape[:2]
    ar = W/H
    bw, bh = (ih*ar, ih) if iw/ih > ar else (iw, iw/ar)
    cx, cy = iw/2, ih/2
    p = subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(fps),'-i','-',
                          '-c:v','libx264','-preset','veryfast','-crf',str(crf),'-pix_fmt','yuv420p','-tune','animation',out], stdin=subprocess.PIPE)
    for f in range(frames):
        s = 1 + z*ease(f/max(1,frames-1))
        k = W/(bw/s)                      # source px -> output px
        M = np.float32([[k,0,W/2-k*cx],[0,k,H/2-k*cy]])
        fr = cv2.warpAffine(im, M, (W,H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        p.stdin.write(fr.tobytes())
    p.stdin.close(); p.wait()
if __name__=='__main__':
    render(sys.argv[1], sys.argv[2], int(sys.argv[3]))
