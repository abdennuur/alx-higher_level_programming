#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult = []
    for ix in range(len(my_list)):
        if my_list[ix] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return mult
