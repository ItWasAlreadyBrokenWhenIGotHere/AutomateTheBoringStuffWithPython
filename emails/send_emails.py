#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import smtplib
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()  # call hello method
    conn.starttls()  # start TLS connection to send credentials
    conn.login('user.name', 'password') # call login method
    # two new line char indicates that we are done with the header
    #conn.sendmail('from.address@gmail.com', 'to.address@gmail.com', 'Subject: So long...\n\nDear Stranger, \nSo long, and thanks for all the fish\n\n-Stranger')
    conn.quit()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
