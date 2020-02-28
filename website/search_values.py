import cgi
form = cgi.FieldStorage()
searchterm = form.getvalue('r-wert')

print(searchterm)
