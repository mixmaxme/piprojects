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
          # Loop thorugh RGB (only to 100)
         for  r in range(0,10,100):
              for g in range(0,10,100):
                    for b in range(0,10,100):
                          print(r,g,b)
                          pixels.fill((r,g,b))
                          time.sleep(0.0001)
                          
