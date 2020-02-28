import board
import neopixel                    # to control LEDs
import datetime                    # for datetime management
import time                        # for sleep/timing commands
from importlib import reload
import brightness
from brightness import *           # to load/reload variables from file
#import os.path                     # to check if file exists

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288, auto_write=False)
pixels.fill((0,0,0))
pixels.show()
olddayminute=0
oncount=0

# define functions

# Hourfunction
def get_light_hour(hour):
     hourdict = {
          0: null_1,
          1: ein_1,
          2: zwei_1,
          3: drei_1,
          4: vier_1,
          5: fuenf_1,
          6: sechs_1,
          7: sieben_1,
          8: acht_1,
          9: neun_1,
          10: zehn_1,
          11: elf_1,
          12: zwoelf_1
     }
     lighthour = hourdict[hour]
     return lighthour

# Minutefunction
def get_light_minute(minute):
     mindict = {
          0: null_2+minuten_2,
          1: eine_2+minute_2,
          2: zwei_2+minuten_2,
          3: drei_2+minuten_2,
          4: vier_2+minuten_2,
          5: fuenf_2+minuten_2,
          6: sechs_2+minuten_2,
          7: sieben_2+minuten_2,
          8: acht_2+minuten_2,
          9: neun_2+minuten_2,
          10: zehn_2+minuten_2,
          11: elf_2+minuten_2,
          12: zwoelf_2+minuten_2,
          13: drei_2+zehn_2+minuten_2,
          14: vier_2+zehn_2+minuten_2,
          15: fuenf_2+zehn_2+minuten_2,
          16: sech_2+zehn_2+minuten_2,
          17: sieb_2+zehn_2+minuten_2,
          18: acht_2+zehn_2+minuten_2,
          19: neun_2+zehn_2+minuten_2,
          20: zwanzig_2+minuten_2,
          21: ein_4+und_3+zwanzig_2+minuten_2,
          22: zwei_2+und_3+zwanzig_2+minuten_2,
          23: drei_2+und_3+zwanzig_2+minuten_2,
          24: vier_2+und_3+zwanzig_2+minuten_2,
          25: fuenf_2+und_3+zwanzig_2+minuten_2,
          26: sechs_2+und_3+zwanzig_2+minuten_2,
          27: sieben_2+und_3+zwanzig_2+minuten_2,
          28: acht_2+und_3+zwanzig_2+minuten_2,
          29: neun_2+und_3+zwanzig_2+minuten_2,
          30: dreissig_2+minuten_2,
          31: ein_4+und_3+dreissig_2+minuten_2,
          32: zwei_2+und_3+dreissig_2+minuten_2,
          33: drei_2+und_3+dreissig_2+minuten_2,
          34: vier_2+und_3+dreissig_2+minuten_2,
          35: fuenf_2+und_3+dreissig_2+minuten_2,
          36: sechs_2+und_3+dreissig_2+minuten_2,
          37: sieben_2+und_3+dreissig_2+minuten_2,
          38: acht_2+und_3+dreissig_2+minuten_2,
          39: neun_2+und_3+dreissig_2+minuten_2,
          40: vierzig_2+minuten_2,
          41: ein_4+und_3+vierzig_2+minuten_2,
          42: zwei_2+und_3+vierzig_2+minuten_2,
          43: drei_2+und_3+vierzig_2+minuten_2,
          44: vier_2+und_3+vierzig_2+minuten_2,
          45: fuenf_2+und_3+vierzig_2+minuten_2,
          46: sechs_2+und_3+vierzig_2+minuten_2,
          47: sieben_2+und_3+vierzig_2+minuten_2,
          48: acht_2+und_3+vierzig_2+minuten_2,
          49: neun_2+und_3+vierzig_2+minuten_2,
          50: fuenfzig_2+minuten_2,
          51: ein_4+und_3+fuenfzig_2+minuten_2,
          52: zwei_2+und_3+fuenfzig_2+minuten_2,
          53: drei_2+und_3+fuenfzig_2+minuten_2,
          54: vier_2+und_3+fuenfzig_2+minuten_2,
          55: fuenf_2+und_3+fuenfzig_2+minuten_2,
          56: sechs_2+und_3+fuenfzig_2+minuten_2,
          57: sieben_2+und_3+fuenfzig_2+minuten_2,
          58: acht_2+und_3+fuenfzig_2+minuten_2,
          59: neun_2+und_3+fuenfzig_2+minuten_2
     }
     lightminute=mindict[minute]
     return lightminute

