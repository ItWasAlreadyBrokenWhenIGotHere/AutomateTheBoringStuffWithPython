#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='fractorial.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)  # This disable all logs as CRITICAL level is highest

def main():
    """ Main entry point of the app """
    logging.debug('Start of program')
    def factorial(n):
        logging.debug('Start of fractorial (%s)' % (n))
        total = 1
        for i in range(1, n + 1): # BUG: for i in range(n + 1): -> as range start from 0
            total *= i
            logging.info('i is %s, total is %s' % (i, total))

        logging.debug('Return value is %s' % (total))
        return total

    print(factorial(5))

    logging.debug('End of program')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()