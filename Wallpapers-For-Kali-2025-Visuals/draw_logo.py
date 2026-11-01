#!/usr/bin/env python3
"""Wallpapers logo: low hooded prompter's box on a stage apron at knee height, curved
hood open toward viewer, prompt book inside on a sloped ledge with one page corner
lifted, pencil stub and folded spectacles beside it, footlights throwing warm light
up onto the hood underside, sky blue strip behind. Wordmark under the box in
Arizonia, cream on scarlet."""
import sys
from PIL import Image, ImageDraw, ImageFont
import numpy as np
W=H=1024
v=sys.argv[1] if len(sys.argv)>1 else "ship"
SCARLET=(142,26,34); CREAM=(244,234,208); STRAW=(206,178,120); SKY=(126,168,208); AMBER=(255,196,110)
img=Image.new("RGB",(W,H),(24,16,18)); d=ImageDraw.Draw(img,"RGBA")
d.rectangle([0,120,W,300],fill=SKY)
d.rectangle([0,300,W,1024],fill=(30,20,20))
d.rectangle([0,690,W,760],fill=(96,72,44))  # apron boards
# footlights first (behind box glow handled by order: draw dots after box too)
bx,by=512,470
d.pieslice([bx-330,by-300,bx+330,by+120],180,360,fill=(74,14,20))
d.pieslice([bx-330,by-300,bx+330,by+120],180,360,outline=(196,84,66),width=8)
# warm light on hood underside
d.pieslice([bx-280,by-240,bx+280,by+100],180,360,fill=(110,30,26))
d.rectangle([bx-330,by-60,bx+330,by+220],fill=(52,10,16))
# book on sloped ledge
d.polygon([(bx-170,by+150),(bx-8,by+118),(bx-8,by+8),(bx-170,by+44)],fill=CREAM)
d.polygon([(bx+150,by+150),(bx+8,by+118),(bx+8,by+8),(bx+150,by+44)],fill=(238,226,196))
# lifted page corner on right page
d.polygon([(bx+150,by+44),(bx+118,by+16),(bx+150,by+96)],fill=(252,246,226))
for gy in range(30,110,20):
    d.line([(bx-150,by+gy+16),(bx-26,by+gy-2)],fill=(188,182,168),width=5)
# pencil stub and folded spectacles on ledge
d.line([(bx+176,by+128),(bx+238,by+104)],fill=STRAW,width=10)
d.ellipse([bx-268,by+96,bx-208,by+140],outline=STRAW,width=6); d.ellipse([bx-200,by+96,bx-140,by+140],outline=STRAW,width=6); d.line([(bx-208,by+110),(bx-200,by+110)],fill=STRAW,width=5)
d.rectangle([bx-360,by+196,bx+360,by+220],fill=(30,6,10))
for x in (bx-430,bx+430-0,):
    pass
for fx in (92,932):
    d.ellipse([fx-20,706,fx+20,746],fill=AMBER); d.arc([fx-26,694,fx+26,748],180,360,fill=STRAW,width=5)
# wordmark plate
d.rectangle([42,806,982,950],fill=SCARLET)
f=ImageFont.truetype("fonts/Arizonia.ttf",72)
txt="Wallpapers-For-Kali-2025"; tw=d.textlength(txt,font=f)
d.text(((W-tw)/2,838),txt,font=f,fill=CREAM)
rng=np.random.default_rng(3); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="logo.png" if v=="ship" else f"scratch/logo-{v}.png"
img.save(out); print(out)
img.resize((64,64),Image.LANCZOS).save(f"scratch/logo64-{v}.png"); print("64px saved")
