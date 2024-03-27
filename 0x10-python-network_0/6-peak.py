#!/usr/bin/python3
"""Define peak-finding algo"""


def find_peak(list_of_integers):
    """ Find peak in list of ints """
    if list_of_integers == []:
        return None

    ln = len(list_of_integers)
    m = int(ln / 2)
    lint = list_of_integers

    if m - 1 < 0 and m + 1 >= ln:
        return lint[m]
    elif m - 1 < 0:
        return lint[m] if lint[m] > lint[m + 1] else lint[m + 1]
    elif m + 1 >= length:
        return lint[m] if lint[m] > lint[m - 1] else lint[m - 1]

    if lint[m - 1] < lint[m] > lint[m + 1]:
        return lint[m]

    if lint[m + 1] > lint[m - 1]:
        return find_peak(lint[m:])
    return find_peak(lint[:m])
