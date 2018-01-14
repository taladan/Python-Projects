#!/usr/bin/python3
# -*- coding utf-8 -*-


import random

nm1 = ["Ad", "Am", "Arm", "Baer", "Daer", "Bal", "Ban", "Bar", "Bel", "Ben",
       "Ber", "Bhal", "Bhar", "Bhel", "Bram", "Bran", "Brom", "Brum", "  un",
       "Dal", "Dar", "Dol", "Dul", "Eb", "Em", "Erm", "Far", "Gal", "Gar", "Ger",
       "Gim", "Gral", "Gram", "Gran", "Grem", "Gren", "Gril", "Gry", "Gul",
       "Har", "Hjal", "Hjol", "Hjul", "Hor", "Hul", "Hur", "Kar", "Khar", "Kram",
       "Krom", "Krum", "Mag", "Mal", "Mel", "Mor", "Muir", "Mur", "Rag", "Ran",
       "Reg", "Rot", "Thal", "Thar", "Thel", "Ther", "Tho", "Thor", "Thul",
       "Thur", "Thy", "Tor", "Ty", "Um", "Urm", "Von"]

nm2 = ["adin", "bek", "' brek", "dahr", "dain", "dal", "dan", "dar", "dek",
       "dir", "dohr", "dor", "drak", "dram", "dren", "drom", "drum", "drus",
       "duhr", "dur", "dus", "gar' n", "gram", "gran", "grim", "grom", "gron",
       "grum", "grun", "gurn", "gus", "iggs", "kahm", "kam", "kohm", "kom",
       "kuhm", "kum", "kyl", "man", "mand' ", "mar", "mek", "miir", "min",
       "mir", "mond", "mor", "mun", "mund", "mur", "mus", "myl", "myr", "nam",
       "nar", "nik", "nir", "nom", "num", "nur", "nu' s", "nyl", "rak", "ram",
       "ren", "rig", "rigg", "rik", "rim", "rom", "ron", "rum", "rus", "ryl",
       "tharm", "tharn", "thran", "thrum", "thrun"]

nm3 = ["An", "Ar", "Baer", "Bar", "Bel", "Belle", "Bon", "Bonn", "Braen", "Bral",
       "Bralle", "Bran", "Bren", "Bret", "Bril", "Brille", "Brol", "Br' on",
       "Brul", "Bryl", "Brylle", "Bryn", "Bryt", "Byl", "Bylle", "Daer", "Dear",
       "Dim", "Ed", "Ein", "El", "Gem", "Ger", "Gwan", "Gwen", "Gwin", "Gwy' n",
       "Gym", "Ing", "Jen", "Jenn", "Jin", "Jyn", "Kait", "Kar", "Kat", "Kath",
       "Ket", "Las", "Lass", "Les", "Less", "Lyes", "Lys", "Lyss", "Maer",
       "Ma' ev", "Mar", "Mis", "Mist", "Myr", "Mys", "Myst", "Naer", "Nal",
       "Nas", "Nass", "Nes", "Nis", "Nys", "Raen", "Ran", "Red", "Reyn", "Run",
       "Ryn", "Sar' ", "Sol", "Tas", "Taz", "Tis", "Tish", "Tiz", "Tor", "Tys",
       "Tysh"]

nm4 = ["belle", "bera", "delle", "deth", "dielle", "dille", "dish", "do' ra",
       "dryn", "dyl", "giel", "glia", "glian", "gwyn", "la", "leen", "leil",
       "len", "lin", "linn", "lyl", "lyn", "lynn", "ma", "mera", "mora", "mura",
       "myl", "myla", "nan", "nar", "nas", "nera", "nia", "nip", "nis", "niss",
       "nora", "nura", "nyl", "nys", "nyss", "ra", "ras", "res", "ri", "ria",
       "ri' elle", "rin", "ris", "ros", "ryl", "ryn", "sael", "selle", "sora",
       "syl", "thel", "thiel", "tin", "tyn", "va", "van", "via", "vian", "waen",
       "win", "wyn", "wynn"]


def name_make():
    rand = random.randrange(0, len(nm1))
    rand2 = random.randrange(0, len(nm2))
    rand3 = random.randrange(0, len(nm3))
    rand4 = random.randrange(0, len(nm4))

    d = random.randrange(0, 4)
    name_rand = [nm1[rand] + nm2[rand2], nm3[rand3] + nm4[rand4], nm1[rand] +
                 nm4[rand4], nm3[rand3] + nm2[rand2]]

    name = name_rand[d]
    return name

if __name__ == '__main__':
    print(name_make())
