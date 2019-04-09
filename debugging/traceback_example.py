#!/usr/bin/env python3
"""
Module Docstring for traceback example

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import traceback


def main():
    """ Main entry point of the app """
    try:
        raise Exception('This is the error message.')
    except:
        errorFile = open('error_log.txt', 'a')
        errorFile.write(traceback.format_exc())
        errorFile.close()
        print('The traceback info was written to error_log.txt')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()