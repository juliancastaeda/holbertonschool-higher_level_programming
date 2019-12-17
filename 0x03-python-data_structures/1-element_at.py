#!/usr/bin/python3
def element_at(my_list, idx):
    siz = len(my_list)
    if (idx < 0) or (idx > siz):
        return None
    else:
        return my_list[idx]
