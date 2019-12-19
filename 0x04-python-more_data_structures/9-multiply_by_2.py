#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for a, b in a_dictionary.items():
        new_dictionary[a] = b * 2
    return new_dictionary
