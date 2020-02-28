#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
searchterm1 = form.getvalue('r-wert')
searchterm2 = form.getvalue('g-wert')
searchterm3 = form.getvalue('b-wert')
print(searchterm1,searchterm2,searchterm3)
