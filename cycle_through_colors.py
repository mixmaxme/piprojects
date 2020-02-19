import board
import neopixel                    # to control LEDs
import datetime                    # for datetime management
import time                        # for sleep/timing commands
from random import random
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

# Start actual infinite while loop to run script
while True:
          r0 = int(100*random())
          g0 = int(100*random())
          b0 = int(100*random())
          # Loop thorugh RGB (only to 100)
          for  r in range(r0,100,10):
                    for g in range(g0,100,10):
                              for b in range(b0,100,10):
                                        print(r,g,b)
                                        pixels.fill((r,g,b))
                                        time.sleep(0.0001)
                          
