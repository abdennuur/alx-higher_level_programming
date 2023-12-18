#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ix = 0
    for ji in range(x):
        try:
            print("{:d}".format(my_list[ji]), end="")
            ix += 1
        except(ValueError, TypeError):
            continue
    print()
    return ix
