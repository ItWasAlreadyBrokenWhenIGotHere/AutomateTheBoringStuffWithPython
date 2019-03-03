#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import os


def main():
    """ Main entry point of the app """
    print("os separator:")
    print(os.sep)
    print("")

    print("current working directory:")
    print(os.getcwd())
    print("")

    print("change reference of current working directory:")
    os.chdir('/Users/petriweckstrom/git/automation/')
    print(os.getcwd())
    print("")

    print("parse os independent folders and file path:")
    print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
    print("")

    print("to get absolute path of file in current directory:")
    print(os.path.abspath('spam.png'))
    print("")

    print("to get relative path between two folders:")
    print(os.path.relpath('/dir1/dir2/dir3/spam.png', '/dir1/dir2'))
    print("")

    print("to get directory name:")
    print(os.path.dirname('/dir1/dir2/dir3/spam.png'))
    print("")

    print("to get only filename:")
    print(os.path.basename('/dir1/dir2/dir3/spam.png'))
    print("")

    print("to test if file exist:")
    print(os.path.exists('/dir1/dir2/dir3/spam.png'))
    print("")

    print("to test if file exist:")
    print(os.path.isfile('/dir1/dir2/dir3/spam.png'))
    print("")

    print("to test if folder exist:")
    print(os.path.isdir('/Users/'))
    print("")

    print("to get file size:")
    print(os.path.getsize('/Users/petriweckstrom/git/automation/files_and_paths/filenames_and_paths.py'))
    print("")

    print("to list of folders and file names:")
    print(os.listdir('/Users/petriweckstrom/git/automation/files_and_paths/'))
    print("")

    print("to calculate combined file sized of directory:")
    totalSize = 0
    for filename in os.listdir('/Users/petriweckstrom/git/automation/files_and_paths/'):
        if not os.path.isfile(os.path.join('/Users/petriweckstrom/git/automation/files_and_paths/', filename)):
            continue
        totalSize = totalSize + os.path.getsize(os.path.join('/Users/petriweckstrom/git/automation/files_and_paths/', filename))

    print(totalSize)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()