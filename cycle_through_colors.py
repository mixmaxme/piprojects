import board
import neopixel                    # to control LEDs
import time                        # for sleep/timing commands
import sys                         # to get velocity imported

# initialize system
pixels = neopixel.NeoPixel(board.D18, 288)
pixels.fill((0,0,0))
v=int(sys.argv[1])

print("Script started running...")

# Start actual infinite while loop to run script
while True:
          # Startwerte
          r = (100)
          g = (0)
          b = (0)          
          
          # rot
          r1 = (100)
          g1 = (0)
          b1 = (0)
          
          # gelb
          r2 = (100)
          g2 = (100)
          b2 = (0)
          
          # grün
          r3 = (0)
          g3 = (100)
          b3 = (0)
          
          # kA
          r4 = (0)
          g4 = (100)
          b4 = (100) 
          
          # blau
          r5 = (0)
          g5 = (0)
          b5 = (100)          
                            
          # lila
          r6 = (100)
          g6 = (0)
          b6 = (100)
          
          print('start with red')
          for g in range(g1,g2,v):
                    pixels.fill((r,g,b))
                    time.sleep(0.05)
          print('yellow arrived')
          for r in range(r2,r3,-v):
                    pixels.fill((r,g,b))  
                    time.sleep(0.05)
          print('green arrived')                
          for b in range(b3,b4,v):
                    pixels.fill((r,g,b))
                    time.sleep(0.05)
          print('cyan arrived')
          for g in range(g4,g5,-v):
                    pixels.fill((r,g,b))
                    time.sleep(0.05)
          print('blue arrived')          
          for r in range(r5,r6,v):
                    pixels.fill((r,g,b))  
                    time.sleep(0.05)
          print('purple arrived')
          for b in range(b6,b1,-v):
                    pixels.fill((r,g,b))  
                    time.sleep(0.05)
          print('red arrived')
