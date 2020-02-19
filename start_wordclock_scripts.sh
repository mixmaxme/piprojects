#!/bin/bash

echo "Killing active sudo python processes"
pkill -f "sudo python"

usage() 
{                                              # Function: To print a help message.
  echo "Wird eh nicht im Terminal gestartet! Falls doch -w ist wordclock, -p ist colorcycle, -f ist fill." 1>&2 
}

exit_abnormal() 
{                                              # Function: Exit with error.
  usage
  exit 1
}

echo "Getting options - prepared for use of multiple options"
while getopts ":n:t:" options; do              # Loop: Get the next option;
                                               # use silent error checking;
                                               # options n and t take arguments.
  case "${options}" in                         # 
    w)                                         # If the option is w
      sudo python max_wordclock_short.py
      ;;
    p)                                         # If the option is p
      sudo python cycle_through_colors.py
      ;;
    f)                                         # If the option is f
      sudo python fill_wordclock.py
  esac
done


echo "Started / Finished Python script"
exit 0                                         # Exit normally.
