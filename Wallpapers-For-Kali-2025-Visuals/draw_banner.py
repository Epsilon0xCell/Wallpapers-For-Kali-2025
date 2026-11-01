#!/usr/bin/env python3
"""Wallpapers banner: stage from the third row before house lights fall. Prompter's
box centre with two hands on the prompt book and a forehead in shadow, playbills tied
with string left, ticket stubs right, water glass, brass bell, closed scarlet curtain,
sky cloth above the valance. Title lettered in Arizonia on the largest playbill
propped against the box, held flat by the bell."""
import sys, random
from PIL import Image, ImageDraw, ImageFont
import numpy as np
random.seed(13)
W,H=1600,900
v=sys.argv[1] if len(sys.argv)>1 else "ship"
SCARLET=(142,26,34); CREAM=(244,234,208); STRAW=(206,178,120); SKY=(126,168,208); AMBER=(255,196,110); BRASS=(186,150,70)
img=Image.new("RGB",(W,H),(10,8,10)); d=ImageDraw.Draw(img,"RGBA")
d.rectangle([180,20,1420,110],fill=SKY); d.rectangle([0,104,1600,140],fill=(52,20,24))
for i in range(26):
    x=i*64; shade=SCARLET if i%2==0 else (112,20,28)
    d.rectangle([x,140,x+64,720],fill=shade); d.line([(x+6,140),(x+6,720)],fill=(170,52,58),width=3)
d.rectangle([0,720,1600,900],fill=(96,72,44))
for bx in range(0,1600,130): d.line([(bx,720),(bx-40,900)],fill=(76,56,32),width=3)
# playbill stack tied with string, left
for i in range(4):
    x=120+i*8; y=706-i*16; d.rectangle([x,y,x+190,y+26],fill=CREAM if i%2 else (232,220,192),outline=STRAW,width=2)
d.line([(210,690),(210,766)],fill=STRAW,width=4); d.line([(120,728),(318,728)],fill=STRAW,width=3)
# ticket stubs scattered right, water glass
for i in range(14):
    x=1180+random.randint(0,300); y=760+random.randint(0,90); d.rectangle([x,y,x+24,y+12],fill=CREAM)
d.polygon([(1120,690),(1162,690),(1156,748),(1126,748)],outline=(210,225,235),width=3)
d.line([(1124,706),(1158,706)],fill=(170,200,220),width=3)
# prompter's box centre with hands and forehead in shadow
bx,by=800,640
d.pieslice([bx-240,by-250,bx+240,by+60],180,360,fill=(70,13,19)); d.pieslice([bx-240,by-250,bx+240,by+60],180,360,outline=(190,76,62),width=6)
d.rectangle([bx-240,by-100,bx+240,by+150],fill=(50,9,15))
d.ellipse([bx-42,by-96,bx+42,by-38],fill=(36,10,12))  # forehead in shadow, no face detail
d.polygon([(bx-130,by+96),(bx-8,by+72),(bx-8,by-6),(bx-130,by+22)],fill=CREAM)
d.polygon([(bx+130,by+96),(bx+8,by+72),(bx+8,by-6),(bx+130,by+22)],fill=(238,226,196))
# two hands resting on the book
for hx,hy in ((bx-96,by+58),(bx+62,by+58)):
    d.ellipse([hx,hy,hx+52,hy+24],fill=(216,170,132))
    for fng in range(4): d.line([(hx+8+fng*11,hy+20),(hx+8+fng*11,hy+34)],fill=(216,170,132),width=5)
# largest playbill propped against the box with the title, bell holding it flat
d.rectangle([bx-330,by+74,bx+330,by+214],fill=CREAM,outline=STRAW,width=3)
f=ImageFont.truetype("fonts/Arizonia.ttf",62 if v!="v1" else 76)
txt="Wallpapers-For-Kali-2025"; tw=d.textlength(txt,font=f)
d.text(((bx-tw/2),by+112),txt,font=f,fill=(60,30,20))
d.ellipse([bx+238,by+52,bx+292,by+96],fill=BRASS); d.rectangle([bx+258,by+38,bx+272,by+56],fill=BRASS)  # bell on the playbill corner
for i in range(11):
    x=90+i*142; d.ellipse([x-16,838,x+16,870],fill=AMBER)
rng=np.random.default_rng(4); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="banner.png" if v=="ship" else f"scratch/banner-{v}.png"
img.save(out); print(out)
