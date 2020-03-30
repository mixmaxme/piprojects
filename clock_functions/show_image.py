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
pix = im.load

pixeltemp = pixels

for i in 1,8:
    n = 1
    for j in 2*i*18,(2*i*18)-18:
        pixeltemp[2*i,n] = pixels[2*i,j] 
        n = n + 1

print(pix)