#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = set(my_list)
    r = 0
    for i in n:
        r += i
    return r
