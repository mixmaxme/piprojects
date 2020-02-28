#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
searchterm1 = form.getvalue('r-wert')
searchterm2 = form.getvalue('g-wert')
searchterm3 = form.getvalue('b-wert')

f = open("/home/pi/piprojects/valueoutput.txt","w+")
f.write("r = "searchterm1)
f.write("g = "searchterm1)
f.write("b = "searchterm1)
f.close()
