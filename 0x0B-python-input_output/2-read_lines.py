#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    j = 0
    with open('my_file_0.txt') as filename:
        for i in filename:
            j += 1
        if nb_lines <= 0 or nb_lines >= j:
            filename.seek(0)
            print(filename.read(), end='')
        else:
            filename.seek(0)
            for i in range(nb_lines,):
                print(filename.readline(), end='')
