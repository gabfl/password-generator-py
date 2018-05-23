# password-generator-py

[![Build Status](https://travis-ci.org/gabfl/password-generator-py.svg?branch=master)](https://travis-ci.org/gabfl/password-generator-py)

## Description

A lot of people with security in mind will use random characters as passwords like `t.J:YuZcTSB=4z*v`.
[We feel it's secure](https://xkcd.com/936/) because it's complicated. But the password above is as difficult as `abcdefghijkl!123` for a machine to brute force even though it's a lot easier for a user to remember.

This program attempts to create passwords truly difficult for a computer to brute force and easier to remember for a user.

### Each password contains:

 - 3 words from the english dictionary
 - 1 random number placed at a random position
 - Random separators between words and numbers

### It is very secure because...

 - Since words length differ, the password length is unpredictable
 - The separators change randomly
 - The position of the number change randomly
 - There are `32,000` (words) `^3` (number of words) `^10` (separator) `^10` (separator) `^10` (separator) `^1000` (numbers) different combinations possible

## Examples

Here are a few passwords that can be generated:

```
Coaches_Acquires=Dumbbell_908
28=Haziness_Spatulas+Mortals
Knights;Decrypts%Oatcakes_320
Optimise=472+Deterred%Apricots
375+Hazy%Decorate%Ruler
Blotched%Dugout_995;Alkyl
```

## Installation & usage

```bash
$> pip3 install passwordgenerator

$> passwordgenerator
844=Chinless=Jewelry+Consumer
```

## Use within another Python script

```python
>>> from passwordgenerator import pwgenerator

>>> pwgenerator.generate()
'676=Layers*Bugbear_Escapes'
```

## Advanced options

```
passwordgenerator [-h] [-n MIN_WORD_LENGTH] [-x MAX_WORD_LENGTH]
                  [-i MAX_INT_VALUE] [-e NUMBER_OF_ELEMENTS] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -n MIN_WORD_LENGTH, --min_word_length MIN_WORD_LENGTH
                        Minimum length for each word
  -x MAX_WORD_LENGTH, --max_word_length MAX_WORD_LENGTH
                        Maximum length for each word
  -i MAX_INT_VALUE, --max_int_value MAX_INT_VALUE
                        Maximum value for the integer
  -e NUMBER_OF_ELEMENTS, --number_of_elements NUMBER_OF_ELEMENTS
                        Number of elements in the password (ie. 4 = 3 words +
                        1 integer)
  -s, --no_special_characters
                        Do not use special characters
```
