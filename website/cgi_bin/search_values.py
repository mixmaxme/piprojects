#!/usr/bin/python
print("Content-type:text/html\r\n\r\n")
print('<html>')

import cgi, cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
rotwert = form.getvalue('r-wert')
gruenwert = form.getvalue('g-wert')
blauwert = form.getvalue('b-wert')
helligkeit = form.getvalue('h-wert')
alleshell = form.getvalue('a-wert')
geschwindigkeit = form.getvalue('v-wert')

f = open("/home/pi/piprojects/website/cgi_bin/brightness.py", "w+")

f.write("r = ")
f.write(rotwert)
f.write("\n")
f.write("g = ")
f.write(str(gruenwert))
f.write("\n")
f.write("b = ")
f.write(str(blauwert))
f.write("\n")
f.write("l = ")
f.write(str(helligkeit))
f.write("\n")
f.write("a = ")
f.write(str(alleshell))
f.write("\n")
f.write("v = ")
f.write(str(geschwindigkeit))
f.write("\n")

f.close()

print('<head>')
print('<title>Values saved - you can return to main site</title>')
print('</head>')
print('<body>')
print('<h2><font face="verdana">Values saved - you can return to main site'</font></h2>')
print('<h2><font face="verdana">You might need to restart the running Mode</font></h2>')
print('<a href="http://raspberrypi/clock_index.html"><font face="verdana">Return to main site.</font></a>')
print('</body>')
print('</html>')
