import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'abhay.cs.777@gmail.com'
smtp_password = 'password'

from_email = 'abhay.cs.777@gmail.com'
to_email = 'abhay.12115826@lpu.in'
subject = 'Email with attachment'
body = 'Please find attached the report.'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject
msg.attach(MIMEText(body))

with open('report.pdf', 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='pdf')
    attachment.add_header('Content-Disposition', 'attachment', filename='report.pdf')
    msg.attach(attachment)

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.send_message(msg)

