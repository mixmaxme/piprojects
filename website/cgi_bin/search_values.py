#!/usr/bin/env python
import cgi, cgitb

form = cgi.FieldStorage()
rotwert = form.getvalue('r-wert')
gruenwert = form.getvalue('g-wert')
blauwert = form.getvalue('b-wert')
helligkeit = form.getvalue('h-wert')
alleshell = form.getvalue('a-wert')
geschwindigkeit = form.getvalue('v-wert')

f = open("/home/pi/piprojects/website/brightness.py", "w+")

f.write("r = ")
f.write(str(rotwert))
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

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Hello World - First CGI Program</title>')
print('</head>')
print('<body>')
print('<h2>Hello Word! This is my first CGI program</h2>')
print('</body>')
print('</html>')
