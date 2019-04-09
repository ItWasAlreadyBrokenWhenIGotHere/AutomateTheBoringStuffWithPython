#!/usr/bin/env python3
"""
Module Docstring to create MS Paint drawing
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
    pyautogui.click()  # click to put drawing program in focus

    distance = 200
    while distance > 0:
        print(distance, 0)
        pyautogui.dragRel(distance, 0, duration=0.1)  # move right
        distance = distance - 25
        print(0, distance)
        pyautogui.dragRel(0, distance, duration=0.1)  # move down
        print(-distance, 0)
        pyautogui.dragRel(-distance, 0, duration=0.1)  # move left
        distance = distance - 25
        print(0, -distance)
        pyautogui.dragRel(0, -distance, duration=0.1)  # move up


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
