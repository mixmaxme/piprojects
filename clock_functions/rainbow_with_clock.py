import board
import neopixel                    # to control LEDs
import time                        # for sleep/timing commands
import datetime
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file
import numpy                       # for the cosinus / linspace functions
from collections import deque
import clock_functions_functions as cf

## Initialize Variables
nol = 288
# get slowness
s = int(nol/6)
v = int(v*50)

# initialize system
pixels = neopixel.NeoPixel(board.D18, nol, auto_write=False)
pixels.fill((0,0,0))
pixels.show()
olddayminute=0
oncount=0

# Build colorcycle
l = numpy.linspace(0, numpy.pi, s)
# define four areas:
cosup = (-0.5) * a * (numpy.cos(l) - 1)
flattop = numpy.linspace(a, a, s)
cosdown = 0.5 * a * (numpy.cos(l) + 1)
flatbottom = numpy.linspace(0, 0, s)

rold = numpy.concatenate([flattop, cosdown, flatbottom, flatbottom, cosup, flattop])
gold = numpy.concatenate([cosup, flattop, flattop, cosdown, flatbottom, flatbottom])
bold = numpy.concatenate([flatbottom, flatbottom, cosup, flattop, flattop, cosdown])

# make intarray out of floatarray
rold = rold.astype(int)
gold = gold.astype(int)
bold = bold.astype(int)

rold = deque(rold)
gold = deque(gold)
bold = deque(bold)



print("Script started running...")

# Start actual infinite while loop to run script
while True:
# get current time
     daynow = datetime.datetime.now()
     dayhour = daynow.hour
     dayminute = daynow.minute
     
     # perform script only when time (minute) has changed
     if dayminute != olddayminute:          
          # get light time
          lighttime = cf.get_light_time_1(dayhour,dayminute)

# Fill up pixels
     for i in range(nol):
            pixels[i]=(rold[i],gold[i],bold[i])   
     for i in lighttime:
            pixels[i]=(r,g,b)
      
     pixels.show()
     rold.rotate(v)
     gold.rotate(v)
     bold.rotate(v)
     time.sleep(0.03)
     reload( brightness )
     from brightness import *
     v = int(v*50)
