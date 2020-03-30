import board
import neopixel                    # to control LEDs
import datetime                    # for datetime management
import time                        # for sleep/timing commands
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file
import os, sys
from PIL import Image

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288, auto_write=False)
pixels.fill((0,0,0))
pixels.show()

# Load image
im = Image.open("/home/pi/piprojects/pictures/mario18x16.png")
im_small = im.resize((18, 16))

pix = im.load

# make shifting list
rearrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
for j in range(2,8):
    for i in range((18*(j-1)*2),(18*(j-1)*2)-18,-1):
        rearrange = rearrange + [i]
    for i in range((18*(j-1)*2)+1,(18*(j-1)*2)+19):
        rearrange = rearrange + [i]
for i in range(288,270,-1):
    rearrange = rearrange + [i]

print(rearrange)

print(pix[1,1])

for i in range(1,18):
    for j in range(1,16):
        print(pix[i,j])