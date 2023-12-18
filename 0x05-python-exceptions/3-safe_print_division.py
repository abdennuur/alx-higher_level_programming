#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        dvs = a / b
    except ZeroDivisionError:
        dvs = None
    finally:
        print("Inside result: {}".format(dvs))
    return dvs
