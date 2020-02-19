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
          # Startwerte
          r = (120)
          g = (0)
          b = (0)          
          
          # rot
          r1 = (120)
          g1 = (0)
          b1 = (0)
          
          # gelb
          r2 = (120)
          g2 = (120)
          b2 = (0)
          
          # grün
          r3 = (0)
          g3 = (120)
          b3 = (0)
          
          # kA
          r4 = (0)
          g4 = (120)
          b4 = (120) 
          
          # blau
          r5 = (0)
          g5 = (0)
          b5 = (120)          
                            
          # lila
          r6 = (120)
          g6 = (0)
          b6 = (120)
          
          for g in range(g1,g2,1):
                  pixels.fill((r,g,b))
          
          for r in range(r2,r3,-1):
                  pixels.fill((r,g,b))         
                          
          for b in range(b3,b4,1):
                  pixels.fill((r,g,b))

          for g in range(g4,g5,-1):
                  pixels.fill((r,g,b))
                    
          for r in range(r5,r6,1):
                  pixels.fill((r,g,b))      
 
          for b in range(b6,b1,-1):
                  pixels.fill((r,g,b))            
