import board
import neopixel
import datetime
from brightness import *

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))
olddayminute=0

def get_light_hour(hour):
     if hour == 1:
          lighthour=eins_1
     elif hour == 2:
          lighthour=zwei_1
     elif hour == 3:
          lighthour=drei_1
     elif hour == 4:
          lighthour=vier_1
     elif hour == 5:
          lighthour=fuenf_1
     elif hour == 6:
          lighthour=sechs_1
     elif hour == 7:
          lighthour=sieben_1
     elif hour == 8:
          lighthour=acht_1
     elif hour == 9:
          lighthour=neun_1
     elif hour == 10:
          lighthour=zehn_1
     elif hour == 11:
          lighthour=elf_1
     elif hour == 12:
          lighthour=zwoelf_1
     elif hour == 0:
          lighthour=null_1
     return lighthour

def get_light_minute(minute):
     if minute == 0:
          lightminute=null_2+minuten_2
     elif minute == 1:
          lightminute=eine_2+minute_2
     elif minute == 2:
          lightminute=zwei_2+minuten_2
     elif minute == 3:
          lightminute=drei_2+minuten_2
     elif minute == 4:
          lightminute=vier_2+minuten_2
     elif minute == 5:
          lightminute=fuenf_2+minuten_2
     elif minute == 6:
          lightminute=sechs_2+minuten_2
     elif minute == 7:
          lightminute=sieben_2+minuten_2
     elif minute == 8:
          lightminute=acht_2+minuten_2
     elif minute == 9:
          lightminute=neun_2+minuten_2
     elif minute == 10:
          lightminute=zehn_2+minuten_2
     elif minute == 11:
          lightminute=elf_2+minuten_2
     elif minute == 12:
          lightminute=zwoelf_2+minuten_2
     elif minute == 13:
          lightminute=drei_2+zehn_2+minuten_2
     elif minute == 14:
          lightminute=vier_2+zehn_2+minuten_2
     elif minute == 15:
          lightminute=fuenf_2+zehn_2+minuten_2
     elif minute == 16:
          lightminute=sech_2+zehn_2+minuten_2
     elif minute == 17:
          lightminute=sieb_2+zehn_2+minuten_2
     elif minute == 18:
          lightminute=acht_2+zehn_2+minuten_2
     elif minute == 19:
          lightminute=neun_2+zehn_2+minuten_2
     elif minute == 20:
          lightminute=zwanzig_1+minuten_2
     elif minute == 21:
          lightminute=ein_2+und_3+zwanzig_2+minuten_2
     elif minute == 22:
          lightminute=zwei_2+und_3+zwanzig_2+minuten_2
     elif minute == 23:
          lightminute=drei_2+und_3+zwanzig_2+minuten_2
     elif minute == 24:
          lightminute=vier_2+und_3+zwanzig_2+minuten_2
     elif minute == 25:
          lightminute=fuenf_2+und_3+zwanzig_2+minuten_2
     elif minute == 26:
          lightminute=sech_2+und_3+zwanzig_2+minuten_2
     elif minute == 27:
          lightminute=sieben_2+und_3+zwanzig_2+minuten_2
     elif minute == 28:
          lightminute=acht_2+und_3+zwanzig_2+minuten_2
     elif minute == 291:
          lightminute=neun_2+und_3+zwanzig_2+minuten_2
     elif minute == 30:
          lightminute=dreissig_2+minuten_2
     elif minute == 31:
          lightminute=ein_2+und_3+dreissig_2+minuten_2
     elif minute == 32:
          lightminute=zwei_2+und_3+dreissig_2+minuten_2
     elif minute == 33:
          lightminute=drei_2+und_3+dreissig_2+minuten_2
     elif minute == 34:
          lightminute=vier_2+und_3+dreissig_2+minuten_2
     elif minute == 35:
          lightminute=fuenf_2+und_3+dreissig_2+minuten_2
     elif minute == 36:
          lightminute=sechs_2+und_3+dreissig_2+minuten_2
     elif minute == 37:
          lightminute=sieben_2+und_3+dreissig_2+minuten_2
     elif minute == 38:
          lightminute=acht_2+und_3+dreissig_2+minuten_2
     elif minute == 39:
          lightminute=neun_2+und_3+dreissig_2+minuten_2
     elif minute == 40:
          lightminute=vierzig_1+minuten_2
     elif minute == 41:
          lightminute=ein_2+und_3+vierzig_2+minuten_2
     elif minute == 42:
          lightminute=zwei_2+und_3+vierzig_2+minuten_2
     elif minute == 43:
          lightminute=drei_2+und_3+vierzig_2+minuten_2
     elif minute == 44:
          lightminute=vier_2+und_3+vierzig_2+minuten_2
     elif minute == 45:
          lightminute=fuenf_2+und_3+vierzig_2+minuten_2
     elif minute == 46:
          lightminute=sechs_2+und_3+vierzig_2+minuten_2
     elif minute == 47:
          lightminute=sieben_2+und_3+vierzig_2+minuten_2
     elif minute == 48:
          lightminute=acht_2+und_3+vierzig_2+minuten_2
     elif minute == 49:
          lightminute=neun_2+und_3+vierzig_2+minuten_2
     elif minute == 50:
          lightminute=fuenfzig_1+minuten_2
     elif minute == 51:
          lightminute=ein_2+und_3+fuenfzig_2+minuten_2
     elif minute == 52:
          lightminute=zwei_2+und_3+fuenfzig_2+minuten_2
     elif minute == 53:
          lightminute=drei_2+und_3+fuenfzig_2+minuten_2
     elif minute == 54:
          lightminute=vier_2+und_3+fuenfzig_2+minuten_2
     elif minute == 55:
          lightminute=fuenf_2+und_3+fuenfzig_2+minuten_2
     elif minute == 56:
          lightminute=sechs_2+und_3+fuenfzig_2+minuten_2
     elif minute == 57:
          lightminute=sieben_2+und_3+fuenfzig_2+minuten_2
     elif minute == 58:
          lightminute=acht_2+und_3+fuenfzig_2+minuten_2
     elif minute == 59:
          lightminute=neun_2+und_3+fuenfzig_2+minuten_2
     else:
          lightminute=zwoelf_2
     return lightminute

# define all words
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
mittags=(276,275,274.273,272,271,270)

while True:
     # get current time
     daynow = datetime.datetime.now()
     dayhour = daynow.hour
     dayminute = daynow.minute

     # get morning or afternoon
     if dayhour > 12:
          dayhour = dayhour-12
          tageszeit = mittags
          if dayhour > 5:
               tageszeit = abends
          elif dayhour > 9:
               tageszeit = nachts
          elif dayhour == 0:
               tageszeit = mitternacht
     else:
          tageszeit = morgens
          if dayhour < 4:
            tageszeit = frueh
    

     
     # check and light h
     lighthour = get_light_hour(dayhour)
     lightminute = get_light_minute(dayminute)
     
     if dayminute != olddayminute:
          # check brightness
          reload( x )
          reload( y )
          reload( z )
          pixels.fill((0,0,0))
     
          for i in es+ist+lighthour+uhr+und_2+lightminute+tageszeit:
               pixels[i]=(x,y,z)
     
     # store old minute
          olddayminute=dayminute
          del x
          del y
          del z
          print("Script running")


    
        




