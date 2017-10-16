# -*- coding: utf-8 -*-

from scraper import OLXScraper
from database import get_offers, update_offers_table
from send_mail import create_email_content, send_email
from config import SMTP_SERVER, PORT, SERVER_LOGIN, SERVER_PASSWORD, SENDER, RECEIVERS, SUBJECT, MAX_PRICE

if __name__ == '__main__':
    scraper = OLXScraper()
    offers = scraper.get_offers()
    update_offers_table(offers)
    offers = get_offers(max_price=MAX_PRICE)
    content = create_email_content(offers)
    send_email(
        smtp_server=SMTP_SERVER,
        port=PORT,
        server_login=SERVER_LOGIN,
        server_password=SERVER_PASSWORD,
        sender=SENDER,
        receivers=RECEIVERS,
        message=content,
        subject=SUBJECT
    )