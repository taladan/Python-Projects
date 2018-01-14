#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
How the algorithm works:

Table 1 D10	Result
1-4	Roll once on Table 2 [pref] and once on Table 3 [suff]
5-7	Roll once on Table 2 [pref] and twice on Table 3 [suff]
8-9	Roll once on Table 2 [pref] and once on Table 3 [suff] for a first name,
then once on Table 2 [pref] and twice on Table 3 [suff] for a second name
10	Roll once on Table 3 [suff], add an apostrophe, then roll once on Table 2
[pref] and twice on Table 3 [suff]

Optional Table 1B (D10)
D10	Result
1-3	Roll once on Table 4 [house_name_pref] and once on Table 5 [house_name_suff]
4-5	Roll once on Table 4 [house_name_pref] and twice on Table 5 [house_name_suff]
6-7	Roll once on Table 4 [house_name_pref] and once on Table 5 [house_name_suff],
add an apostrophe, then roll again on Table 3.
8-9	Roll once on Table 4 [house_name_pref] and once on Table 5 [house_name_suff]
for a first name, then roll on Table 1 again for a second name.
10	Roll once on Table 5 [house_name_suff], add an apostrophe, then roll once on
Table 4 [house_name_pref] and once on Table 5

Author: Taladan
Last Edited: December 6, 2017
"""

import random
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QComboBox, QLabel,
                             QHBoxLayout, QPushButton, QVBoxLayout, QWidget)
import sqlite3 as lt


class NameGen(QWidget):

    def __init__(self, race=None):

        super().__init__()
        self.initUI(race)

    # Sets up the variables to display the widgets properly
    def initUI(self, race):

        # Set up our database connection
        self.db = lt.connect('pycg.db')
        self.curs = self.db.cursor()

        self.racelst_obj = self.curs.execute("SELECT race FROM races")
        self.racelst = self.set_racelst(self.racelst_obj)

        # Create widgets
        # self.races = QComboBox(self)
        # self.disp = QLabel(self)
        # self.disp.setFont(QFont('Sans Serif', 20))
        # self.okBut = QPushButton('Okay')
        # self.quitBut = QPushButton('&Quit')

        # Populate races combobox
        # for i in self.racelst:
        #     self.races.addItem(i[0])

        # Assign the combobox text so it doesn't show as empty on init
        # self.races.setCurrentIndex(15)

        # Set up the race
        if race:
            self.race = race
        else:
            # self.race = self.races.currentText()
            self.race = 'human'

        # Populate variables for init
        self.setup()

        # Bind OK button - gen and reset the variables correctly when clicked
        # self.okBut.clicked.connect(self.onClick)

        # Bind the quit button to destroy the window
        # self.quitBut.clicked.connect(lambda: self.close())

        # Display box layout
        # self.hbox_di# sp = QHBoxLayout()
        # self.hbox_di# sp.add# stretch(1)
        # self.hbox_di# sp.addWidget(# self.di# sp)
        # self.hbox_di# sp.add# stretch(1)

        # Layout comboBoxe# s
        # self.hbox_race# s = QHBoxLayout()
        # self.hbox_race# s.add# stretch(1)
        # self.hbox_race# s.addWidget(# self.race# s)
        # self.hbox_race# s.add# stretch(1)

        # Layout Button# s
        # self.hbox_but = QHBoxLayout()
        # self.hbox_but.add# stretch(1)
        # self.hbox_but.addWidget(# self.okBut)
        # self.hbox_but.addWidget(# self.quitBut)
        # self.hbox_but.add# stretch(1)

        # Package layout# s into full di# splay
        # self.vbox = QVBoxLayout()
        # self.vbox.add# stretch(1)
        # self.vbox.addLayout(# self.hbox_di# sp)
        # self.vbox.add# stretch(1)
        # self.vbox.addLayout(# self.hbox_race# s)
        # self.vbox.add# stretch(1)
        # self.vbox.addLayout(# self.hbox_but)

        # # set layout to vbox
        # self.# setLayout(# self.vbox)

        # # set Window Geometry and di# splay it
        # self.# setGeometry(300, 300, 300, 150)
        # self.# setWindowTitle('PyCGen Name Generator')

    def setup(self):
        self.race_pref = self.pref_get()
        self.race_suff = self.suff_get()
        self.race_house_name_pref = self.hn_pref_get()
        self.race_house_name_suff = self.hn_suff_get()

        # run the filters to populate
        self.name_filter()
        self.opt_name_filter()
        self.pref()
        self.pref_h_n()
        self.suff()
        self.suff_h_n()

    # Called when the combobox changes, resets variables
    # @QtCore.pyqtSlot()
    # def onClick(self):
    #     self.setup()
    #     self.gen()

    """
    Generation engine:
        This function runs the show and changes the widget display.
        To use namegen from an external source, call namegen.NameGen.gen()
        and assign it to a variable.  This will generate a name.
    """

    def gen(self, race=None):
        # allow gen() to be called and affect the race directly.
        self.set_racelst(self.racelst)
        if race:
            self.race = race

        if random.randrange(1, 101) < 75:
            name = self.name_filter()
        else:
            name = self.opt_name_filter()
        # change the display
        # self.disp.setText(str(name))
        # return the name  -  do this when called from an external source
        return name

    def set_racelst(self, racelst_obj):
        rcs = []
        for i in racelst_obj:
            rcs.append(i)
        return rcs

    # Query the db for the race_pref and load/return it up
    def pref_get(self):
        pref = self.curs.execute("SELECT pref FROM races WHERE race = '" + self.race + "'").fetchall()
        pref = pref[0][0]
        pref = pref.split(',')
        return pref

    # Query the db for the race_suff and load/return it up
    def suff_get(self):
        suff = self.curs.execute("SELECT suff FROM races WHERE race = '" + self.race + "'").fetchall()
        suff = suff[0][0]
        suff = suff.split(',')
        return suff

    # Query the db for the house_name_race_pref and load/return it up
    def hn_pref_get(self):
        hn_pref = self.curs.execute("SELECT hn_pref FROM races WHERE race = '" + self.race + "'").fetchall()
        hn_pref = hn_pref[0][0]
        hn_pref = hn_pref.split(',')
        return hn_pref

    # Query the db for the house_name_race_suff and load/return it up
    def hn_suff_get(self):
        hn_suff = self.curs.execute("SELECT hn_suff FROM races WHERE race = '" + self.race + "'").fetchall()
        hn_suff = hn_suff[0][0]
        hn_suff = hn_suff.split(',')
        return hn_suff

    # Returns a random prefix from race.pref
    def pref(self):
        pref = self.race_pref[random.randrange(1, len(self.race_pref) - 1)].strip()
        return pref.lower()

    # Returns a random suff from race.suff
    def suff(self):
        suff = self.race_suff[random.randrange(1, len(self.race_suff) - 1)].strip()
        return suff.lower()

    # Returns a random house_name_pref from race.house_name_pref
    def pref_h_n(self):
        pref_h_n = self.race_house_name_pref[random.randrange(1, len(self.race_house_name_pref) - 1)].strip()
        return pref_h_n.lower()

    # Returns a random house_name_suff from race.house_name_suff
    def suff_h_n(self):
        suff_h_n = self.race_house_name_suff[random.randrange(1, len(self.race_house_name_suff) - 1)].strip()
        return suff_h_n.lower()

    # Returns randomized generation of the name
    def name_filter(self):
        self.roll = random.randrange(1, 11)

        if self.roll in range(1, 5):
            name = (self.pref() + self.suff())
            return name.title()

        elif self.roll in range(5, 8):
            name = (self.pref() + self.suff() + ' ' + self.pref())
            return name.title()

        elif self.roll in range(8, 11):
            if self.race == 'elf' or self.race == 'half_elf':
                name = (self.suff() + "'" + self.pref() + ' ' + self.pref() + self.suff())
                return name.title()
            elif self.race == 'human':
                name = (self.pref() + self.suff() + ' of ' + self.pref_h_n() + self.suff_h_n())
                return name.title()
            else:
                name = (self.pref() + self.suff() + ' ' + self.pref() + self.suff())
                return name.title()

    # Returns randomized generation of the optional portion of the name
    def opt_name_filter(self):
        roll = random.randrange(1, 11)

        if roll in range(1, 4):
            name = (self.pref_h_n() + self.suff_h_n())
            return name.title()

        elif roll in range(4, 6):
            name = (self.pref_h_n() + self.suff_h_n() + ' ' + self.pref_h_n())
            return name.title()

        elif roll in range(6, 8):
            if self.race == 'elf' or self.race == 'half_elf':
                name = (self.pref_h_n() + self.suff_h_n() + "'" + self.suff())
                return name.title()
            elif self.race == 'human':
                name = (self.pref() + self.suff_h_n() + ' ' + self.pref_h_n() + self.suff())
                return name.title()
            else:
                name = (self.pref_h_n() + self.suff_h_n() + ' ' + self.pref())
                return name.title()

        elif roll in range(8, 11):
            if self.race == 'elf' or self.race == 'half_elf':
                name = (self.suff() + "'" + self.pref() + '  ' + self.suff())
                return name.title()
            elif self.race == 'human':
                name = (self.pref() + self.suff() + ' of ' + self.pref_h_n() + self.suff_h_n())
                return name.title()
            else:
                name = (self.suff() + self.pref() + '  ' + self.suff())
                return name.title()


# Run this widget if this is the file run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ng = NameGen()
    sys.exit(app.exec_())
