# piprojects

Website:
- clock_index.html - STATUS: WORKING (slow communication).
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

Note:
HTML page has to be stored in correct folder/Apache has to be reconfigured - correct access rights to work. Access rights too open for public network.
For CGI-Bin to work
