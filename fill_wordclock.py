import board
import neopixel                    # to control LEDs
import datetime                    # for datetime management
import time                        # for sleep/timing commands
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

# Start actual infinite while loop to run script
while True:
          # check brightness and color
          reload( brightness )
          from brightness import *
          # adjust brightness/color levels when wrong values input
          if l > 1:
               l = 1
          if r > 100:
               r = 100
          elif r < 0:
               r = 0
          if g > 100:
               g = 100
          elif g < 0:
               g = 0
          if b > 100:
               b = 100
          elif b < 0:
               b = 0
               
          # Fill all LEDs
          pixels.fill((r,g,b))
          
          time.sleep(0.5)
