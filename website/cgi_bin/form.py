#!/usr/bin/python
print("Content-Type: text/html")    
print()                             
 
import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
name = form.getvalue('fname')

f = open("/home/pi/piprojects/website/cgi_bin/brightness.py", "w+")
f.write("r = ")
f.write(name)
f.close()

print("Name of the user is:",name)

