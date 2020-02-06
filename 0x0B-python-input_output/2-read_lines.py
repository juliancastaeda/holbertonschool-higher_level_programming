#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    j = 0
    with open(filename) as file:
        for i in file:
            j += 1
        if nb_lines <= 0 or nb_lines >= j:
            file.seek(0)
            print(file.read(), end='')
        else:
            file.seek(0)
            for i in range(nb_lines,):
                print(file.readline(), end='')
