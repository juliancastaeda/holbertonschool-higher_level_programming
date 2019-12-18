#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for i in range(length):
        if (i == '\0'):
            tuple_a = (length, None)
            return tuple_a
        if (i >= 0):
            tuple_b = (length, sentence[0])
            return tuple_b
