#!/usr/bin/python3


def inherits_from(obj, a_class):
    if type(obj) is not a_class:
        a = type(obj)
        return issubclass(a, a_class)
    else:
        return False
