#!/usr/bin/env python3

# Author: Gabriel Bordeaux (gabfl)
# Github: https://github.com/gabfl/password-generator-py
# Compatible with python 2.7 & 3

from random import randint, choice
import os, importlib

import argparse

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--min_word_length", type = int, help = "Minimum length for each word", default = 3)
parser.add_argument("-x", "--max_word_length", type = int, help = "Maximum length for each word", default = 8)
parser.add_argument("-i", "--max_int_value", type = int, help = "Maximum value for the integer", default = 1000)
parser.add_argument("-e", "--number_of_elements", type = int, help = "Number of elements in the password (ie. 4 = 3 words + 1 integer)", default = 4)
parser.add_argument("-s", "--no_special_characters",  action='store_true', help = "Do not use special characters")
args = parser.parse_args()

class PasswordGenerator:

    def __init__(self):
        # Set default vars
        self.separators = ('-', '_', ':', ';', '.', '=', '+', '%', '*'); # List of available separators

        # Call initial methods
        self.loadDictionary();
        self.setIntPosition();

    def getCurrentDir(self):
        """
            Returns the script directory name to locate the correct dictionary path
        """

        return os.path.dirname(os.path.abspath(__file__)) + '/';

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
            if len(word) >= args.min_word_length and len(word) <= args.max_word_length:
                break

        return word;

    def getRandomSeparator(self):
        """
            Returns a random separator
        """

        if not args.no_special_characters:
            return choice(self.separators);

        return ''

    def getRandomInt(self):
        """
            Returns a random number between 0 and `args.max_int_value`
        """

        return randint(0, args.max_int_value);

    def setIntPosition(self):
        """
            Set the position of the integer in the final password
        """

        self.intPosition = randint(0, args.number_of_elements - 1);

    def generate(self):
        """
            Generate a password
        """

        password = '';
        for i in range(args.number_of_elements):
            # Add word or integer
            if i == self.intPosition:
                password += str(self.getRandomInt());
            else:
                password += self.getRandomWord().title();

            # Add separator
            if i != args.number_of_elements - 1:
                password += self.getRandomSeparator();

        return password;

    def __call__(self):
        return self.generate();

def main():
    """
        Main method
    """

    pw = PasswordGenerator()
    print (pw())

def generate():
    """
        To use the module within another module
    """

    pw = PasswordGenerator()
    return pw()

# Generate a password
if __name__ == "__main__":
    main()
