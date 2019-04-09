#!/usr/bin/env python3
"""
Module for printing dynamic box
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    def boxPrint(symbol, width, height):
        if len(symbol) != 1:
            raise Exception('"Symbol" needs to a string of length 1.')
        if (width < 2) or (height < 2):
            raise Exception('"Width" or "Heigth" needs to be greater or equal to 2.')

        print(symbol * width)

        for i in range(height - 2):
            print(symbol + (' ' * (width - 2)) + symbol)

        print(symbol * width)

    boxPrint('*', 15, 5)
    boxPrint('O', 4, 8)
    #boxPrint('**', 5, 8)
    boxPrint('*', 1, 1)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()