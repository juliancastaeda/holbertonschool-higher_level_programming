#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                a += 1
        print()
    except TypeError:
        print()
    return a
