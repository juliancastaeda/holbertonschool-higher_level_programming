#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    a = []
    a.append([1, ])
    for i in range(0, n - 1):
        array1 = [1, ]
        for j in range(0, len(a[-1]) - 1):
            array1.append(a[-1][j] + a[-1][j + 1])
        array1.append(1)
        a.append(array1)
    return a
