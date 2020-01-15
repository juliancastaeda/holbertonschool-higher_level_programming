#!/usr/bin/python3
"""
   a = integuer
   b = integuer
   return add a + b
"""


def add_integer(a, b=98):
    """
       this function
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is int or type(a) is float:
        if type(a) is float:
            a = int(a)
    if type(b) is int or type(b) is float:
        if type(b) is float:
            b = int(b)
    return a + b
