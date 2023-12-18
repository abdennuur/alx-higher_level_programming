#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nls = []
    for ix in range(list_length):
        try:
            rslt = my_list_1[ix] / my_list_2[ix]
        except (TypeError):
            print("wrong type")
            rslt = 0
        except (ZeroDivisionError):
            print("division by 0")
            rslt = 0
        except (IndexError):
            print("out of range")
            rslt = 0
        finally:
            nls.append(rslt)
    return (nls)
