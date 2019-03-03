#!/usr/bin/env python3
"""
Module for copying and moving files examples
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import shutil


def main():
    print('To copy file to a new folder:')
    shutil.copy('./spam.txt', './delicious/spam.txt')

    print('To copy and rename file to a new folder:')
    shutil.copy('./spam.txt', './delicious/spamspamspam.txt')

    print('To whole folder and all the content:')
    shutil.copytree('./delicious', './delicious_backup')

    print('To move file to new folder:')
    shutil.move('./delicious_backup/spam.txt', './delicious/walnut')

    print('To rename, use move with new file name:')
    shutil.move('./delicious_backup/spamspamspam.txt', './delicious_backup/spam2.txt')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()