#!/usr/bin/env python3
"""
Module to demonstrate debugger functionality
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    print('Enter the first number to add:')
    first = input()
    print('Enter the second number to add:')
    second = input()
    print('Enter the third number to add:')
    third = input()
    print('The sum is ' + first + second + third)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()