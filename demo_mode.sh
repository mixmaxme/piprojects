#!/bin/bash

# Demo mode

echo "Show every available mode"

export PATH=$PATH:/home/pi/piprojects

# Fill wordclock with color
bash /home/pi/piprojects/start_wordclock_scripts -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -e &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -f &
sleep 30

# Cycle through colors
bash /home/pi/piprojects/start_wordclock_scripts -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -q &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -p &
sleep 30

# Show rainbow
bash /home/pi/piprojects/start_wordclock_scripts -w &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -a &
sleep 30

bash /home/pi/piprojects/start_wordclock_scripts -r &
sleep 30

# Finish with Picture
bash /home/pi/piprojects/start_wordclock_scripts -m &
sleep 30

echo "Demo mode finished"