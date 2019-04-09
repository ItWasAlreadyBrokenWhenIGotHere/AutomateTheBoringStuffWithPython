#!/usr/bin/env python3
"""
Module Docstring for logging example
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest
"""
Log Levels:
debug (lowest)
info
warning
error
critical (highest)
"""

def main():
    """ Main entry point of the app """
    print("hello world")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()