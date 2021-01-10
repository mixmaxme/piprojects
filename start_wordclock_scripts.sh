#!/bin/bash

echo "Killing active sudo python processes"
sudo pkill -f python

echo "Getting options - prepared for use of multiple options"
while getopts ":abcdefmpqrtw" options; do              # Loop: Get the next option;
  case "${options}" in                         # 
    a)
      echo "Starting Wordclock + Rainbow"
      sudo python /home/pi/piprojects/clock_functions/rainbow_with_clock.py
      ;;
    b)
      echo "Starting autobrightness Wordclock"
      sudo python /home/pi/piprojects/clock_functions/max_wordclock_auto_brightness.py
      ;;
    c)
      echo "Kill all running processes"
      sudo pkill -f python
      ;;
    d) 
      echo "Start Demo Mode"
      bash /hoe/pi/piprojects/demo_mode.sh
      ;;
    e)
      echo "Fill wordclock with color and clock"
      sudo python /home/pi/piprojects/clock_functions/fill_with_clock.py
      ;;
    f)                             
      echo "Fill wordclock with current color"
      sudo python /home/pi/piprojects/clock_functions/fill_wordclock.py
      ;;
    m)
      echo "Fill Wordclock with Yoshi!"
      sudo python /home/pi/piprojects/clock_functions/show_image.py yoshi.png
      ;;
    p)                                      
      echo "Starting Colorcycle"
      sudo python /home/pi/piprojects/clock_functions/cycle_through_colors.py
      ;;
    q)
      echo "Start wordclock with color cycle"
      sudo python /home/pi/piprojects/clock_functions/cycle_through_colors_with_clock.py
      ;;
    r)
      echo "Fill wordclock with a rainbow!"
      sudo python /home/pi/piprojects/clock_functions/rainbow.py
      ;;
    t)
      echo "Fill wordclock with a temperature!"
      sudo python /home/pi/piprojects/clock_functions/show_temperature.py
      ;;
    w)                                      
      echo "Starting Wordclock"
      sudo python /home/pi/piprojects/clock_functions/wordclock.py
      ;;
    \? )
      echo "Usage: ./start_wordclock_scripts.sh [-w/p/f]"
     ;;
  esac
done

echo "Started / Finished Python script"
exit 0                                         # Exit normally.
