#!/usr/bin/python3
def uppercase(str):
    for ca in str:
        if ord(ca) >= 97 and ord(ca) <= 123:
            ca = chr(ord(ca) - 32)
        print("{}".format(ca), end="")
    print("")
