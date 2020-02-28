#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
searchterm1 = form.getvalue('r-wert')
searchterm2 = form.getvalue('g-wert')
searchterm3 = form.getvalue('b-wert')

f = open("/var/www/html/valueoutput.txt", "w+")
f.write(searchterm1)
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
