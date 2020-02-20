
import board
import neopixel                    # to control LEDs
import time                        # for sleep/timing commands
from brightness import *           # to load/reload variables from file
import numpy                       # for the cosinus / linspace functions

## Initialize Variables
nol=288
# get slowness
s=int(nol/6)

# initialize system
pixels = neopixel.NeoPixel(board.D18, nol, auto_write=False)
pixels.fill((0,0,0))

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

print("Script started running...")

# Start actual infinite while loop to run script
while True:
      for i in range(nol):
            pixels[i]=(r[i],g[i],b[i])
     
      pixels.show()
