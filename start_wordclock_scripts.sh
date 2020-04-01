#!/bin/bash

echo "Killing active sudo python processes"
sudo pkill -f python

echo "Getting options - prepared for use of multiple options"
while getopts ":abwpfrctqem" options; do              # Loop: Get the next option;
  case "${options}" in                         # 
    b)
      echo "Starting autobrightness Wordclock"
      sudo python /home/pi/piprojects/clock_functions/max_wordclock_auto_brightness.py
      ;;
    w)                                      
      echo "Starting Wordclock"
      sudo python /home/pi/piprojects/clock_functions/max_wordclock_short.py
      ;;
    a)
      echo "Starting Wordclock + Rainbow"
      sudo python /home/pi/piprojects/clock_functions/rainbow_with_clock.py
      ;;
    p)                                      
      echo "Starting Colorcycle"
      sudo python /home/pi/piprojects/clock_functions/cycle_through_colors.py
      ;;
    f)                             
      echo "Fill wordclock with current color"
      sudo python /home/pi/piprojects/clock_functions/fill_wordclock.py
      ;;
    r)
      echo "Fill wordclock with a rainbow!"
      sudo python /home/pi/piprojects/clock_functions/rainbow.py
      ;;
    c)
      echo "Kill all running processes"
      sudo pkill -f python
      ;;
    t)
      echo "Fill wordclock with a temperature!"
      sudo python /home/pi/piprojects/clock_functions/show_temperature.py
      ;;
    q)
      echo "Start wordclock with color cycle"
      sudo python /home/pi/piprojects/clock_functions/cycle_through_colors_with_clock.py
      ;;
    e)
      echo "Fill wordclock with color and clock"
      sudo python /home/pi/piprojects/clock_functions/fill_with_clock.py
      ;;
    m)
      echo "Fill Wordclock with Yoshi!"
      sudo python /home/pi/piprojects/clock_functions/show_image.py yoshi.png
      ;;
    \? )
      echo "Usage: ./start_wordclock_scripts.sh [-w/p/f]"
     ;;
  esac
done

echo "Started / Finished Python script"
exit 0                                         # Exit normally.