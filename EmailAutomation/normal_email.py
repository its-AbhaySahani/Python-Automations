import imaplib
import email

imap_server = 'imap.gmail.com'
imap_username = 'youremail@gmail.com'
imap_password = 'yourpassword'

with imaplib.IMAP4_SSL(imap_server) as imap:
    imap.login(imap_username, imap_password)
    imap.select('inbox')
    _, data = imap.search(None, 'ALL')
    latest_email_id = data[0].split()[-1]
    _, message_data = imap.fetch(latest_email_id, '(BODY.PEEK[HEADER])')
    message = email.message_from_bytes(message_data[0][1])
    subject = message['Subject']
    sender = message['From']
    print(f'Subject: {subject}')
    print(f'Sender: {sender}')