#!/bin/bash

echo "Killing active sudo python processes"
sudo pkill -f "sudo python"

echo "Getting options - prepared for use of multiple options"
while getopts ":wpfr" options; do              # Loop: Get the next option;
                                               # use silent error checking;
                                               # options n and t take arguments.
  case "${options}" in                         # 
    w)                                         # If the option is w
      echo "Starting Wordclock"
      sudo python /var/www/html/wordclock_modes/max_wordclock_short.py
      ;;
    p)                                         # If the option is p
      echo "Starting Colorcycle"
      sudo python /var/www/html/wordclock_modes/cycle_through_colors.py 5
      ;;
    f)                                         # If the option is f
      echo "Fill wordclock with current color"
      sudo python /var/www/html/wordclock_modes/fill_wordclock.py
      ;;
    r)
      echo "Fill wordclock with a rainbow!"
      sudo python /var/www/html/wordclock_modes/rainbow.py
      ;;
    \? )
      echo "Usage: ./start_wordclock_scripts.sh [-w/p/f]"
     ;;
  esac
done


echo "Started / Finished Python script"
exit 0                                         # Exit normally.
