#!/usr/bin/env python3
"""
Module Docstring for example how to scrape text from Word document
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import docx
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """


def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    # main()
    print(getText('E:\\Git\\automation\\document_handling\\documents\\demo.docx'))
