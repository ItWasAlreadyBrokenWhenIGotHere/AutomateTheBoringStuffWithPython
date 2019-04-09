#!/usr/bin/env python3
"""
Module for example how to scrape book info from Amazon web store
https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import bs4
import requests

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """

    def getSamsungPrice(productUrl):
        logging.debug('Start of get Samsung price function')
        # some web page needs header information
        # headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', }
        # res = requests.get(Url, headers=headers)
        logging.debug('Open product URL')
        res = requests.get(productUrl)
        res.raise_for_status()  # raise exception if request.get failed
        soup = bs4.BeautifulSoup(res.text, 'html.parser')  # returns beautifulsoup object
        logging.debug('Get price element')
        priceElem = soup.select('#app > div > div.main > div > div > section > aside.product__main-view > div.main-view__info > div:nth-child(1) > div.price-tag > div > div.price-tag-prices > div > span')
        logging.debug('End of get Samsung price function')
        return priceElem[0].text.strip()  # strip is used to trim white spaces and tabs out of the string

    price = getSamsungPrice('https://www.verkkokauppa.com/fi/product/36712/kjsdn/Samsung-C34J791-34-naytto?list=OZZQMqhQhX0hHyOqNQv6b55hZEhRwSEhUIZzZHEYsNxzF29')
    print('Todays price for the Samsung is: ' + price + 'e')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
