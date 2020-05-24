#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """ use recursivity to find the peak
    """
    if len(list_of_integers) == 0:
        return None
    start = 0
    end = len(list_of_integers) - 1

    while (start <= end):
        mid = (start + end) // 2
        if ((mid == 0 or list_of_integers[mid - 1] <=
            list_of_integers[mid]) and (mid == len(list_of_integers) - 1 or
           list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]
        elif (mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]):
            end = mid - 1
        else:
            start = mid + 1
