#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    temp_tuple_a = list(tuple_a)
    temp_tuple_b = list(tuple_b)
    if len(temp_tuple_a) < 2:
        for i in range(len(temp_tuple_a), 2):
            temp_tuple_a.append(0)
    if len(temp_tuple_b) < 2:
        for i in range(len(temp_tuple_b), 2):
            temp_tuple_b.append(0)
    c = [temp_tuple_a[0] + temp_tuple_b[0], temp_tuple_a[1] + temp_tuple_b[1]]
    tuple_c = tuple(c)
    return tuple_c
