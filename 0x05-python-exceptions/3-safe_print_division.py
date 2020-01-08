#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if b != 0:
            return a/b
    finally:
        print("Inside result:")
        if b == 0:
            return None
