#!/usr/bin/python3
def read_file(filename=""):
    filename = open('my_file_0.txt', 'r')
    print(filename.read(), end='')
