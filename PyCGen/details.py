#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This file builds the details layout and contents of
the details tab in PyCGen.

Author: Taladan
Last Edited: December 5, 2017
"""
from PyQt5.QtCore import (QSize, pyqtSlot)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtWidgets import (QComboBox, QFormLayout, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget)
import sqlite3
import namegen as ng


class BuildDetailsTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        # Set up our database connection
        self.db = sqlite3.connect("pycg.db")
        self.curs = self.db.cursor()

        # Fonts setup
        self.lbl_font = QFont()
        self.lbl_font.setFamily("Free Mono")
        self.lbl_font.setPointSize(18)

        # Create widgets
        self.pc_name_field = QLineEdit(self)
        self.pc_nmgen_but = QPushButton(self)
        self.pl_name_field = QLineEdit(self)
        self.race_cb = QComboBox(self)
        self.pc_class_cb = QComboBox(self)
        self.pc_level_cb = QComboBox(self)
        self.hd_lbl = QLabel()
        self.age_field = QLineEdit(self)
        self.sex_field = QLineEdit(self)
        self.height_field = QLineEdit(self)
        self.weight_field = QLineEdit(self)
        # unconfigured
        self.hair_color_field = QLineEdit(self)
        self.eye_color_field = QLineEdit(self)
        self.skin_color_field = QLineEdit(self)
        self.personality_trait_one_field = QLineEdit(self)
        self.personality_trait_two_field = QLineEdit(self)
        self.ideals_field = QLineEdit(self)
        self.bonds_field = QLineEdit(self)
        self.flaws_field = QLineEdit(self)

        # name field stuff
        self.pc_name_field.setMaximumWidth(200)
        self.pl_name_field.setMaximumWidth(200)

        # generator button stuff
        self.pc_nmgen_but.setIcon(QIcon('d20-icon.png'))
        self.pc_nmgen_but.setIconSize(QSize(15, 15))
        self.pc_nmgen_but.setToolTip('Generate a random PC name')
        self.pc_nmgen_but.clicked.connect(self.pc_nmgen_on_click)

        # Race selection combobox
        races = self.get_races()

        for i in range(len(self.get_races())):
            self.race_cb.addItem(races[i])

        self.race_cb.setCurrentIndex(15)
        self.race_cb.activated[str].connect(self.race_cb_onActivated)
        self.race = self.set_race()

        # Populate class/level combobox
        self.classes = self.get_classes()

        for i in range(len(self.get_classes())):
            self.pc_class_cb.addItem(self.classes[i])

        for i in range(1, 21):
            self.pc_level_cb.addItem(str(i))

        # set class
        self.pc_class = self.pc_class_cb.currentText()
        self.pc_class_cb.activated[str].connect(self.class_cb_onActivated)

        # Set level
        self.pc_level = self.pc_level_cb.currentText()

        # HD label config
        self.hd_lbl.setFont(self.lbl_font)
        self.hd_lbl.setText(self.get_hd())

        self.age_field.setMaximumWidth(50)
        self.sex_field.setMaximumWidth(50)
        self.height_field.setMaximumWidth(50)
        self.weight_field.setMaximumWidth(50)

        self.hair_color_field.setMaximumWidth(50)
        self.eye_color_field.setMaximumWidth(50)
        self.skin_color_field.setMaximumWidth(50)
        self.personality_trait_one_field.setMaximumWidth(200)
        self.personality_trait_two_field.setMaximumWidth(200)
        self.ideals_field.setMaximumWidth(200)
        self.bonds_field.setMaximumWidth(200)
        self.flaws_field.setMaximumWidth(200)

        # Set widget sizes
        self.pc_nmgen_but.setMaximumWidth(50)
        self.race_cb.setMaximumWidth(100)
        self.pc_class_cb.setMaximumWidth(100)
        self.pc_level_cb.setMaximumWidth(50)

        """
        vbox_layout - main container
        hbox_cont_layout - lines container
        left_form_layout - left side of the window - holds fields and controls
        center_form_layout - left side of the window - holds fields and controls
        right_form_layout - left side of the window - holds fields and controls
        """
        self.vbox_layout = QVBoxLayout(self)
        self.hbox_cont_layout = QHBoxLayout(self)
        self.left_form_layout = QFormLayout(self)
        self.center_form_layout = QFormLayout(self)
        self.right_form_layout = QFormLayout(self)

        # left_form_layout rows
        self.left_form_layout.addRow("PC Name: ", self.pc_name_field)
        self.left_form_layout.addRow("Player Name: ", self.pl_name_field)
        self.left_form_layout.addRow("Level: ", self.pc_level_cb)
        self.left_form_layout.addRow("Age", self.age_field)
        self.left_form_layout.addRow("Sex", self.sex_field)
        self.left_form_layout.addRow("Height", self.height_field)
        self.left_form_layout.addRow("Weight", self.weight_field)

        # center_form_layout rows
        self.center_form_layout.addRow("Random", self.pc_nmgen_but)
        self.center_form_layout.addRow("Race: ", self.race_cb)
        self.center_form_layout.addRow("Class: ", self.pc_class_cb)
        self.center_form_layout.addRow("Hair:", self.hair_color_field)
        self.center_form_layout.addRow("Eyes:", self.eye_color_field)
        self.center_form_layout.addRow("Skin:", self.skin_color_field)

        # right_form_layout rows
        self.right_form_layout.addRow("HitDie:", self.hd_lbl)

        # Add forms to hbox_cont_layout
        self.hbox_cont_layout.addLayout(self.left_form_layout, 1.5)
        self.hbox_cont_layout.addLayout(self.center_form_layout, .5)
        self.hbox_cont_layout.addLayout(self.right_form_layout, 2)

        # Add form to container
        self.vbox_layout.addLayout(self.hbox_cont_layout)
        self.vbox_layout.addStretch(1)
        self.setLayout(self.vbox_layout)
        self.hbox_cont_layout.addStretch(1)

    # This is vital - sets the race correctly
    def set_race(self):
        return self.race_cb.currentText()

    # Run when the races combobox is activated
    @pyqtSlot()
    def race_cb_onActivated(self):
        race = self.race_cb.currentText()
        return race

    # Update Hitdice when class combobox is changed.
    @pyqtSlot()
    def class_cb_onActivated(self):
        self.pc_class = self.get_class()
        self.hd_lbl.setText(self.get_hd())

    # Run this when the random name generation button is clicked
    @pyqtSlot()
    def pc_nmgen_on_click(self):
        self.race = self.set_race()
        self.nmgen = ng.NameGen(str(self.race))
        self.nmgen.race = self.race_cb.currentText()
        name = self.nmgen.gen(self.nmgen.race)
        self.pc_name_field.setText(name)

    # Get races list from database
    def get_races(self):
        rc = self.curs.execute("SELECT race FROM races").fetchall()
        races = []

        for i in rc:
            races.append(i[0])
        return races

    # Get classes list from database
    def get_classes(self):
        cs = self.curs.execute("SELECT class FROM classes").fetchall()
        classes = []

        for i in cs:
            classes.append(i[0])
        return classes

    # Get current class
    def get_class(self):
        return self.pc_class_cb.currentText()

    # Get the hd from database
    def get_hd(self):
        hd = self.curs.execute("SELECT hit_dice FROM classes where class = '" +
                               self.pc_class + "'").fetchall()
        hd = str(hd[0][0])
        return hd
