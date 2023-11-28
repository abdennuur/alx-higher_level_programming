#!/usr/bin/python3
ix = 0
for ca in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(ca - ix)), end="")
    ix = 32 if ix == 0 else 0
