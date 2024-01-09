#!/usr/bin/python3
"""Define Pascal's Triangle function"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
    Return  list of lists of ints representing the triangle.
    """
    if n <= 0:
        return []

    trgls = [[1]]
    while len(trgls) != n:
        tr = trgls[-1]
        temp = [1]
        for ix in range(len(tr) - 1):
            temp.append(tr[ix] + tr[ix + 1])
        temp.append(1)
        trgls.append(temp)
    return trgls
