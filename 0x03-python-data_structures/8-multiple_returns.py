#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = None
    for i in range(length):
        if (i == '\0'):
            tuple_a = (length, None)
            return tuple_a
        if (i >= 0):
            first = sentence[0]
            tuple_b = (length, first)
            return tuple_b
