#!/usr/bin/python3
def magic_calculation(a, b):
    rslt = 0
    for ix in range(1, 3):
        try:
            if (ix > a):
                raise Exception("Too far")
            else:
                rslt += (a ** b) / ix
        except:
            rslt = b + a
            break
    return (rslt)
