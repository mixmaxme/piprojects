#!/usr/bin/env python
import cgi
form = cgi.FieldStorage()
searchterm1 = form.getvalue('r-wert')
searchterm2 = form.getvalue('g-wert')
searchterm3 = form.getvalue('b-wert')

f = open("/var/www/html/valueoutput.txt", "w+")
f.write("Hallo")
f.close()
