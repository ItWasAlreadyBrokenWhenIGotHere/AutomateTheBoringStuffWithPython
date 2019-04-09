#!/usr/bin/env python3
"""
Character Count app
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import pprint


def main():
    """ Main entry point of the app """
    message = "It was a bright cold day in April, and the clocks were striking thirteen."
    count = {}  # count how many times characters appear in string: e.g. 'r': 12
    for character in message.upper():
        count.setdefault(character, 0)  # set default value 0 for char when first founded
        count[character] = count[character] + 1  # current count + 1

    pprint.pprint(count)
    #form_text = pprint.pformat(count)
    #print(form_text)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
