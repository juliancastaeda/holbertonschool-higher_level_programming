#!/usr/bin/python3
def print_last_digit(number):
    y = -1
    if number >= 0:
        x = number % 10
        print('{:d}'.format(x), end="")
    if number < 0:
        x = (number % -10) * y
        print('{:d}'.format(x), end="")
        return x
