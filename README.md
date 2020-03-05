# piprojects

Website:
- clock_index.html - STATUS: PHP Working - CGI and Color Picker not working.
- brightness.py - STATUS: WORKING 
  - php scripts - all working, one for every wordclock mode
  - php script / cgi script to get data from website not working

Wordclock Modes
- max_wordclock_short.py - STATUS: GOOD
- fill_wordclock.py - STATUS: GOOD
- cylce_through_colors.py - STATUS: GOOD
- rainbow.py - STATUS: GOOD
- max_wordclock_auto_brightness.py - STATUS: GOOD
- rainbow_with_clock.py - STATUS: GOOD
- show_temperature.py - STATUS: GOOD

I2C Scripts:
- bme280.py - in the same folder to call it
- lightsensor - only a few lines of code - in the autobrightness wordclock mode

Misc
- brightness.py - STATUS: WORKING - maybe reduce different brightness levels down to one
- bluetooth startup script to configure the WLAN access of the wordclock - STATUS: NOT WORKING
- crontab - STATUS: GOOD
- info - Links to important pages


HTML Page with several buttons should be build, where the buttons start a shell-script that kills all wordclock-related running scripts and then starts the requested script (test if nohup and/or & is needed)
