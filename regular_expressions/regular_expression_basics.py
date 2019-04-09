#!/usr/bin/env python3
"""
Module Docstring for basic regex
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import re


def main():
    """ Main entry point of the app """
    message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 for office number"

    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # r means raw strings which enable \d kind of expressions

    matched_object = phoneNumberRegex.search(message)
    print("First founded: " + matched_object.group())

    matched_object = phoneNumberRegex.findall(message)
    print("All founded: " + str(matched_object))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
