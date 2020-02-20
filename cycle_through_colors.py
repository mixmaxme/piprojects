import board
import neopixel                    # to control LEDs
import time                        # for sleep/timing commands
from brightness import *           # to load/reload variables from file
import numpy                       # for the cosinus / linspace functions

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))

# Build colorcycle
l = numpy.linspace(0, numpy.pi, v)
# define four areas:
cosup = (-0.5) * a * (numpy.cos(l) - 1)
flattop = numpy.linspace(a, a, v)
cosdown = 0.5 * a * (numpy.cos(l) + 1)
flatbottom = numpy.linspace(0, 0, v)

r = numpy.concatenate([flattop, cosdown, flatbottom, cosup])
g = numpy.concatenate([cosup, flattop, cosdown, flatbottom])
b = numpy.concatenate([flatbottom, cosup, flattop, cosdown])

# make intarray out of floatarray
r = r.astype(int)
g = g.astype(int)
b = b.astype(int)

print("Script started running...")

# Start actual infinite while loop to run script
while True:
          for i in range(4*v):
                    pixels.fill((r[i],g[i],b[i]))
                    time.sleep(0.05)
                    
                    
#          # Startwerte
#          r = (100)
#          g = (0)
#          b = (0)          
#          
#          # rot
#          r1 = (100)
#          g1 = (0)
#          b1 = (0)
#          
#          # gelb
#          r2 = (100)
#          g2 = (100)
#          b2 = (0)
#          
#          # grün
#          r3 = (0)
#          g3 = (100)
#          b3 = (0)
#          
#          # kA
#          r4 = (0)
#          g4 = (100)
#          b4 = (100) 
#          
#          # blau
#          r5 = (0)
#          g5 = (0)
#          b5 = (100)          
#                            
#          # lila
#          r6 = (100)
#          g6 = (0)
#          b6 = (100)
#          
#          print('start with red')
#          for g in range(g1,g2,v):
#                    pixels.fill((r,g,b))
#                    time.sleep(0.05)
#          print('yellow arrived')
#          for r in range(r2,r3,-v):
#                    pixels.fill((r,g,b))  
#                    time.sleep(0.05)
#          print('green arrived')                
#          for b in range(b3,b4,v):
#                    pixels.fill((r,g,b))
#                    time.sleep(0.05)
#          print('cyan arrived')
#          for g in range(g4,g5,-v):
#                    pixels.fill((r,g,b))
#                    time.sleep(0.05)
#          print('blue arrived')          
#          for r in range(r5,r6,v):
#                    pixels.fill((r,g,b))  
#                    time.sleep(0.05)
#          print('purple arrived')
#          for b in range(b6,b1,-v):
#                    pixels.fill((r,g,b))  
#                    time.sleep(0.05)
#          print('red arrived')
