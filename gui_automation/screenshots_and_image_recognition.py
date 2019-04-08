#!/usr/bin/env python3
"""
Module Docstring
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
    pyautogui.screenshot('E:\\Git\\automation\\gui_automation\\screenshot_example.png')  # take and save screen shot
    pyautogui.locateOnScreen('E:\\Git\\automation\\gui_automation\\calc7key.png')  # locate sub image from screen
    pyautogui.locateCenterOnScreen('E:\\Git\\automation\\gui_automation\\calc7key.png')  # returns center coordinates of sub image from the screen
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
