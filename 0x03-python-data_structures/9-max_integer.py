#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    num:larger = my_list[0]
    for i in my_list:
        if num_larger <= i:
            num_larger = i
    return (num_larger)
