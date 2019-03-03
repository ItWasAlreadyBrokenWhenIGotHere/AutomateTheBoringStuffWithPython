#!/usr/bin/env python3
"""
Module for listing directory files and directories and total size of files
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import os


def main():
    """ Main entry point of the app """

    def print_dir_info(base_dir):
        print("to list of folders and file names:")
        print(os.listdir(base_dir))
        print("")

        print("to calculate combined file sized of directory:")
        totalSize = 0
        for filename in os.listdir(base_dir):
            if not os.path.isfile(os.path.join(base_dir, filename)):
                continue
            totalSize = totalSize + os.path.getsize(
                os.path.join(base_dir, filename))
        print(totalSize)

    base_dir = input("Enter base dir: >>> ")
    print_dir_info(base_dir)
    """ e.g: /Users/petriweckstrom/git/automation/files_and_paths/ """


if __name__ == "__main__":
    main()
