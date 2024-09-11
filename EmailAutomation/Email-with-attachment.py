import smtplib
"""
This script sends an email with an attachment using the smtplib and email libraries.
Modules:
    smtplib: Defines an SMTP client session object that can be used to send mail.
    email.mime.multipart: Defines the MIMEMultipart class, which represents a multipart MIME message.
    email.mime.text: Defines the MIMEText class, which represents text MIME objects.
    email.mime.application: Defines the MIMEApplication class, which represents application MIME objects.
Configuration:
    smtp_server (str): The SMTP server address.
    smtp_port (int): The port to use for the SMTP server.
    smtp_username (str): The username for the SMTP server.
    smtp_password (str): The password for the SMTP server.
    from_email (str): The sender's email address.
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body text of the email.
Usage:
    This script reads a PDF file named 'report.pdf' from the current directory and attaches it to the email.
    It then sends the email to the specified recipient using the provided SMTP server credentials.
Example:
    To use this script, update the smtp_username, smtp_password, from_email, and to_email variables with
    appropriate values. Ensure that 'report.pdf' is present in the current directory.
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'youremail@gmail.com'
smtp_password = 'yourpassword'

from_email = 'youremail@gmail.com'
to_email = 'recipient@example.com'
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

