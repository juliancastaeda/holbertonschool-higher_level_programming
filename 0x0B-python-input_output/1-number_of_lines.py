#!/usr/bin/python3
def number_of_lines(filename=""):
    filename = open('my_file_0.txt', 'r')
    a = len(filename.readlines())
    return a
    filename.close
