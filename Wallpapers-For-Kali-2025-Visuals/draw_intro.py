#!/usr/bin/env python3
"""Wallpapers intro: darkened opera stage before a performance, wordless. Footlights
along the apron, ticket stubs at a stair, prompter's box centre with open prompt book
shown as blank cream shapes with soft grey bands and no letterforms, closed scarlet
curtain with one heavier right fold, empty chair with shawl in the left wing gap,
folded music stand in the right wing gap, sky cloth with a plain cream moon above
the valance, dust in the footlight beams. No text of any kind."""
import sys, random
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
random.seed(41)
W,H=1600,900
v=sys.argv[1] if len(sys.argv)>1 else "ship"
SCARLET=(142,26,34); CREAM=(244,234,208); STRAW=(206,178,120); SKY=(126,168,208); AMBER=(255,196,110)
img=Image.new("RGB",(W,H),(8,6,8)); d=ImageDraw.Draw(img,"RGBA")
# sky cloth strip above valance with plain moon
d.rectangle([200,26,1400,120],fill=SKY)
d.ellipse([1180,42,1264,126],fill=CREAM)
d.rectangle([0,0,200,140],fill=(8,6,8)); d.rectangle([1400,0,1600,140],fill=(8,6,8))
d.rectangle([0,116,1600,150],fill=(52,20,24))  # valance
# closed curtain, scarlet folds straight; right fold heavier
for i in range(26):
    x=i*64
    shade = SCARLET if i%2==0 else (112,20,28)
    if i==21: shade=(88,15,22)
    wdt = 86 if i==21 else 64
    d.rectangle([x,150,x+wdt,742],fill=shade)
    d.line([(x+6,150),(x+6,742)],fill=(170,52,58),width=3)
d.rectangle([0,742,1600,760],fill=(96,18,26))
# left wing gap: chair with shawl; right wing gap: folded music stand
d.rectangle([0,300,86,760],fill=(14,10,12)); d.rectangle([1514,300,1600,760],fill=(14,10,12))
d.rectangle([24,468,72,528],fill=(120,90,54))
d.polygon([(22,462),(74,462),(70,506),(26,506)],fill=(172,154,172))  # shawl draped over chair back
d.rectangle([20,528,76,544],fill=(120,90,54)); d.line([(28,544),(28,646)],fill=(120,90,54),width=6); d.line([(68,544),(68,646)],fill=(120,90,54),width=6)
# folded stand: X frame with a small tilted desk plate, flat against the wing
d.line([(1538,560),(1578,660)],fill=(150,150,156),width=5); d.line([(1578,560),(1538,660)],fill=(150,150,156),width=5)
d.polygon([(1540,520),(1576,532),(1572,560),(1544,548)],fill=(150,150,156))
# boards
d.rectangle([0,760,1600,900],fill=(96,72,44))
for bx in range(0,1600,130): d.line([(bx,760),(bx-40,900)],fill=(76,56,32),width=3)
# stage stair lowest step left with stub drift
d.rectangle([60,724,240,760],fill=(110,84,50))
for i in range(12):
    x=70+random.randint(0,150); y=736+random.randint(0,16); d.rectangle([x,y,x+18,y+9],fill=CREAM)
# prompter's box centre: dark lacquer body distinct from the curtain, hood dome above, book inside on its ledge
bx,by=800,690
d.pieslice([bx-196,by-268,bx+196,by+40],180,360,fill=(74,14,20))  # hood dome, top in shadow
d.pieslice([bx-196,by-268,bx+196,by+40],180,360,outline=(188,72,60),width=6)
d.rectangle([bx-196,by-118,bx+196,by+96],fill=(58,12,18))
d.rectangle([bx-196,by+78,bx+196,by+96],fill=(40,8,12))
# book: two blank cream page shapes on sloped ledge inside the hood opening
d.polygon([(bx-118,by+52),(bx-6,by+30),(bx-6,by-52),(bx-118,by-30)],fill=CREAM)
d.polygon([(bx+118,by+52),(bx+6,by+30),(bx+6,by-52),(bx+118,by-30)],fill=(238,226,196))
for gy in range(-28,34,16):
    d.line([(bx-104,by+gy+8),(bx-20,by+gy-6)],fill=(188,182,168),width=5)
    d.line([(bx+20,by+gy-6),(bx+104,by+gy+8)],fill=(182,176,162),width=5)
d.rectangle([bx-140,by+58,bx+140,by+72],fill=(30,6,10))  # ledge shadow under book
# footlight row with glow and dust
glow=Image.new("RGBA",(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow)
for i in range(11):
    x=90+i*142
    gd.ellipse([x-44,690,x+44,792],fill=(255,190,100,50))
    gd.polygon([(x-16,742),(x+16,742),(x+52,470),(x-52,470)],fill=(255,205,120,16))
img=Image.alpha_composite(img.convert("RGBA"),glow.filter(ImageFilter.GaussianBlur(10))).convert("RGB"); d=ImageDraw.Draw(img,"RGBA")
for i in range(11):
    x=90+i*142
    d.ellipse([x-17,724,x+17,758],fill=AMBER); d.arc([x-22,712,x+22,760],180,360,fill=STRAW,width=4)
    for k in range(6):
        dx=x+random.randint(-30,30); dy=520+random.randint(0,190); d.ellipse([dx,dy,dx+3,dy+3],fill=(255,240,210,170))
rng=np.random.default_rng(9); a=np.asarray(img).astype(np.int16); n=rng.normal(0,4,a.shape[:2])[...,None]
img=Image.fromarray(np.clip(a+n,0,255).astype(np.uint8))
out="intro-banner.png" if v=="ship" else f"scratch/intro-{v}.png"
img.save(out); print(out)
