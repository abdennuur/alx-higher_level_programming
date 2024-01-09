#!/usr/bin/python3
"""
Contains read_file function
"""


def read_file(filename=""):
    """""read text file(UTF8) and print it to stdout"""
    with open(filename, "r", encoding="utf-8") as fl:
        print(fl.read(), end="")
