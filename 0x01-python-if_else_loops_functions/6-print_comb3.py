#!/usr/bin/python3
for n1 in range(0, 8):
    for n2 in range(n1 + 1, 10):
        print("{:d}{:d}".format(n1, n2), end=', ')
print("{:d}{:d}".format(n1 + 1, n2))
