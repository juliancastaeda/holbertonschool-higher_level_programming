#!/usr/bin/python3
def search_replace(my_list, search, replace):
    New_list = my_list.copy()
    if len(my_list) == 0:
        return (None)
    for i in range(len(my_list)):
        if my_list[i] == search:
            New_list[i] = replace
    return New_list
