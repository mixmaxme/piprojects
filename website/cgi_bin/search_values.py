#!/usr/bin/python
print("Content-type:text/html\r\n\r\n")
print('<html>')

import cgi, cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
rotwert = form.getvalue('rwert')
gruenwert = form.getvalue('gwert')
blauwert = form.getvalue('bwert')
helligkeit = form.getvalue('hwert')
alleshell = form.getvalue('awert')
geschwindigkeit = form.getvalue('vwert')

# Insert Tests to validate values

f = open("/home/pi/piprojects/clock_functions/brightness.py", "w+")

f.write("r = ")
f.write(rotwert)
f.write("\n")
f.write("g = ")
f.write(gruenwert)
f.write("\n")
f.write("b = ")
f.write(blauwert)
f.write("\n")
f.write("l = ")
f.write(helligkeit)
f.write("\n")
f.write("a = ")
f.write(alleshell)
f.write("\n")
f.write("v = ")
f.write(geschwindigkeit/100)
f.write("\n")

f.close()

print('<head>')
print('<title>Values saved - you can return to main site</title>')
print('</head>')
print('<body>')
print('<h2><font face="verdana">Values saved - you can return to main site</font></h2>')
print('<h2><font face="verdana">You might need to restart the running Mode</font></h2>')
print('<a href="http://raspberrypi/clock_index.html"><font face="verdana">Return to main site.</font></a>')
print('</body>')
print('</html>')
