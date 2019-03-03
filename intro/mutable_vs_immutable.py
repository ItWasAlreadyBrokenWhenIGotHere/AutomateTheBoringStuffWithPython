#!/usr/bin/env python3
"""
Mutable (lists) vs immutable (strings, tuples)
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import copy


def main():
    """ Main entry point of the app """
    # immutable's like: int, float, bool, str, tuple, unicode
    spam = 42
    cheese = spam
    spam = 100
    print(spam)
    print(cheese)

    # mutable's like: list, set, dict
    spam1 = [0, 1, 2, 3, 4, 5]
    cheese1 = spam1
    cheese1[1] = "Hello"
    # both has now same value as they are references to same list
    print(cheese1)
    print(spam1)

    # to copy list, you need to use deecopy from copy
    spam2 = ['A', 'B', 'C', 'D']
    cheese2 = copy.deepcopy(spam2)
    cheese2[1] = 42
    print(spam2)
    print(cheese2)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
