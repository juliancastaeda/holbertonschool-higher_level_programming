#!/usr/bin/python3
def max_integer(my_list=[]):
    num_larger = my_list[0]
    if (len(my_list) == 0):
        return (None)
    for i in range(len(my_list)):
        if num_larger < my_list[i]:
            num_larger = my_list[i]
    return (num_larger)
