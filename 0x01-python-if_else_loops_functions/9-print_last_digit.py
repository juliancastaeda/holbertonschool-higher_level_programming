#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        x = number % 10
        print('{}'.format(x), end="")
    if number < 0:
        x = (number % -10)*-1
        print('{}'.format(x), end="")
    return x
