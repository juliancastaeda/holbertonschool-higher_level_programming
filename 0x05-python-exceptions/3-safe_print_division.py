#!/usr/bin/python3
def safe_print_division(a, b):
    c = 'Inside result:'
    try:
        if b != 0:
            return a/b
        else:
            return None
    except TypeError:
        print()
    finally:
        print("{}".format(c)) 
