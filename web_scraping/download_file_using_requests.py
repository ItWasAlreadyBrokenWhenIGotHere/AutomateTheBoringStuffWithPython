#!/usr/bin/env python3
"""
Module Docstring for example how to download a file from Python
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import requests

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    print(res.status_code)
    print(res.text[:500])  # prints 500 characters from the file (Romeo and Juliet)

    # Example about bad request and how to show error using raise_for_status
    #badRes = requests.get('https://automatetheboringstuff.com/kjdfnksdjndfkajn')
    #badRes.raise_for_status()

    # To write response to file
    playFile = open('RomeoAndJuliet.txt', 'wb')  # content needs to be written in binary mode (wb)
    for chunk in res.iter_content(100000): # writing is done in iterations of 100000 char per loop
        playFile.write(chunk)

    playFile.close()


if __name__ == "__main__":
    main()
