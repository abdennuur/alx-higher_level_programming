#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r_n = 0
    for ji in range(len(roman_string)):
        if ji > 0 and r_d[roman_string[ji]] > r_d[roman_string[j - 1]]:
            r_n += r_d[roman_string[ji]] - 2 * \
                        r_d[roman_string[ji - 1]]
        else:
            r_n += r_d[roman_string[ji]]
    return r_n
