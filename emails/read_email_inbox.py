#!/usr/bin/env python3
"""
Module Docstring for reading email from INBOX

Typical IMAP server domain names:
Gmail - imap.gmail.com
Outlook.com/Hotmail.com - imap-mail.outlook.com
Yahoo Mail - imap.mail.yahoo.com
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import pyzmail36
import imapclient
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)  # create connection object
    conn.login('email.address@gmail.com', 'password')  # Returns a byte object
    conn.select_folder('INBOX', readonly=True)  # select folder to read, set read only to prevent accidentally deleting something etc
    UIDs = conn.search(['SINCE 20-Jan-2019'])  # returns list on unique id's
    rawMessage = conn.fetch([UIDs[0]], ['BODY[]', 'FLAGS'])  # returns raw massages of given unique id
    message = pyzmail36.PyzMessage.factory(rawMessage[UIDs[0]][b'BODY[]'])  # returns pyzmail message object
    message.get_subject()
    print('subject: ' + message)
    #message.get_addresses('from')
    #message.get_addresses('to')
    #message.get_addresses('bcc')
    #message.text_part
    #message.html_part
    #message.html_part == None
    message.text_part.get_payload().decode('UTF-8')
    print('payload: ' + message)
    # conn.delete_messages([12345])  # to delete message
    conn.logout()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
