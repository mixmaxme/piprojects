#!/bin/bash

echo "Killing active sudo python processes"
rm /home/pi/piprojects/wc_running.info
sleep 1
touch /home/pi/piprojects/wc_running.info
echo "" | sudo -S pkill -f "sudo python"
pkill -f "max_wordclock"
pkill -f "rainbow"
pkill -f "cycle_through"
pkill -f "fill_wordclock"

echo "Getting options - prepared for use of multiple options"
while getopts ":awpfrct" options; do              # Loop: Get the next option;
                                               # use silent error checking;
                                               # options n and t take arguments.
  case "${options}" in                         # 
    a)
      echo "Starting Wordclock + Rainbow"
      sudo python /home/pi/piprojects/clock_functions/rainbow_with_clock.py
      ;;
    w)                                         # If the option is w
      echo "Starting Wordclock"
      sudo python /home/pi/piprojects/clock_functions/max_wordclock_short.py
      ;;
    p)                                         # If the option is p
      echo "Starting Colorcycle"
      sudo python /home/pi/piprojects/clock_functions/cycle_through_colors.py 5
      ;;
    f)                                         # If the option is f
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
    \? )
      echo "Usage: ./start_wordclock_scripts.sh [-w/p/f]"
     ;;
  esac
done


echo "Started / Finished Python script"
exit 0                                         # Exit normally.
