#!/usr/bin/env python3
"""
Module Docstring for example how to move in the file ssystem
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import shutil


def main():
    print('To handle directory and sub-directory files:')
    for folderName, subfolders, filenames in os.walk('/Users/petriweckstrom/git/automation/files_and_paths/delicious/'):
        print('The folder is ' +folderName)
        print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
        print('The file names in ' + folderName + ' are: ' + str(filenames))
        print()

        # From here you can extend the functionality as you wish, e.g.
        """ for subfolder in subfolders:
            if 'fish' in subfolders:
                os.rmdir(subfolder) """

        # or e.g. rename files like
        """ for file in filenames:
            if file.endswith('.py'):
                shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup')) """


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
