#!/usr/bin/env python3
"""
Module Docstring for example how to control browser from Python
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

from selenium import webdriver

import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    logging.debug('Start of Selenium Browser control')
    browser = webdriver.Chrome(executable_path='E:/Git/automation/web_scraping/chromedriver.exe')
    logging.debug('Open www.google.com')
    browser.get('https://www.google.com')
    # element for the search field
    searchElem = browser.find_element_by_css_selector('#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input')
    searchElem.send_keys('cat video')
    searchElem.submit()
    time.sleep(5)  # Delays for 5 seconds. You can also use a float value.
    browser.back()
    time.sleep(2)
    browser.quit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
