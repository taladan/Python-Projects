#!/usr/bin/python3
# coding utf-8 -*-
"""
firbolg name generator using info from fantasynamegenerators.com

author: Taladan
last edit: December 12, 2017
"""
import random

nm1 = ["Ad", "Ae", "Bal", "Bei", "Car", "Cra", "Dae", "Dor", "El", "Ela", "Er",
       "Far", "Fen", "Gen", "Glyn", "Hei", "Her", "Ian", "Ili", "Kea", "Kel",
       "Leo", "Lu", "Mira", "Mor", "Nae", "Nor", "Olo", "Oma", "Pa", "Per",
       "Pet", "Qi", "Qin", "Ralo", "Ro", "Sar", "Syl", "The", "Tra", "Ume",
       "Uri ", "Va", "Vir", "Waes", "Wran", "Yel", "Yin", "Zin", "Zum"]

nm2 = ["balar", "beros", "can", "ceran", "dan", "dithas", "faren", "fir",
       "geiros", "golor", "hice", "horn", "jeon", "jor", "kas", "kian", "lamin",
       "lar", "len", "maer", "maris", "menor", "myar", "nan", "neiros", "nelis",
       "no rin", "peiros", "petor", "qen", "quinal", "ran", "ren", "ric", "ris",
       "ro", "salor", "sandoral", "toris", "tumal", "valur", "ven", "warin",
       "wrae k", "xalim", "xidor", "yarus", "ydark", "zeiros", "zumin"]

nm3 = ["Ad", "Ara", "Bi", "Bry", "Cai", "Chae", "Da", "Dae", "Eil", "En", "Fa",
       " Fae", "Gil", "Gre", "Hele", "Hola", "Iar", "Ina", "Jo", "Key", "Kris",
       "Lia", "Lora", "Mag", "Mia", "Neri", "Ola", "Ori", "Phi", "Pres", "Qi",
       "Qui", "Rava", "Rey", "Sha", "Syl", "Tor", "Tris", "Ula", "Uri", "Val",
       "Ven", "Wyn", "Wysa", "Xil", "Xyr", "Yes", "Ylla", "Zin", "Zyl"]

nm4 = ["b anise", "bella", "caryn", "cyne", "di", "dove", "fiel", "fina",
       "gella", "gwyn", "hana", "harice", "jyre", "kalyn", "krana", "lana",
       "lee", "leth ", "lynn", "moira", "mys", "na", "nala", "phine", "phyra",
       "qirelle", "ra", "ralei", "rel", "rie", "rieth", "rona", "rora", "roris",
       "satra", "sti na", "sys", "thana", "thyra", "tris", "varis", "vyre",
       "wenys", "wynn", "xina", "xisys", "ynore", "yra", "zana", "zorwyn"]


def nameGen():
    for i in range(10):
        if i < 4:
            nMs = nameFem()
        while nMs is "":
            nMs = nameFem()

        else:
            nMs = nameMas()
            while nMs is "":
                nMs = nameMas()

        return nMs


def nameFem():
    rnd = random.randrange(len(nm3))
    rnd2 = random.randrange(len(nm4))
    nMs = nm3[rnd] + nm4[rnd2]

    return nMs


def nameMas():
    rnd = random.randrange(len(nm1))
    rnd2 = random.randrange(len(nm2))
    nMs = nm1[rnd] + nm2[rnd2]

    return nMs


if __name__ == '__main__':

    print(nameGen())
