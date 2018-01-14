#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyCGen v0.1

This is a character generation program for 5th Edition
Dungeons and Dragons.

Author: Taladan
Last Edited: November 20, 2017
"""
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
                             QLabel, QPushButton, QVBoxLayout, QWidget)
import sys
import character as ch
# from dicetools import *

new_character = ch.Character()

"""
 for roll methods:
   Classic     -   Roll 3d6 and apply them as desired
   Standard    -   Roll 4d6 discard the lowest & apply them as desired
   Hardmode    -   Roll 3d6 and apply them in rolled order
"""

method = 'standard'

def roll_method(method, temp_abilities):
    unset_abilities = []
    if method == 'standard':
        for i in temp_abilities:
            i.remove(min(i))
            unset_abilities.append(sum(i))
    elif method == 'classic':
        for i in temp_abilities:
            unset_abilities.append(sum(i))
    elif method == 'hardmode':
        for i in temp_abilities:
            unset_abilities.append(sum(i))
        keys = new_character.abilities_order
        values = unset_abilities
        new_character.abilities = dict(zip(keys, values))
        unset_abilities = 'Character abilities assigned.'
    return unset_abilities

def roll_abilities(method):
    num_dice = None
    try:
        if method == 'standard':
            num_dice = '4d6'
        elif method == 'classic' or method == 'hardmode':
            num_dice = '3d6'
        else:
            raise TypeError
    except TypeError:
        print('Improper method input: {method}.  Choose standard, classic, or hardmode'.format(method=method))
    temp_abilities = []
    for key in new_character.abilities:
        seq = throw(num_dice)[1]
        temp_abilities.append(seq)
    abilities = roll_method(method, temp_abilities)
    return abilities


if __name__ == '__main__':

    app = QApplication(sys.argv)
    cg = CGen()
    sys.exit(app.exec_())
