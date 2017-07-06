# password-generator-py

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

```
$> pip3 install passwordgenerator

$> passwordgenerator
844=Chinless=Jewelry+Consumer
```

## Use within another Python script

```
from passwordgenerator import passwordgenerator

p = passwordgenerator.PasswordGenerator()
print(p())
```
