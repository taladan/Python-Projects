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
Last Edited: November 24, 2017
"""
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QComboBox, QLabel, QHBoxLayout,
                             QPushButton, QVBoxLayout, QWidget)
import random
import sqlite3 as lt
import sys


class namegen(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()

    # Sets up the variables to display the widgets properly
    def initUI(self):
        # self.racelst = ['aasimar', 'bugbear', 'dragonborn', 'dwarf', 'elf',
        #                 'firbolg', 'genasi', 'gnome', 'goblin', 'goliath',
        #                 'half_elf', 'half_orc', 'halfling', 'hobgoblin', 'human',
        #                 'kenku', 'kobold', 'lizardfolk', 'orc', 'tabaxi',
        #                 'tiefling', 'tortle', 'triton', 'yuan_ti']

        self.racelst = ['dragonborn', 'dwarf', 'elf', 'gnome', 'goliath',
                        'half_elf', 'half_orc', 'halfling', 'tiefling']

        # Set up our database connection
        self.db = lt.connect('pycg.db')
        self.curs = self.db.cursor()

        # Create widgets
        self.races = QComboBox()
        self.disp = QLabel()
        self.disp.setFont(QFont('Sans Serif', 20))
        self.okBut = QPushButton('Okay')
        self.quitBut = QPushButton('Quit')

        # Populate races combobox
        for i in self.racelst:
            self.races.addItem(i)

        # Populate variables when combobox is changed.
        self.races.setCurrentIndex(1)
        # self.races.currentIndexChanged.connect(lambda: self.set_vars(self.race))
        self.race = self.races.currentText()
        self.race_pref = self.pref_get(self.race)
        self.race_suff = self.suff_get(self.race)
        self.race_house_name_pref = self.hn_pref_get(self.race)
        self.race_house_name_suff = self.hn_suff_get(self.race)

        # Bind buttons
        self.okBut.clicked.connect(lambda: self.gen(self.race))
        self.okBut.clicked.connect(lambda: self.set_vars(self.race))
        self.quitBut.clicked.connect(QtCore.QCoreApplication.instance().quit)

        # Display box layout
        hbox_disp = QHBoxLayout()
        hbox_disp.addStretch(1)
        hbox_disp.addWidget(self.disp)
        hbox_disp.addStretch(1)

        # Layout comboBoxes
        hbox_races = QHBoxLayout()
        hbox_races.addStretch(1)
        hbox_races.addWidget(self.races)
        hbox_races.addStretch(1)

        # Layout Buttons
        hbox_but = QHBoxLayout()
        hbox_but.addStretch(1)
        hbox_but.addWidget(self.okBut)
        hbox_but.addWidget(self.quitBut)
        hbox_but.addStretch(1)

        # Package layouts into full display
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_disp)
        vbox.addStretch(1)
        vbox.addLayout(hbox_races)
        vbox.addStretch(1)
        vbox.addLayout(hbox_but)

        # Set layout to vbox
        self.setLayout(vbox)

        # Set Window Geometry and display it
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('PyCGen Name Generator')
        self.show()

    # Set the variables to the right ones
    @QtCore.pyqtSlot(str)
    def set_vars(self, race):
        self.race_pref = self.pref_get(race)
        self.race_suff = self.suff_get(race)
        self.race_house_name_pref = self.hn_pref_get(race)
        self.race_house_name_suff = self.hn_suff_get(race)
        self.race = self.races.currentText()

        self.name_filter()
        self.opt_name_filter()
        self.pref()
        self.pref_h_n()
        self.suff()
        self.suff_h_n()

    # Generation engine - this function runs the show and changes the widget
    # display.
    def gen(self, race):
        if random.randrange(1, 101) < 65:
            name = self.name_filter()
        else:
            name = self.opt_name_filter()
        self.disp.setText(str(name))

    # Query the db for the race_pref and load/return it up
    def pref_get(self, race):
        pref = self.curs.execute("SELECT pref FROM " + race + "_pref").fetchall()
        return pref

    # Query the db for the race_suff and load/return it up
    def suff_get(self, race):
        suff = self.curs.execute("SELECT suff FROM " + race + "_suff").fetchall()
        return suff

    # Query the db for the house_name_race_pref and load/return it up
    def hn_pref_get(self, race):
        hn_pref = self.curs.execute("SELECT house_name_pref FROM " + race + "_house_name_pref").fetchall()
        return hn_pref

    # Query the db for the house_name_race_suff and load/return it up
    def hn_suff_get(self, race):
        hn_suff = self.curs.execute("SELECT house_name_suff FROM " + race + "_house_name_suff").fetchall()
        return hn_suff

    # Returns a random prefix from race.pref
    def pref(self):
        pref = self.race_pref[random.randrange(1, len(self.race_pref))][0]
        return pref.lower()

    # Returns a random suff from race.suff
    def suff(self):
        suff = self.race_suff[random.randrange(1, len(self.race_suff))][0]
        if suff[0] == '-':
            suff = suff[1:]
        return suff.lower()

    # Returns a random house_name_pref from race.house_name_pref
    def pref_h_n(self):
        pref_h_n = self.race_house_name_pref[random.randrange(1, len(self.race_house_name_pref))][0]
        return pref_h_n.lower()

    # Returns a random house_name_suff from race.house_name_suff
    def suff_h_n(self):
        suff_h_n = self.race_house_name_suff[random.randrange(1, len(self.race_house_name_suff))][0][1:]
        if suff_h_n[0] == '-':
            suff_h_n = suff_h_n[1:]
        return suff_h_n.lower()

    # Returns randomized generation of the name
    def name_filter(self):
        self.table1 = random.randrange(1, 11)

        if self.table1 in range(1, 5):
            name = (self.pref() + self.suff())
        elif self.table1 in range(5, 8):
            name = (self.pref() + self.suff() + self.suff())
        elif self.table1 in range(8, 10):
            name = (self.pref() + self.suff() + ' ' + self.pref() + self.suff() +
                    self.suff())
        else:
            name = (self.suff() + "'" + self.pref() + self.suff() + self.suff())
        return name.title()

    # Returns randomized generation of the optional portion of the name
    def opt_name_filter(self):
        self.table1b = random.randrange(1, 11)

        if self.table1b in range(1, 4):
            name = (self.pref_h_n() + self.suff_h_n())

        elif self.table1b in range(4, 6):
            name = (self.pref_h_n() + self.suff_h_n() + self.suff_h_n())

        elif self.table1b in range(6, 8):
            name = (self.pref_h_n() + self.suff_h_n() + "'" + self.suff())

        elif self.table1b in range(8, 10):
            name = (self.pref_h_n() + self.suff_h_n() + ' ' + self.pref())
        else:
            name = (self.suff() + "'" + self.pref() + '  ' + self.suff())
        return name.title()


# Run this widget if this is the file run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ng = namegen()
    sys.exit(app.exec_())
