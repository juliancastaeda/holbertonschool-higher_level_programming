#!/usr/bin/python3
"""
   size
   i count integuer
   print ##
"""


def print_square(size):
    """
       function print ##
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
