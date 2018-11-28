#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import re


def main():
    """ Main entry point of the app """
    message = "My number is 415-555-1011"

    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    matched_object = phoneNumberRegex.search(message)
    print("First founded: " + matched_object.group())

    phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    matched_object = phoneNumberRegex.search(message)
    print("All groups: " + matched_object.group())
    print("Area code: " + matched_object.group(1))
    print("Phone number: " + matched_object.group(2))

    message = "My number is (415) 555-1011"

    phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
    matched_object = phoneNumberRegex.search(message)
    print("All groups with parentheses: " + matched_object.group())

    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    matched_object = batRegex.search("Batmobile lost a wheel")
    print(matched_object)

    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    matched_object = batRegex.search("Batmotorcycle lost a wheel")
    print("If nothing is founded, python returns: " + str(matched_object))

    batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
    matched_object = batRegex.search("Batmobile lost a wheel")
    print(matched_object.group(1))


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
