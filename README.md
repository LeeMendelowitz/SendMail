# Send Mail #

A simple Python script for sending e-mails. This has been tested with G-Mail. 

# Usage #

```{python}  
import send_mail
import smtplib

# Initialize SMTP server
username = "username"
password = "password"
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

html_msg = """<html>
<body>
<p>How are you?</p>
</body>
</html>
"""

text_msg = "How are you?"

send_mail.send(fromaddr="Lee.Mendelowitz@gmail.com",
               toaddr="you@mailinator.com",
               subject="Hi",
               text_msg = text_msg,
               html_msg = html_msg
               )
```