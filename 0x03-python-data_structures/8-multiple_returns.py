#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if (len == 0):
        tuple_a = (length, None)
        return (tuple_a)
    else:
        tuple_a = (length, sentence[0])
        return (tuple_a)
