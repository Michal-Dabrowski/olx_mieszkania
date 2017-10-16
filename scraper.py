# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from config import CITY

class OLXScraper:

    def __init__(self):
        self.session = requests.session()
        self.session.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'})

    def get_url(self, url):
        request = self.session.get(url)
        response = request.content
        return response

    def create_soup(self, response):
        soup = BeautifulSoup(response)
        return soup

    def find_offers(self, soup):
        offers = soup.find_all('tr', class_='wrap')
        return offers

    def get_details(self, offer):
        price = self.get_price(offer)
        name, link = self.get_name_and_link(offer)
        location = self.get_location(offer)
        date = self.get_date(offer)
        id = self.get_olx_id(offer)
        return {'price': price, 'name': name, 'link': link, 'location': location, 'date': date, 'olx_id': id}

    def get_price(self, offer):
        price = offer.find('p', class_='price')
        price = self.get_text(price)
        price = price.replace(' ', '')
        price = price.replace('zł', '')
        return int(price)

    def get_name_and_link(self, offer):
        name = offer.find(class_='marginright5 link linkWithHash detailsLink')
        if not name:
            name = offer.find(class_='marginright5 link linkWithHash detailsLinkPromoted')
        link = name.get('href')
        name = self.get_text(name)
        return name, link

    def get_location(self, offer):
        location = offer.find(class_='color-9 lheight16 marginbott5')
        location = self.get_text(location)
        return location

    def get_date(self, offer):
        date = offer.find(class_='color-9 lheight16 marginbott5 x-normal')
        date = self.get_text(date)
        return date

    def get_text(self, offer):
        text = offer.text
        text = text.strip()
        return text

    def get_olx_id(self, offer):
        id = offer.contents[1].contents[1].get('data-id')
        return int(id)

    def get_offers(self):
        url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/' + CITY + '/'
        response = self.get_url(url)
        soup = self.create_soup(response)
        raw_offers = self.find_offers(soup)

        offers = []
        for raw_offer in raw_offers:
            offers.append(self.get_details(raw_offer))
        return offers
