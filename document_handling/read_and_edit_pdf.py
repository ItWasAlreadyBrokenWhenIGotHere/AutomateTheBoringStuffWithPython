#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import PyPDF2
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    logging.debug('Start of the Main entry point...')
    os.chdir('./documents')
    pdfFile = open('meetingminutes1.pdf', 'rb')  # PDF files needs to be opened in read-binary "rb" mode
    reader = PyPDF2.PdfFileReader(pdfFile)  # binary file object is passed to PyPDF2
    pageCount = reader.numPages
    page = reader.getPage(0)
    pageContent = page.extractText()
    print(pageCount)
    print(pageContent)

    # for printing content from all the pages
    for pageNum in range(reader.numPages):
        print(reader.getPage(pageNum).extractText())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
