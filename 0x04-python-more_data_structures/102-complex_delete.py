#!/usr/bin/python3
def complex_delete(my_dict, value):
    k_del = []
    for k in my_dict:
        if my_dict[k] == value:
            k_del.append(k)
    for k in k_del:
        del my_dict[k]
    return my_dict
