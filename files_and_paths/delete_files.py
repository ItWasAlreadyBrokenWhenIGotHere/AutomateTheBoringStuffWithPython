#!/usr/bin/env python3
"""
Module Docstring for example how to delete files
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import shutil
import send2trash


def main():
    print('To Delete (permanently) single file using os Unlink method:')
    os.unlink('file.name')

    print('To Delete (permanently) empty directory using os remove directory method:')
    os.rmdir('dir_name')

    print('To Delete (permanently) directory with files using shutil remove tree method:')
    shutil.rmtree('dir_name')

    print('To move file or directory to trash, use send2trash method:')
    send2trash.send2trash('file_name_or_dir_name')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()