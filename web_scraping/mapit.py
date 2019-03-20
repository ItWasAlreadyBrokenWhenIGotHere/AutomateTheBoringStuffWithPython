#!/usr/bin/env python3
"""
Module for example to open Google Maps with address provided as a arguments
e.g. python mapit.py 870 Valencia St.
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import webbrowser, sys, pyperclip
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    sys.argv  # ['mapit.py, '870', Valencia', 'St.']
    # Check if command line arguments were passed
    if len(sys.argv) > 1:
        # ['mapit.py', '870', Valencia', 'St.' -> '870 Valencia St.']
        address = ' '.join(sys.argv[1:])
    else:
        # if user have not provide address as input arguments
        # we assume that address is in clipboard, so we just paste it to browser using pyperclip
        address = pyperclip.paste()

    # https://www.google.com/maps/place/<ADDRESS>
    webbrowser.open('https://www.google.com/maps/place/' + address)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