# define all occurring words of 24h wordclock (take care - alternating LED numbering)
# Zeile 1
es=(0,1)
ist=(3,4,5)
viertel=(7,8,9,10,11,12,13)
ein_1=(14,15,16)
eins_1=(14,15,16,17)
wc_in=(15,16)
# Zeile 2
drei_1=(35,34,33,32)
ein_2=(33,32,31)
eine_1=(33,32,31,30)
einer=(33,32,31,30,29)
sech_1=(28,27,26,25)
sechs_1=(28,27,26,25,24)
sieb_1=(24,23,22,21)
sieben_1=(24,23,22,21,20,19)
# Zeile 3
elf_1=(36,37,38)
fuenf_1=(38,39,40,41)
neun_1=(42,43,44,45)
vier_1=(46,47,48,49)
acht_1=(50,51,52,53)
# Zeile 4
null_1=(71,70,69,68)
zwei_1=(67,66,65,64)
zwoelf_1=(62,61,60,59,58)
zehn_1=(57,56,55,54)
# Zeile 5
und_1=(72,73,74)
zwanzig_1=(76,77,78,79,80,81,82)
vierzig_1=(83,84,85,86,87,88,89)
# Zeile 6
dreissig_2=(107,106,105,104,103,102,101,100)
fuenfzig_1=(99,98,97,96,95,94,93)
uhr=(92,91,90)
# Zeile 7
minute_1=(108,109,110,111,112,113)
minuten_1=(108,109,110,111,112,113,114)
vor_1=(116,117,118)
und_2=(119,120,121)
nach_1=(122,123,124,125)
# Zeile 8
ein_3=(143,142,141)
dreiviertel_=(140,139,138,137,136,135,134,133,132,131,130)
viertel_2=(136,135,134,133,132,131,130)
halb=(129,128,127,126)
# Zeile 9
sieb_2=(144,145,146,147)
sieben_2=(144,145,146,147,148,149)
neun_2=(149,150,151,152)
null_2=(152,153,154,155)
zwei_2=(156,157,158,159)
ein_4=(158,159,160)
eine_2=(158,159,160,161)
# Zeile 10
fuenf_2=(179,178,177,176)
sech_2=(175,174,173,172)
sechs_2=(175,174,173,172,171)
nach=(170,169,168,167)
nacht=(170,169,168,167,166)
acht_2=(169,168,167,166)
vier_2=(165,164,163,162)
# Zeile 11
drei_2=(180,181,182,183)
ein_5=(182,183,184)
eins_2=(182,183,184,185)
und_3=(186,187,188)
elf_2=(190,191,192)
zehn_2=(194,195,196,197)
# Zeile 12
zwanzig_2=(215,214,213,212,211,210,209)
grad=(208,207,206,205)
dreissig_2=(205,204,203,202,201,200,199,198)
# Zeile 13
vierzig_2=(216,217,218,219,220,221,222)
zwoelf_2=(223,224,225,226,227)
fuenfzig_2=(227,228,229,230,231,232,233)
# Zeile 14
minute_2=(251,250,249,248,247,246)
minuten_2=(251,250,249,248,247,246,245)
uhr_2=(244,243,242)
frueh=(240,239,238,237)
vor_2=(236,235,234)
# Zeile 15
abends=(252,253,254,255,256,257)
mitternacht=(258,259,260,261,262,263,264,265,266,267,268)
nachts=(264,265,266,267,268,269)
# Zeile 16
morgens=(287,286,285,284,283,282,281)
warm=(280,279,278,277)
mittags=(276,275,274,273,272,271,270)

# Start actual infinite while loop to run script
#while os.path.exists("/home/pi/piprojects/wc_running.info"):
while True:
     # get current time
     daynow = datetime.datetime.now()
     dayhour = daynow.hour
     dayminute = daynow.minute
     
     # perform script only when time (minute) has changed
     if dayminute != olddayminute:          
          # get timerange of the day
          if dayhour > 12:
               dayhour = dayhour-12
               tageszeit = mittags
               if dayhour > 5:
                    tageszeit = abends
               elif dayhour > 9:
                    tageszeit = nachts
          
          else:
               tageszeit = morgens
               if dayhour == 1:
                    tageszeit = nachts
               elif dayhour == 2:
                    tageszeit = frueh
               elif dayhour == 3:
                    tageszeit = frueh
               elif dayhour == 4:
                    tageszeit = frueh
               elif dayhour == 0:
                    tageszeit = mitternacht
                    
          # check and light h
          lighthour = get_light_hour(dayhour)
          lightminute = get_light_minute(dayminute)
          lighttime = es+ist+lighthour+uhr+und_2+lightminute+tageszeit
          
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
          #print("Script running")
