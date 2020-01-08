#!/usr/bin/python3
def safe_print_division(a, b):
    c = 'Inside result:'
    try:
        if b != 0:
            return a / b
    except ZeroDivisionError:
        return None
    finally:
        if b != 0:
            print("{}".format(c), a/b)
        if b == 0:
            print("{}".format(c), None)
