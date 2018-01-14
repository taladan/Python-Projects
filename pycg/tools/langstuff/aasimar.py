#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
Aasimar name generation
based on the work from fantasynamegenerators.com

Author: Taladan
Last Edited: December 12, 2017
"""
import random

nm1 = ["", "", "", "", "b", "br", "c", "cr", "h", "l", "m", "n", "p", "r", "t",
       "v", "w", "z"]
nm2 = ["a", "e", "i", "o", "u", "y", "a", "e", "i", "o", "u", "y", "a", "e", "i",
       "o", "u", "y", "au", "ai", "ea", "ei"]
nm3 = ["d", "dr", "g", "gg", "gr", "gw", "k", "kr", "kl", "l", "ld", "lg", "lw",
       "lr", "lt", "n", "nr", "nw", "nl", "r", "rn", "rr", "rw", "rl", "v", "vr",
       "w"]
nm4 = ["a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "a", "i", "e", "a", "i",
       "e", "a", "i", "e", "o", "o", "u", "u", "ee", "ia", "ie", "ai", "ei"]
nm5 = ["d", "l", "m", "n", "t", "v"]
nm6 = ["l", "m", "n", "nt", "r"]

nm7 = ["", "", "", "", "", "br", "d", "dr", "h", "l", "m", "n", "ph", "r", "rh",
       "th", "v", "w", "z"]
nm8 = ["a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o", "a", "i", "o",
       "a", "i", "o", "e", "e", "ia", "io", "ea", "eo"]
nm9 = ["d", "j", "l", "ld", "ldr", "lv", "ll", "lt", "m", "mm", "mn", "n", "nr",
       "nv", "nl", "ndr", "nm", "r", "rd", "rk", "rs", "s", "sr", "sl", "v"]
nm10 = ["a", "e", "i", "o", "a", "e", "i", "o", "a", "e", "i", "o", "a", "e",
        "i", "o", "a", "e", "i", "o", "ea", "ia", "ie"]
nm11 = ["l", "m", "n", "r", "s", "z"]
nm12 = ["a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e", "i", "a", "e",
        "i", "au", "ou", "oe"]
nm13 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "h", "l",
        "m", "n", "r"]


def nameGen():
    for i in range(0, 10):
        if i < 4:
            name = nameFem()
        else:
            name = nameMas()

        return name


def nameFem():
    rnd = random.randrange(len(nm7))
    rnd2 = random.randrange(len(nm8))
    rnd3 = random.randrange(len(nm9))
    rnd4 = random.randrange(len(nm10))
    rnd5 = random.randrange(len(nm13))
    i = random.randrange(0, 11)

    if(i < 6):
        while nm9[rnd3] is nm7[rnd] or nm9[rnd3] is nm13[rnd5]:
            rnd3 = random.randrange(len(nm9))

        nMs = nm7[rnd] + nm8[rnd2] + nm9[rnd3] + nm10[rnd4] + nm13[rnd5]
    else:
        rnd6 = random.randrange(len(nm11))
        rnd7 = random.randrange(len(nm12))
        while(nm11[rnd6] is nm9[rnd3] or nm11[rnd6] is nm13[rnd5]):
            rnd6 = random.randrange(len(nm11))

        nMs = nm7[rnd] + nm8[rnd2] + nm9[rnd3] + nm10[rnd4] + nm11[rnd6] + nm12[rnd7] + nm13[rnd5]

    return nMs


def nameMas():
    rnd = random.randrange(len(nm1))
    rnd2 = random.randrange(len(nm2))
    rnd3 = random.randrange(len(nm3))
    rnd4 = random.randrange(len(nm4))
    rnd5 = random.randrange(len(nm6))
    i = random.randrange(0, 11)

    if(i < 6):
        while nm3[rnd3] is nm1[rnd] or nm3[rnd3] is nm6[rnd5]:
            rnd3 = random.randrange(len(nm3))

        nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm6[rnd5]
    else:
        rnd6 = random.randrange(len(nm5))
        rnd7 = random.randrange(len(nm4))
        while nm5[rnd6] is nm3[rnd3] or nm5[rnd6] is nm6[rnd5]:
            rnd6 = random.randrange(len(nm5))

        nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd6] + nm4[rnd7] + nm6[rnd5]

        print("Mas: " + nMs)
    return nMs


if __name__ == '__main__':
    print(nameGen())
