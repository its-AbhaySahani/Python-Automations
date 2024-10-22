import imaplib
import email
import csv
from email.header import decode_header

# account credentials
username = "EMAIL"
password = "pASS"

imap_url = 'imap.gmail.com'

def clean_text(text):
    return " ".join([i if ord(i) < 128 else ' ' for i in text])

def fetch_email():
    mail = imaplib.IMAP4_SSL(imap_url)
    mail.login(username, password)

    mail.select('inbox')

    status, messages = mail.search(None, 'ALL')

    email_ids = messages[0].split()

    emails = []

    for mail_id in email_ids[-10]:
        status, msg_data = mail.fetch(mail_id, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # decode the email subject
                subject, encoding = decode_header(msg['Subject'])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else 'utf-8')
                subject = clean_text(subject)

                # decode email sender
                from_ = msg.get("From")
                from_ = clean_text(from_)

                date_ = msg.get("Date")

                # extract email body
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            print(body)
                else:
                    content_type = msg.get_content_type()
                    body = msg.get_payload(decode=True).decode()
                    if content_type == "text/plain":
                        print(body)

                if content_type == "text/plain":    
                    emails.append([date_, from_, subject, body])
    return emails


                

                
