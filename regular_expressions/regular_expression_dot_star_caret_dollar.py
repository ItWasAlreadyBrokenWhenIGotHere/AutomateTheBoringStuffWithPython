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

    print("Find match from the beginning")
    beginsWithHelloRegex = re.compile(r'^Hello')
    print(beginsWithHelloRegex.search("Hello, my phone number is 415-555-1234."))
    print("")

    print("Find pattern match from the end of the string")
    endsWithHelloRegex = re.compile(r'World$')
    print(endsWithHelloRegex.search("Hello World"))
    print("")

    print("Find pattern to start and end with digits")
    allDigitsRegex = re.compile(r'^\d+$')
    print(allDigitsRegex.search("298374982374987239487239874"))
    print("")

    print('Find pattern "(anything)at" anywhere in the string')
    atRegex = re.compile(r'.at')
    print(atRegex.findall("The cat in the hat sat on the flat mat"))
    print("")

    print('Find pattern "(anything x 1 or 2 times)at" anywhere in the string')
    atRegex = re.compile(r'.{1,2}at')
    print(atRegex.findall("The cat in the hat sat on the flat mat"))
    print("")

    print("Find pattern to find names using .*")
    nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
    print(nameRegex.findall("First Name: Al Last Name: Sweigart"))
    print("")

    print("Find pattern using non greedy match (shortest possible match)")
    serve = "<To serve humans> for dinner.>"
    nongreedy = re.compile(r'<(.*?)>')
    print(nongreedy.findall(serve))
    print("")

    print("Find pattern using greedy match (longest possible match)")
    serve = "<To serve humans> for dinner.>"
    greedy = re.compile(r'<(.*)>')
    print(greedy.findall(serve))
    print("")

    # . means any character except new line character
    # to pattern for all possible character, DOTALL parameter needs to be passed
    print("Find pattern using additional DOTALL parameter to match all possible characters")
    prime = "Serve the public trust \nProtect the innocent. \nUpload the law"
    dotStart = re.compile(r'.*', re.DOTALL)
    print(dotStart.search(prime))
    print("")

    print("Find pattern passing additional argument to ignore case")
    book = "Al, why does your programming book talk about RoboCop so much?"
    vowelReqex = re.compile(r'[aeiou]', re.I)
    print(vowelReqex.findall(book))
    print("")


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

