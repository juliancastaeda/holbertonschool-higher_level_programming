#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string1 = 'Last digit of {:d} is {:d} and is greater than 5'
string2 = 'Last digit of {:d} is {:d} and is less than 6 and not 0'
string3 = 'Last digit of {:d} is {:d} and is less than 6 and not 0'
if number >= 0:
    x = number % 10
    if x > 5:
        print(string1.format(number, x))
    if x == 0:
        print('Last digit of {:d} is {:d} and is 0'.format(number, x))
    if (x != 0) and (x < 6):
        print(string2.format(number, x))
if number < 0:
    x = (number % -10)
    if (x != 0) and (x < 6):
        print(string3.format(number, x))
