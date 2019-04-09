#!/usr/bin/env python3
"""
Module Docstring for example how to control keyboard from Python
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
    pyautogui.click()  # to activate windows, we need to click mouse
    pyautogui.typewrite('Hello World')  # send key strokes to active window

    pyautogui.typewrite('This is in slower interval', interval=0.2)  # slower interval

    pyautogui.typewrite(['enter', 'a', 'b', 'left', 'left', 'X', 'Y'], interval=0.5)  # send chars and left keys

    pyautogui.press('f1')  # to send single key

    pyautogui.hotkey('ctrl', 's')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()