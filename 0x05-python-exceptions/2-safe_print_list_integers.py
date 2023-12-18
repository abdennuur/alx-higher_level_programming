#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr = 0
    for ix in range(x):
        try:
            print("{:d}".format(my_list[ix]), end="")
        except (ValueError, TypeError):
            pass
        else:
            nbr += 1
    print()
    return (nbr)
