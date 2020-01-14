#!/usr/bin/python3
"""
   text
   i count integuer
   print text delim '.' ':' '?'
"""
def text_indentation(text):
    """
       print text
    """ 
    if type(text) is not str:
        raise TypeError("text must be a string")
    if type(text) is str:
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                print("\n")
            else:
                print(text[i], end="")
