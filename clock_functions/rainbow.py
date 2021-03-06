
import board
import neopixel                    # to control LEDs
import time                        # for sleep/timing commands
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file
import numpy                       # for the cosinus / linspace functions
from collections import deque

## Initialize Variables
nol = 288
# get slowness
s = int(nol/6)
v = int(v*50)

# initialize system
pixels = neopixel.NeoPixel(board.D18, nol, auto_write=False)
pixels.fill((0,0,0))
pixels.show()

# Build colorcycle
l = numpy.linspace(0, numpy.pi, s)
# define four areas:
cosup = (-0.5) * a * (numpy.cos(l) - 1)
flattop = numpy.linspace(a, a, s)
cosdown = 0.5 * a * (numpy.cos(l) + 1)
flatbottom = numpy.linspace(0, 0, s)

r = numpy.concatenate([flattop, cosdown, flatbottom, flatbottom, cosup, flattop])
g = numpy.concatenate([cosup, flattop, flattop, cosdown, flatbottom, flatbottom])
b = numpy.concatenate([flatbottom, flatbottom, cosup, flattop, flattop, cosdown])

# make intarray out of floatarray
r = r.astype(int)
g = g.astype(int)
b = b.astype(int)

r = deque(r)
g = deque(g)
b = deque(b)

print("Script started running...")

# Start actual infinite while loop to run script
while True:
      for i in range(nol):
            pixels[i]=(r[i],g[i],b[i])   
      
      pixels.show()
      r.rotate(v)
      g.rotate(v)
      b.rotate(v)
      time.sleep(0.03)
      reload( brightness )
      from brightness import v
      v = int(v*50)
