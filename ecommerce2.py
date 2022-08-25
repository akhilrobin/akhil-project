import cgi,cgitb
form=cgi.FieldStorage()
if form.getvalue('mobiles'):
    mobile=form.getvalue('mobiles')
else:
    mobile="not entered"
if form.getvalue('text_content'):
    text_content=form.getvalue('text_content')
else:
    text_content="not entered"
print"content-type:text/html\r\n\r\n" 
print"<html>"
print"<body>"
print"</h2> selected mobile is %s </h2>"%mobile
print"</h2> entered textcontent is %s </h2>"%text_content
print"</body>"
print"</html>"
 

