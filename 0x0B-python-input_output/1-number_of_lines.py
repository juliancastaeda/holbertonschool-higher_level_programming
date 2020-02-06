#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as file:
        a = 0
        for num in file:
            a += 1
        return a
