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
background = Image.new("RGB",im_small.size, (255,255,255))
background.paste(im_small, mask = im_small.split()[3])
background.save("/home/pi/piprojects/pictures/mario18x16.jpg", "JPEG", quality=100)
im_rgb = Image.open("/home/pi/piprojects/pictures/mario18x16.jpg")

# make shifting list
rearrange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
for j in range(2,8):
    for i in range((18*(j-1)*2),(18*(j-1)*2)-18,-1):
        rearrange = rearrange + [i]
    for i in range((18*(j-1)*2)+1,(18*(j-1)*2)+19):
        rearrange = rearrange + [i]
for i in range(288,270,-1):
    rearrange = rearrange + [i]

pixel_values = list(im_rgb.getdata())

print(len(rearrange))

for i in range(0,269):
    j = int(rearrange[i])-1
    pixels[j] = pixel_values[i]

pixels.show()