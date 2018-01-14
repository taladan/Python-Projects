#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
Bugbear name generator, inspired by the generators at
http://fantasynamegenerators.com

Author: Taladan
Last Edited: December 14 2017 -- Happy Birthday me!
"""

import random

nm1 = ['angr', 'angs', 'bend', 'blan', 'blud', 'bludg', 'blug', 'breng', 'cern',
       'cest', 'chime', 'chur', 'churl', 'churn', 'cill', 'clef', 'clem',
       'clen', 'cref', 'cril', 'crim', 'crus', 'cull', 'curm', 'dagg', 'dagn',
       'dam', 'delg', 'dim', 'dorm', 'dorn', 'dread', 'dred', 'dredg', 'drel',
       'drim', 'drud', 'drujg', 'drum', 'dum', 'eart', 'end', 'erd', 'erg',
       'ert', 'fang', 'fel', 'fer', 'fest', 'fien', 'find', 'fish', 'fist',
       'flea', 'flem', 'fles', 'flesh', 'flind', 'flint', 'forn', 'fring',
       'fur', 'gar', 'geld', 'gelf', 'gerd', 'gim', 'glug', 'grel', 'grif',
       'grim', 'grin', 'grind', 'grug', 'gug', 'hang', 'helg', 'hend', 'heph',
       'herd', 'herl', 'hirl', 'hunt', 'hurl', 'ilg', 'ird', 'irg', 'irn',
       'iron', 'jang', 'jel', 'jell', 'jeng', 'jerm', 'kerg', 'kern', 'kip',
       'klang', 'kleg', 'lard', 'larg', 'leng', 'lerd', 'lerg', 'lull', 'lurd',
       'lurg', 'mel', 'melg', 'meng', 'merg', 'morn', 'nail', 'nerg', 'nork',
       'nug', 'nul', 'olg', 'ork', 'orn', 'perg', 'plek', 'plug', 'prel',
       'pung', 'purl', 'quir', 'quiv', 'quol', 'quop', 'rag', 'rage', 'rong',
       'rore', 'ruor', 'rusk', 'rust', 'sel', 'skern', 'skum', 'spore', 'spurn',
       'surn', 'tern', 'thel', 'thug', 'thun', 'tor', 'tore', 'tred', 'ugl',
       'ulf', 'ulfo', 'ulg', 'unda', 'unga', 'verm', 'vile', 'vill', 'vorn',
       'wart', 'welt', 'weng', 'wort', 'wulf', 'yeg', 'yerg', 'yern', 'zern',
       'zert']

nm2 = ['ald', 'end', 'turk', 'fern', 'fend', 'grind', 'pull', 'tear', 'cuds',
       'scurt', 'scurd', 'spurd', 'bled', 'berf', 'beng', 'cern', 'culd', 'dert',
       'dern', 'drim', 'drelf', 'eolf', 'erp', 'egg', 'fard', 'ferd', 'flerm',
       'fust', 'grip', 'grippe', 'gripe', 'gul', 'guld', 'guln', 'hel', 'harm',
       'huld', 'irfo', 'ill', 'ist', 'ilgo', 'jes', 'jam', 'jelg', 'kirm', 'ker',
       'kill', 'kurn', 'kesh', 'lair', 'lemo', 'lesp', 'merth', 'mern', 'mest',
       'nual', 'nast', 'nell', 'nerl', 'orl', 'orne', 'or', 'pul', 'pel', 'rell',
       'runt', 'relp', 'stomp', 'stol', 'stole', 'stele', 'telf', 'terg', 'toss',
       'toe', 'toas', 'urne', 'urda', 'ust', 'verge', 'virge', 'vuls', 'velsh',
       'werst', 'wurnt', 'warnt', 'welg', 'yersh', 'yesh', 'yans', 'zelg', 'zel',
       'zosh']

nm3 = ['ale', 'anger', 'asp', 'blood', 'bone', 'brain', 'bad', 'brut', 'brute',
       'blud', 'carp', 'crush', 'crud', 'clash', 'cram', 'cold', 'dest', 'drum',
       'dog', 'dirt', 'flesh', 'flush', 'fell', 'fel', 'foe', 'gem', 'god',
       'gnash', 'grim', 'grunt', 'hurl', 'hang', 'hell', 'hull', 'ire', 'irk',
       'ink', 'jam', 'jark', 'jank', 'kill', 'krush', 'kurse', 'krang', 'klang',
       'lust', 'lash', 'left', 'mast', 'maul', 'maim', 'null', 'nail', 'ork',
       'ole', 'ore', 'pain', 'pulse', 'pale', 'quick', 'quirt', 'rust', 'rage',
       'rail', 'shatter', 'skum', 'scum', 'spit', 'snot', 'thorn', 'trap',
       'tear', 'torn', 'vermin', 'vale', 'vast', 'worm', 'waste', 'wrack',
       'whelp', 'xorn']

nm4 = ['ache', 'acher', 'bash', 'basher', 'bast', 'belch', 'craft', 'cull',
       'cast', 'dash', 'dust', 'dull', 'drag', 'end', 'earth', 'ent', 'fire',
       'flame', 'flash', 'fort', 'gort', 'grip', 'grippe', 'hate', 'harm',
       'hilt', 'hert', 'jest', 'jank', 'jaste', 'kish', 'kram', 'krum', 'krippe',
       'lair', 'mort', 'must', 'mank', 'murt', 'nipe', 'nost', 'nast', 'nelk',
       'orst', 'ort', 'over', 'push', 'press', 'power', 'path', 'quit', 'quire',
       'ripper', 'ripped', 'rack', 'racked', 'staph', 'stab', 'strife', 'skill',
       'tusk', 'tor', 'ture', 'ulm', 'ust', 'vane', 'vein', 'vern', 'wreck',
       'wrath', 'wrest', 'wash', 'yern', 'yearn']


def nameGen():

    nMs = nameMas(random.randrange(11))

    return nMs


def nameMas(i):
    print(i)
    if i < 4:
        rand = random.randrange(len(nm1))
        rand2 = random.randrange(len(nm2))
        nMs = nm1[rand] + nm2[rand2]

    elif i < 6:
        rand3 = random.randrange(len(nm3))
        rand4 = random.randrange(len(nm4))
        nMs = nm3[rand3] + nm4[rand4]

    else:
        rand = random.randrange(len(nm1))
        rand2 = random.randrange(len(nm2))
        rand3 = random.randrange(len(nm3))
        rand4 = random.randrange(len(nm4))
        nMs = nm1[rand] + nm2[rand2] + ' ' + nm3[rand3] + nm4[rand4]

    return nMs

if __name__ == '__main__':

    print(nameGen())
