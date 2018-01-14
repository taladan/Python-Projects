#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
aaracokra name generator

Author Taladan
Last Edited: December 12, 2017
"""
import random

nm1 = ["", "", "", "", "", "c", "cl", "cr", "d", "g", "gr", "h", "k", "kh", "kl",
       "kr", "q", "qh", "ql", "qr", "r", "rh", "s", "y", "z"]
nm2 = ["a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i",
       "u", "a", "e", "i", "u", "a", "e", "i", "u", "a", "e", "i", "u", "ae",
       "aia", "ee", "oo", "ou", "ua", "uie"]
nm3 = ["c", "cc", "k", "kk", "l", "ll", "q", "r", "rr"]
nm4 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i",
       "aa", "ea", "ee", "ia", "ie"]
nm5 = ["", "", "", "", "c", "ck", "d", "f", "g", "hk", "k", "l", "r", "rr", "rc",
       "rk", "rrk", "s", "ss"]


def nameGen():
    for i in range(11):
        nMs = nameMas(i)
        while nMs is "":
            nMs = nameMas(i)
    return nMs


def nameMas(i):
    rnd = random.randrange(len(nm1))
    rnd2 = random.randrange(len(nm2))
    rnd3 = random.randrange(len(nm5))
    if i < 5:
        while nm1[rnd] is nm5[rnd3]:
            rnd3 = random.randrange(len(nm5))

        nMs = nm1[rnd] + nm2[rnd2] + nm5[rnd3]
    else:
        rnd4 = random.randrange(len(nm3))
        rnd5 = random.randrange(len(nm4))
        nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm5[rnd3]

    return nMs


if __name__ == '__main__':

    print(nameGen())
