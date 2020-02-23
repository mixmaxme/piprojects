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

          r = int((r/255)*a)
          g = int((g/255)*a)
          b = int((b/255)*a)
               
          # Fill all LEDs
          pixels.fill((r,g,b))
          
          time.sleep(0.5)
