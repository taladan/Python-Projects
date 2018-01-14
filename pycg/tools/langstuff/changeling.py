#!/usr/bin/python3
# -*- coding utf-8
"""
Changeling namegen, based on the namegenerators found at:
    http://fantasynamegenerators.com

Author: Taladan
Last Edited: December 14, 2017
"""

import random

nm1 = ["", "", "", "b", "d", "f", "h", "j", "l", "m", "n", "p", "r", "s", "t",
       "v", "w", "y"]

nm2 = ["a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o", "u", "a", "i", "o",
       "u", "ee", "ie", "ea", "ey", "ae", "ai", "ay", "oo", "ou"]

nm3 = ["c", "g", "gs", "k", "ks", "kt", "m", "n", "rx", "rt", "rs", "s", "sk",
       "st", "sp", "t", "ts", "x", "z"]


def nameGen():
    rand = random.randrange(len(nm1))
    rand2 = random.randrange(len(nm2))
    rand3 = random.randrange(len(nm3))

    name = nm1[rand] + nm2[rand2] + nm3[rand3]

    return name


if __name__ == '__main__':

    print(nameGen())
