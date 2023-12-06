#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    av = 0
    dv = 0
    for tp in my_list:
        av += tp[0] * tp[1]
        dv += tp[1]
    return float(av / dv)
