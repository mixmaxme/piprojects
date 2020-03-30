#!/bin/bash

# Demo mode

echo "Show every available mode"

export PATH=$PATH:/home/pi/piprojects

# Fill wordclock with color
bash /home/pi/piprojects/start_wordclock_scripts.sh -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -e &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -f &
sleep 30

# Cycle through colors
bash /home/pi/piprojects/start_wordclock_scripts.sh -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -q &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -p &
sleep 30

# Show rainbow
bash /home/pi/piprojects/start_wordclock_scripts.sh -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -a &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts.sh -r &
sleep 30

# Finish with Picture
bash /home/pi/piprojects/start_wordclock_scripts.sh -m &
sleep 30

echo "Demo mode finished"