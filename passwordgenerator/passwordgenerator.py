#!/usr/bin/env python3

# Author: Gabriel Bordeaux (gabfl)
# Github: https://github.com/gabfl/password-generator-py
# Version: 1.0.1
# Compatible with python 2.7 & 3

from random import randint, choice
import os

class PasswordGenerator:

    def __init__(self):
        # Set default vars
        self.numberOfElements = 4; # 4 = 3 words + 1 integer
        self.maxInt = 1000; # Maximum value for the integer
        self.separators = ('-', '_', ':', ';', '.', '=', '+', '%', '*'); # List of available separators
        self.maxWordLength = 8; # Maximum characters per word

        # Call initial methods
        self.loadDictionary();
        self.setIntPosition();

    def getCurrentDir(self):
        """returns the script directory name to locate the correct dictionary path"""
        return os.path.dirname(os.path.abspath(__file__)) + '/';

    def loadDictionary(self):
        """load dictionary into a list."""
        dicList = [];
        with open(self.getCurrentDir() + "data/english.csv") as f:
            lines = f.readlines();
            # self.dictionary = [line.strip('\n') for line in lines]
            for line in lines:
                word = line.strip('\n');
                if len(word) <= self.maxWordLength:
                    dicList.append(word);
        self.dictionary = tuple(dicList);

    def getRandomWord(self):
        """returns a random word from the dictionary"""
        return choice(self.dictionary);

    def getRandomSeparator(self):
        """returns a random separator"""
        return choice(self.separators);

    def getRandomInt(self):
        """returns a random number between 0 and self.maxInt"""
        return randint(0, self.maxInt);

    def setIntPosition(self):
        """Set the position of the integer in the final password"""
        self.intPosition = randint(0, self.numberOfElements - 1);

    def generate(self):
        """Generate a password"""
        password = '';
        for i in range(self.numberOfElements):
            # Add word or integer
            if i == self.intPosition:
                password += str(self.getRandomInt());
            else:
                password += self.getRandomWord().title();

            # Add separator
            if i != self.numberOfElements - 1:
                password += self.getRandomSeparator();

        return password;

    def __call__(self):
        return self.generate();

def main():
    pw = PasswordGenerator()
    print (pw())

# Generate a password
if __name__ == "__main__":
    main()
