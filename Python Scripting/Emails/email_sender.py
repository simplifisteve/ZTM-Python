import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

# # Python Email Sender Template
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Python Master'
email['to'] = 'example@gmail.com'
email['subject'] = 'Test email from Python Scripting'

email.set_content(html.substitute(name='Qoobee'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'App Password')
    smtp.send_message(email)
    print('Email sent!')
