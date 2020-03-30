#!/bin/bash

# Demo mode

echo "Show every available mode"

# Fill wordclock with color
start_wordclock_scripts -w &
sleep 30

start_wordclock_scripts -e &
sleep 30

start_wordclock_scripts -f &
sleep 30

# Cycle through colors
start_wordclock_scripts -w &
sleep 30

start_wordclock_scripts -q &
sleep 30

start_wordclock_scripts -p &
sleep 30

# Show rainbow
start_wordclock_scripts -w &
sleep 30

start_wordclock_scripts -a &
sleep 30

start_wordclock_scripts -r &
sleep 30

# Finish with Picture
start_wordclock_scripts -m &
sleep 30

echo "Demo mode finished"