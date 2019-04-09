#!/usr/bin/env python3
"""
Module for assertion examples
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    market_2nd = {'ns': 'green', 'ew': 'red'}

    def switchLights(intersection):
        for key in intersection.keys():
            if intersection[key] == 'green':
                intersection[key] = 'yellow'
            elif intersection[key] == 'yellow':
                intersection[key] = 'red'
            elif intersection[key] == 'red':
                intersection[key] = 'green'
        assert 'red' in intersection.values(), 'Neither light is red! ' + str(intersection)
        # assert include the rule which needs to always be true, otherwise exception is raised!

    print(market_2nd)
    switchLights(market_2nd)
    print(market_2nd)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()