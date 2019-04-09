#!/usr/bin/env python3
"""
Module Docstring for example how to control mouse from Python
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import pyautogui
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL) # This disable all logs as CRITICAL level is highest


def main():
    """ Main entry point of the app """
    print(pyautogui.size())  # prints resolution
    width, height = pyautogui.size()  # assign resolution to variables

    print(pyautogui.position())  # returns current position of the mouse

    pyautogui.moveTo(10, 10)  # move mouse
    pyautogui.moveTo(400, 400, duration=2.5)  # move mouse in slower pace (duration in seconds)

    pyautogui.moveRel(200, 0)  # moves mouse from its current position to relative position
    pyautogui.moveRel(200, 0, duration=1.5)  # moves mouse from its current position to relative position

    pyautogui.moveRel(0, -100, duration=1)  # moves up

    pyautogui.click(53, 44)  # to click something
    pyautogui.doubleClick(41, 538)  # double click something


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()