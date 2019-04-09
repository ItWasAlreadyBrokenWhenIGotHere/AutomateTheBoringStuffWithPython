#!/usr/bin/env python3
"""
Module Reading and writing files to disk
"""

__author__ = "Petri Weckström"
__version__ = "0.1.0"
__license__ = "MIT"

import shelve


def main():
    """ Main entry point of the app """

    print('Read returns file content:')
    helloFile = open('hello.txt')  # Returns a file object
    fileContent = helloFile.read()
    print(fileContent)
    helloFile.close()

    print('Readlines returns each line content as a list:')
    helloFile = open('hello.txt')
    fileContent = helloFile.readlines()
    print(fileContent)
    helloFile.close()

    print('Write mode will overwrite whole file:')
    helloFile = open('hello2.txt', 'w')
    helloFile.write('Hello!!!!')
    helloFile.close()

    print('Append mode will add text at the end of the file:')
    helloFile = open('hello2.txt', 'a')
    helloFile.write('\nBacon is not a vegetable!')
    helloFile.close()

    print('Binary Shelve method is good way to store more structured data like dictionary or list to a file:')
    shelfFile = shelve.open('mydata')
    shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tal']
    shelfFile.close()

    print('To print Shelve file content of key')
    shelfFile = shelve.open('mydata')
    print(shelfFile['cats'])
    shelfFile.close()

    print('To print Shelve file keys')
    shelfFile = shelve.open('mydata')
    print(list(shelfFile.keys()))
    shelfFile.close()

    print('To print Shelve file values')
    shelfFile = shelve.open('mydata')
    print(list(shelfFile.values()))
    shelfFile.close()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()