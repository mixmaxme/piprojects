import board
import neopixel                    # to control LEDs
import datetime                    # for datetime management
import time                        # for sleep/timing commands
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file
#import os.path                     # to check if file exists
import clock_functions_functions as cf

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288, auto_write=False)
pixels.fill((0,0,0))
pixels.show()
olddayminute=0
oncount=0

# Start actual infinite while loop to run script
#while os.path.exists("/home/pi/piprojects/wc_running.info"):
while True:
     # get current time
     daynow = datetime.datetime.now()
     dayhour = daynow.hour
     dayminute = daynow.minute
     
     # perform script only when time (minute) has changed
     if dayminute != olddayminute:          
          # get light time
          lighttime = cf.get_light_time_1(dayhour,dayminute)
          
          # check brightness
          reload( brightness )
          from brightness import *
          # adjust brightness/color levels when wrong values input
          if l > 1:
               l = 1
          if r > 255:
               r = 255
          elif r < 0:
               r = 0
          if g > 255:
               g = 255
          elif g < 0:
               g = 0
          if b > 255:
               b = 255
          elif b < 0:
               b = 0
          # Reset all LEDs to off
          pixels.fill((0,0,0))
     
          for i in lighttime:
               pixels[i]=(int(l*r),int(l*g),int(l*b))
          pixels.show()
                 
          # Counter to keep the times accourate before slowing down the program
          if oncount > 120:
               time.sleep(55)
               
          oncount=oncount+1
     
     # store old minute for beginning of the loop
          olddayminute=dayminute
