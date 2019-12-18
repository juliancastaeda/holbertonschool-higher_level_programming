#!/usr/bin/python3
def max_integer(my_list=[]):
    num_larger = my_list[0]
    if my_list == []:
        return (None)
    num:larger = my_list[0]
    for i in my_list:
        if num_larger <= i:
            num_larger = i
    return (num_larger)
