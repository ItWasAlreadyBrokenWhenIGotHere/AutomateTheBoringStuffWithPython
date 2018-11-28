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

    print("Find match + word after match")
    namesRegex = re.compile(r'Agent \w+')
    print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
    print("")

    print("Find and replace match + word after match")
    namesRegex = re.compile(r'Agent \w+')
    print(namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))
    print("")

    print("Find and replace match + part of the word after match")
    namesRegex = re.compile(r'Agent (\w)\w*')
    print(namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))
    print("")

    print("Verbose - multiline string")
    multilineRegex = re.compile(r'''
    (\d\d\d-)|    # area code (without parens, with dash
    (\(\d\d\d\) ) # -or- area code with parend and no dash
    -         # first dash
    \d\d\d    # first 3 digits
    -         # second dash
    \d\d\d\d  # last 4 digits''', re.VERBOSE)
    print(multilineRegex)
    print("")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

