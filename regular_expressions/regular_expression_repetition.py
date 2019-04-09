#!/usr/bin/env python3
"""
Module Docstring for example how to regular expression examples
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import re


def main():
    """ Main entry point of the app """

    print("? means that content can appear 0 - 1 times")
    batRegex = re.compile(r'Bat(wo)?man')  # find batman or batwoman -
    mo = batRegex.search("The Adventures of Batwoman")
    print(mo.group())
    print("")

    phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
    mo = phoneRegex.search("My phone number is 415-555-1234. Call me tomorrow.")
    print(mo.group())
    mo = phoneRegex.search("My phone number is 555-1234. Call me tomorrow.")
    print(mo.group())
    print("")

    print("* means that content can appear 0 - n times. To find * chat, use \*")
    batRegex = re.compile(r'Bat(wo)*man')
    mo = batRegex.search("The Adventures of Batwowowowoman")
    print(mo.group())
    print("")

    print("+ means that content can appear 1 - n times.")
    batRegex = re.compile(r'Bat(wo)+man')
    mo = batRegex.search("The Adventures of Batman")
    print(mo)
    mo = batRegex.search("The Adventures of Batwowoman")
    print(mo)
    print("")

    print("escape characters")
    regex = re.compile(r'\+\*\?')
    mo = regex.search("I learned about +*? regex syntax")
    print(mo)
    print("")

    print("escape characters, same as above with repetition")
    regex = re.compile(r'(\+\*\?)+')
    mo = regex.search("I learned about +*?+*?+*?+*?+*? regex syntax")
    print(mo)
    print("")

    print("{x} to specify how many occurrence needs to be found")
    haRegex = re.compile(r'(Ha){3}')
    mo = haRegex.search("I learned about HaHaHa regex syntax")
    print(mo)
    haRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
    mo = haRegex.search("My numbers are 415-555-1234,555-4242,212-555-0000")
    print(mo)
    print("")

    print("{x,y} to specify range of how many occurrence needs to be found. This is greedy match")
    haRegex = re.compile(r'(Ha){3,5}')
    mo = haRegex.search("I learned about HaHaHaHa regex syntax")
    print(mo)
    print("")

    print("{x,y}? to specify range of how many occurrence needs to be found. This returns shortest match")
    haRegex = re.compile(r'(\d){3,5}?')
    mo = haRegex.search("1234567890")
    print(mo)
    print("")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
