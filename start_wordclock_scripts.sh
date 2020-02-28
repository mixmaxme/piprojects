#!/bin/bash

echo "Killing active sudo python processes"
echo "pi"  | sudo -S pkill -f "sudo python"

echo "Getting options - prepared for use of multiple options"
while getopts ":awpfr" options; do              # Loop: Get the next option;
                                               # use silent error checking;
                                               # options n and t take arguments.
  case "${options}" in                         # 
    a)
      echo "Starting Wordclock + Rainbow"
      echo "pi"  | sudo -S python /home/pi/piprojects/clock_functions/rainbow_with_clock.py
      ;;
    w)                                         # If the option is w
      echo "Starting Wordclock"
      echo "pi"  | sudo -S python /home/pi/piprojects/clock_functions/max_wordclock_short.py
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
    \? )
      echo "Usage: ./start_wordclock_scripts.sh [-w/p/f]"
     ;;
  esac
done


echo "Started / Finished Python script"
exit 0                                         # Exit normally.
