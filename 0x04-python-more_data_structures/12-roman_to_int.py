#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                     'M': 1000}
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    if len(roman_string) > 0:
        previo = 0
    for letter in roman_string:
        if letter in roman:
            actual = roman[letter]
        else:
            return 'no'
        if previo >= actual:
            result += actual
        else:
            result += actual - (2 * previo)
        previo = actual
    return result
