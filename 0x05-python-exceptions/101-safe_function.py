#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        rslt = fct(*args)
        return rslt
    except Exception as er:
        import sys
        print("Exception: {}".format(er), file=sys.stderr)
        return None
