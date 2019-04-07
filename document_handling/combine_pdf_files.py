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
    pdf1File = open('meetingminutes1.pdf', 'rb')  # PDF files needs to be opened in read-binary "rb" mode
    pdf2File = open('meetingminutes2.pdf', 'rb')  # PDF files needs to be opened in read-binary "rb" mode
    reader1 = PyPDF2.PdfFileReader(pdf1File)  # binary file object is passed to PyPDF2
    reader2 = PyPDF2.PdfFileReader(pdf2File)  # binary file object is passed to PyPDF2

    # loop trough each pdf files and add every page from those to new pdf document
    writer = PyPDF2.PdfFileWriter()
    logging.debug('Add pages from 1st pdf')
    for pageNum in range(reader1.numPages):
        page = reader1.getPage(pageNum)
        writer.addPage(page)

    logging.debug('Add pages from nd pdf')
    for pageNum in range(reader2.numPages):
        page = reader2.getPage(pageNum)
        writer.addPage(page)

    # save pdf file content from writer to actual file
    logging.debug('Save content to new file and close all files')
    outputFile = open('combinedminutes.pdf', 'wb')  # again, binary mode is required for pdf
    writer.write(outputFile)
    outputFile.close()
    pdf1File.close()
    pdf2File.close()



if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
