#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        ca = add(a, b)
        for i in range(4, 6):
            ca = add(ca, i)
        return (ca)
    else:
        return(sub(a, b))
