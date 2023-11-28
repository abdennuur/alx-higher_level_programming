#!/usr/bin/python3
for ix in range(26):
    if ix % 2 == 0:
        print('{:c}'.format(122 - ix), end='')
    else:
        print('{:c}'.format(90 - ix), end='')
