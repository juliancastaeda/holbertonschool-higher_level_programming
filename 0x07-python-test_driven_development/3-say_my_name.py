#!/usr/bin/python3
"""
   First_name
   last_name
   print name
"""
def say_my_name(first_name, last_name=""):
    """
       print name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if type(first_name) is str:
        print("My name is {}".format(first_name), end=" ")

    if type(last_name) is str:
        print(last_name)
