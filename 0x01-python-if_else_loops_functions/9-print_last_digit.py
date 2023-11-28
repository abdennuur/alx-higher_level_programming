#!/usr/bin/python3
def print_last_digit(number):
    last_dgt = abs(number) % 10
    print(f"{last_dgt}", end='')
    return last_dgt
