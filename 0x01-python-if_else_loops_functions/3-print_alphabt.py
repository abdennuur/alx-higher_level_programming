#!/usr/bin/python3
for alphabet in range(97, 123):
    if chr(alphabet) == 'q' or chr(alphabet) == 'e':
        continue
    print(chr(alphabet).format(alphabet), end='')
