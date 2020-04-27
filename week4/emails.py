
#!/usr/bin/env python3

import smtplib
import mimetypes
import os.path
import email.message


def generate_email(sender,receipt,sub,body,attach):
    msg = email.message.EmailMessage()
    msg['From'] = sender
    msg['To'] = receipt
    msg['Subject'] = sub
    msg.set_content(body)
    attachment=os.path.basename(attach)
    mime_type, _ = mimetypes.guess_type(attach)
    mime_type,mime_subtype=mime_type.split('/',1)
    with open(attach,'rb') as ap:
       msg.add_attachment(ap.read,maintype=mime_type, subtype=mime_subtype, filename=attachment_filename)
    return msg

def send_email(msg):
    mail_server=smtplib.SMTP('localhost')
    mail_server.send_message(msg)
    mail_server.quit()
