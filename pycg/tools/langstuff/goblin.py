#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
Goblin namegen, based on the name generators at:
    http://fantasynamegenerators.com

Author: Taladan
Last Edited: December 14, 2017
"""

import random

nm1 = ["", "", "", "", "", "", "", "b", "c", "d", "f", "g", "h", "j", "k", "l",
       "p", "r", "t", "v", "w", "x", "z", "br", "bl", "cr", "cl", "ch", "dr",
       "fr", "gr", "gl", "gn", "kr", "kl", "pr", "pl", "str", "st", "sr", "sl",
       "tr", "vr", "wr", "zr"]

nm2 = ["a", "e", "i", "o", "u", "a", "e", "i", "o", "u", "a", "e", "i", "o",
       "u", "y", "ia", "io", "ee", "aa", "ui", "ie", "ea", "oi"]

nm3 = ["b", "d", "g", "h", "k", "l", "m", "n", "r", "s", "t", " v", "z", "b",
       "d", "g", "h", "k", "l", "m", "n", "r", "s", "t", "v", "z", "b", "d",
       "g", "h", "k", "l", "m", "n", "r", "s", "t", "v", "z", "b", "d", "g",
       "h", " k", "l", "m", "n", "r", "s", "t", "v", "z", "bb", "bd", "bh",
       "bl", "bk", "bn", "br", "bs", "bt", "bz", "db", "dd", "df", "dh", "dl",
       "dn", "dr", "ds", "dv ", "dz", "", "gg", "gb", "gd", "gh", "gk", "gl",
       "gm", "gn", "gr", "gs", "gt", "gz", "hd", "hb", "hk", "hn", "hz", "kl",
       "kn", "kz", "kv", "kk", "lb", "ld ", "lg", "lk", "ll", "lr", "ls", "lt",
       "lv", "lz", "mr", "mv", "mz", "mt", "nr", "nv", "nz", "nt", "rb", "rd",
       "rg", "rk", "rl", "rm", "rn", "rr", "rs", " rt", "rv", "rz", "sb", "sd",
       "sh", "sk", "sm", "sn", "sr", "str", "st", "sv", "sz", "ss", "tb", "tl",
       "tm", "tn", "tr", "tv", "tz", "tt", "vl", "vn", "vr ", "vz", "zb", "zd",
       "zg", "zl", "zm", "zn", "zt"]

nm4 = ["c", "g", "k", "l", "q", "r", "t", "x", "z", "nk", "ld", "rd", "s", "sz",
       "zz", "ng", "k z", "lb", "rm", "sb", "bs", "ts", "cs", "ct", "gs", "gz",
       "kt", "kx", "lk", "lx", "rk", "rt", "rd", "rx"]

nm5 = ["", "", "", "", "", "", "", "b", " c", "d", "f", "g", "h", "j", "k", "l",
       "m", "n", "p", "q", "r", "s", "t", "v", "w", "bh", "br", "bl", "cr",
       "cl", "ch", "fr", "fl", "gr", "gl", "gn", "kh", " kl", "ph", "pr", "sh",
       "st", "sr", "sl", "sw", "th", "thr", "tr", "vr", "wr"]

nm6 = ["b", "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", " v", "b",
       "f", "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "b", "f",
       "g", "h", "k", "l", "m", "n", "p", "r", "s", "t", "v", "b", "f", "g",
       "h", "k", " l", "m", "n", "p", "r", "s", "t", "v", "bb", "bd", "bh",
       "bl", "bk", "bn", "br", "bs", "bt", "bz", "fb", "fl", "fm", "fn", "fs",
       "ft", "gg", "gb", "gd", "g h", "gk", "gl", "gm", "gn", "gr", "gs", "gt",
       "gz", "hd", "hb", "hk", "hn", "hz", "kl", "kn", "kz", "kv", "kk", "lb",
       "ld", "lg", "lk", "ll", "lr", "ls", "lt", "lv", "lz", "mr", "mv", "mz",
       "mt", "nr", "nv", "nz", "nt", "ph", "pf", "pl", "pn", "pm", "pr", "ps",
       "pt", "pv", "rb", "rd", "rg", "rk", "rl", "rm ", "rn", "rr", "rs", "rt",
       "rv", "rz", "sb", "sd", "sh", "sk", "sm", "sn", "sr", "str", "st", "sv",
       "sz", "ss", "tb", "tl", "tm", "tn", "tr", "tv", "tz", "tt", "vl", "vn",
       "vr", "vz"]

nm7 = ["h", "f", "g", "l", "n", "q", "s", "x", "z", "ls", "nk", "zz", "ld",
       "sh", "sz", "ss", "gs", "sx", "lx", "hx ", "th", "rx", "rt", "ft", "fs",
       "fz", "lm", "lk", "lt", "ng", "nx", "ns", "nq"]

nm8 = ["e", "i", "ee", "ia", "ea", "a", "ai", "", "", "", "", "", "", "", "",
       "", "", "", "", ""]


r1 = random.randrange(len(nm1))
r2 = random.randrange(len(nm2))
r3 = random.randrange(len(nm3))
r4 = random.randrange(len(nm4))
r5 = random.randrange(len(nm5))
r6 = random.randrange(len(nm6))
r7 = random.randrange(len(nm7))
r8 = random.randrange(len(nm8))


def nameGen():
    tp = random.randrange(11)

    for i in range(11):
        rnd2 = r2
        rnd2b = r2
        if tp < 5:
            rnd5 = r5
            rnd7 = r7
            rnd8 = r8

            if(i < 5):
                names = nm5[rnd5] + nm2[rnd2] + nm7[rnd7] + nm8[rnd8]
            else:
                rnd6 = r6
                names = nm5[rnd5] + nm2[rnd2] + nm6[rnd6] + nm2[rnd2b] + nm7[rnd7] + nm8[rnd8]

        else:
            rnd5 = r1
            rnd7 = r4
            if(i < 5):
                names = nm1[rnd5] + nm2[rnd2] + nm4[rnd7]
            else:
                rnd3 = r3
                names = nm1[rnd5] + nm2[rnd2] + nm3[rnd3] + nm2[rnd2b] + nm4[rnd7]

        return names


if __name__ == '__main__':

    print(nameGen())
