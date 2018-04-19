#!/usr/bin/env python3

# Author: Gabriel Bordeaux (gabfl)
# Github: https://github.com/gabfl/password-generator-py
# Compatible with python 2.7 & 3

from random import randint, choice
import os
import importlib

import argparse


class PasswordGenerator:

    def __init__(self, argparse=True):
        # Set default vars
        self.separators = ('-', '_', ':', ';', '.', '=', '+',
                           '%', '*')  # List of available separators

        # Define options
        self.setOptions(argparse)

        # Call initial methods
        self.loadDictionary()
        self.setIntPosition()

    def setOptions(self, argparse):
        """
            Set options either with argsparse or with a default
        """

        # Define options
        self.options = {}
        if argparse:
            self.options['min_word_length'] = args.min_word_length
            self.options['max_word_length'] = args.max_word_length
            self.options['max_int_value'] = args.max_int_value
            self.options['number_of_elements'] = args.number_of_elements
            self.options['no_special_characters'] = args.no_special_characters
        else:
            self.options['min_word_length'] = 3
            self.options['max_word_length'] = 8
            self.options['max_int_value'] = 1000
            self.options['number_of_elements'] = 4
            self.options['no_special_characters'] = False

    def getCurrentDir(self):
        """
            Returns the script directory name to locate the correct dictionary path
        """

        return os.path.dirname(os.path.abspath(__file__)) + '/'

    def loadDictionary(self):
        """
            Load dictionary.
        """

        # Get module
        module = importlib.import_module('passwordgenerator.data.english')

        # Save env dict in the global scope
        self.dictionary = getattr(module, 'dictionary')

    def getRandomWord(self):
        """
            Returns a random word from the dictionary
        """

        while True:
            # Choose a random word
            word = choice(self.dictionary)
            # Stop looping as soon as we have a valid candidate
            if len(word) >= self.options['min_word_length'] and len(word) <= self.options['max_word_length']:
                break

        return word

    def getRandomSeparator(self):
        """
            Returns a random separator
        """

        if not self.options['no_special_characters']:
            return choice(self.separators)

        return ''

    def getRandomInt(self):
        """
            Returns a random number between 0 and `self.options['max_int_value']`
        """

        return randint(0, self.options['max_int_value'])

    def setIntPosition(self):
        """
            Set the position of the integer in the final password
        """

        self.intPosition = randint(0, self.options['number_of_elements'] - 1)

    def generate(self):
        """
            Generate a password
        """

        password = ''
        for i in range(self.options['number_of_elements']):
            # Add word or integer
            if i == self.intPosition:
                password += str(self.getRandomInt())
            else:
                password += self.getRandomWord().title()

            # Add separator
            if i != self.options['number_of_elements'] - 1:
                password += self.getRandomSeparator()

        return password

    def __call__(self):
        return self.generate()


def main():
    """
        Main method
    """

    # Options
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--min_word_length", type=int,
                        help="Minimum length for each word", default=3)
    parser.add_argument("-x", "--max_word_length", type=int,
                        help="Maximum length for each word", default=8)
    parser.add_argument("-i", "--max_int_value", type=int,
                        help="Maximum value for the integer", default=1000)
    parser.add_argument("-e", "--number_of_elements", type=int,
                        help="Number of elements in the password (ie. 4 = 3 words + 1 integer)", default=4)
    parser.add_argument("-s", "--no_special_characters",
                        action='store_true', help="Do not use special characters")
    args = parser.parse_args()

    # Genrate a password
    pw = PasswordGenerator()

    print(pw())


def generate():
    """
        To use the module within another module
    """

    pw = PasswordGenerator(False)
    return pw()


# Generate a password
if __name__ == "__main__":
    main()
