#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nbr = 0
    for ix in range(x):
        try:
            print("{}".format(my_list[ix]), end="")
        except IndexError:
            break
        else:
            nbr += 1
    print()
    return nbr
