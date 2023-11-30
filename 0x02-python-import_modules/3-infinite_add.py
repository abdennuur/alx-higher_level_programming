#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    for ix in range(len(sys.argv) - 1):
        total += int(sys.argv[ix + 1])
    print("{}".format(total))
