#!/usr/bin/python
print('Content-type: text/html\n')

import cgitb #
cgitb.enable() #These 2 lines will allow error messages to appear on a web page in the browser

import cgi

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""




data = cgi.FieldStorage()
name = 'hi'
if ('name' in data):
    name = data['name'].value
bgcolor = 'DarkSeaGreen'
if ('bgcolor' in data):
    bgcolor = data['bgcolor'].value

html= HTML_HEADER
html+= '<body style="background-color: '
html+= '<h1>' + name + '</h1>'
html+= bgcolor + ';">'
html+= '<br><a href="final_project/form.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
