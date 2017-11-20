#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyDice v1.1

A program to roll dice ranging from d4 to d100.

Author: Taladan
Last Edited: November 2017
"""

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
                             QLabel, QPushButton, QVBoxLayout, QWidget)

import random
import sys


class PyDice(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    # Set the number of dice to roll
    def set_dice_total(self, roll_table):
        roll_table['roll_total'] = self.num_of_dice.currentText()
        return roll_table

    # Set the type of dice to roll
    def set_die_type(self, roll_table):
        roll_table['die'] = self.die_type.currentText()
        return roll_table

    # Roll & update label
    def roll(self, roll_table, ischecked):

        die = int(roll_table['die'][1:])
        tot = int(roll_table['roll_total'])

        choice_lst = []

        for i in range(tot):
            choice_lst.append(random.randrange(1, die + 1))

        if ischecked and tot > 1:
            choice_lst.remove(min(choice_lst))

        choice = sum(choice_lst)
        self.disp.setText(str(choice))

    # Build the display
    def initUI(self):

        # Dictionary that stores type of dice and number to roll
        roll_table = {'die': 'd4', 'roll_total': '1'}

        # List of dice type
        self.dice = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20', 'd100']

        # Create Output Display
        self.disp = QLabel(self)
        self.disp.setFont(QFont('Sans Serif', 20))

        # Create ComboBox Labels
        self.dice_num_lbl = QLabel("# of Die to roll", self)
        self.die_type_lbl = QLabel("Type of Die to roll", self)

        # Create comboBoxes
        self.num_of_dice = QComboBox(self)
        self.num_of_dice.activated.connect(lambda: self.set_dice_total(roll_table))
        self.die_type = QComboBox(self)
        self.die_type.activated.connect(lambda: self.set_die_type(roll_table))

        # Build contents of comboBoxes
        for num in range(1, 51):
            self.num_of_dice.addItem(str(num))

        for num in self.dice:
            self.die_type.addItem(str(num))

        # Build checkbox
        self.rm_lowest_cb = QCheckBox('Remove Lowest')

        # Assign buttons
        rollBut = QPushButton('Roll')
        rollBut.clicked.connect(lambda: self.roll(roll_table,
                                                  self.rm_lowest_cb.isChecked()))
        quitBut = QPushButton('Quit')
        quitBut.clicked.connect(QCoreApplication.instance().quit)

        # Layout Display
        hbox_disp = QHBoxLayout()
        hbox_disp.addStretch(1)
        hbox_disp.addWidget(self.disp)
        hbox_disp.addStretch(1)

        # Layout labels
        hbox_lbls = QHBoxLayout()
        hbox_lbls.addStretch(1)
        hbox_lbls.addWidget(self.dice_num_lbl)
        hbox_lbls.addStretch(1)
        hbox_lbls.addWidget(self.die_type_lbl)
        hbox_lbls.addStretch(1)

        # Layout comboBoxes
        hbox_die = QHBoxLayout()
        hbox_die.addStretch(1)
        hbox_die.addWidget(self.num_of_dice)
        hbox_die.addStretch(1)
        hbox_die.addWidget(self.die_type)
        hbox_die.addStretch(1)

        # Layout Buttons
        hbox_but = QHBoxLayout()
        hbox_but.addStretch(1)
        hbox_but.addWidget(rollBut)
        hbox_but.addWidget(quitBut)
        hbox_but.addStretch(1)

        # Package layouts into full display
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox_disp)
        vbox.addStretch(1)
        vbox.addLayout(hbox_lbls)
        vbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox_die)
        vbox.addStretch(1)
        vbox.addWidget(self.rm_lowest_cb)
        vbox.addStretch(1)
        vbox.addLayout(hbox_but)

        # Set layout to vbox
        self.setLayout(vbox)

        # Set Window Geometry and display it
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('PyDice Roller')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    pd = PyDice()
    sys.exit(app.exec_())
