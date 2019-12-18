#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for i in range(length):
        if (i == '\0'):
            first = None
        else:
            tuple_b = (length, sentence[0])
            return (tuple_b)
