#!/usr/bin/python3
def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) is True:
        if isinstance(obj, a_class) is True and type(obj) != a_class:
            return True
        else:
            return False
