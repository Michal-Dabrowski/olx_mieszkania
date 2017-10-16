# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from database import session

def create_email_content(offers):
    content = ''
    if not offers:
        return None
    for offer in offers:
        content += '{} | {}zł | {} | {} | {}\n\n'.format(offer.name, offer.price, offer.location, offer.date, offer.link)
        offer.archive = True
        session.add(offer)
    session.commit()
    return content
        
def send_email(smtp_server, port, server_login, server_password, sender, receivers, message, subject):
    if message:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.login(server_login, server_password)
        subject = subject
        body = MIMEText(message, _charset="UTF-8")
        body['Subject'] = Header(subject, "utf-8")
        body['To'] = ', '.join(receivers)
        body['From'] = sender
        server.sendmail(sender, receivers, body.as_string())
        server.close()
        print("Successfully sent email")
