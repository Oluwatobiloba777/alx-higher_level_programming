#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string and type(roman_string) == str:
        rn = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nun_rn = [s for s in roman_string]
        res = 0
        l = len(nun_rn)
        for i in range(l):
            if i < l - 1 and rn.get(nun_rn[i]) < rn.get(nun_rn[i + 1]):
                res -= rn.get(nun_rn[i])
            else:
                res += rn.get(nun_rn[i])
        return res
    return 0
