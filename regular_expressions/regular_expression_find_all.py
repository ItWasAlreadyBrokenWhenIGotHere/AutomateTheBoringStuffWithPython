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

    print(".findall is used to find all matches, it returns regular list")
    phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneRegex.findall("My phone number is 415-555-1234. Call me tomorrow or at the office 415-444-1234.")
    print(mo)
    print("")

    print("if regex have groups .findall returns list of tuples")
    phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneRegex.findall("My phone number is 415-555-1234. Call me tomorrow or at the office 415-444-1234.")
    print(mo)
    print("")


    lyrics = "12 drummers drumming, 11 pipers piping, 10 lords a-leaping, 9 ladies dancing, 8 maids a-milking, " \
             "7 swans a-swimming, 6 geese a-laying, 5 gold rings, 4 calling birds, 3 french hans, " \
             "2 turtle doves and 1 partridge in a pear tree"
    print("find number and text patterns from lyrics - 1st iteration")
    xmasRegex = re.compile(r'\d+\s\w+')
    print(xmasRegex.findall(lyrics))
    print("")

    print("Testing own character class to find vowel")
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    print(vowelRegex.findall("Robocop eats baby food."))
    print("")

    print("To find two vowels in a row")
    doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
    print(doubleVowelRegex.findall("Robocop eats baby food."))
    print("")

    print("Negative character class for consonants")
    consonantsRegex = re.compile(r'[^aeiouAEIOU]')
    print(consonantsRegex.findall("Robocop eats baby food."))
    print("")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

