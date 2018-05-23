#!/usr/bin/env python3

# Author: Gabriel Bordeaux (gabfl)
# Github: https://github.com/gabfl/password-generator-py
# Compatible with python 2.7 & 3

from random import randint, choice
import os
import importlib

import argparse


def load_dictionary():
    """
        Load dictionary.
    """

    # Get module
    module = importlib.import_module('passwordgenerator.data.english')

    # Save env dict in the global scope
    return getattr(module, 'dictionary')


def get_random_word(dictionary, min_word_length=3, max_word_length=8):
    """
        Returns a random word from the dictionary
    """

    while True:
        # Choose a random word
        word = choice(dictionary)
        # Stop looping as soon as we have a valid candidate
        if len(word) >= min_word_length and len(word) <= max_word_length:
            break

    return word


def get_random_separator(no_special_characters=False):
    """
        Returns a random separator
    """

    # List of available separators
    separators = ('-', '_', ':', ';', '.', '=', '+', '%', '*')

    if not no_special_characters:
        return choice(separators)

    return ''


def get_random_int(max_int_value):
    """
        Returns a random number between 0 and `max_int_value`
    """

    return randint(0, max_int_value)


def set_int_position(number_of_elements):
    """
        Set the position of the integer in the final password
    """

    return randint(0, number_of_elements - 1)


def pw(min_word_length=3, max_word_length=8, max_int_value=1000, number_of_elements=4, no_special_characters=False):
    """
        Generate a password
    """

    # Set the position of the integer
    int_position = set_int_position(number_of_elements)

    # Load dictionary
    dictionary = load_dictionary()

    password = ''
    for i in range(number_of_elements):
        # Add word or integer
        if i == int_position:
            password += str(get_random_int(max_int_value))
        else:
            password += get_random_word(dictionary,
                                        min_word_length,
                                        max_word_length).title()

        # Add separator
        if i != number_of_elements - 1:
            password += get_random_separator(no_special_characters)

    return password


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

    # Print a password
    print(pw(min_word_length=args.min_word_length,
             max_word_length=args.max_word_length,
             max_int_value=args.max_int_value,
             number_of_elements=args.number_of_elements,
             no_special_characters=args.no_special_characters))


def generate():
    """
        To use the module within another module
    """

    return pw()


# Generate a password
if __name__ == "__main__":
    main()
