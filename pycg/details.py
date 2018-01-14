#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This file builds the details layout and contents of
the details tab in PyCGen

Author: Taladan
Last Edited: December 8, 2017
"""
from PyQt5.QtCore import (QSize, pyqtSlot)
from PyQt5.QtGui import (QIcon, QFont)
from PyQt5.QtWidgets import (QComboBox, QFormLayout, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget)
import sqlite3
import namegen as ng
import tools.Debugger as Debug


class BuildDetailsTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):

        # Path settings
        self.img = './images/'

        # Module Name
        self.module_name = 'details.py'

        # Set up our database connection
        self.db = sqlite3.connect("pycg.db")
        self.curs = self.db.cursor()

        # Fonts setup
        self.lbl_font = QFont()
        self.lbl_font.setFamily("Free Mono")
        self.lbl_font.setPointSize(18)

        # Create widgets
        self.age_field = QLineEdit()
        self.hd_lbl = QLabel()
        self.height_field = QLineEdit()
        self.pc_class_cb = QComboBox()
        self.pc_level_cb = QComboBox()
        self.pc_name_field = QLineEdit()
        self.pc_nmgen_but = QPushButton()
        self.pl_name_field = QLineEdit()
        self.race_combo = QComboBox()
        self.sex_field = QLineEdit()
        self.weight_field = QLineEdit()

        # unconfigured
        self.bonds_field = QLineEdit()
        self.eye_color_field = QLineEdit()
        self.flaws_field = QLineEdit()
        self.hair_color_field = QLineEdit()
        self.ideals_field = QLineEdit()
        self.personality_trait_one_field = QLineEdit()
        self.personality_trait_two_field = QLineEdit()
        self.skin_color_field = QLineEdit()

        # name field width config
        self.pc_name_field.setMaximumWidth(200)
        self.pl_name_field.setMaximumWidth(200)

        # generator button config
        self.pc_nmgen_but.setIcon(QIcon(self.img + 'd20-icon.png'))
        self.pc_nmgen_but.setIconSize(QSize(15, 15))
        self.pc_nmgen_but.setToolTip('Generate a random PC name')
        self.pc_nmgen_but.clicked.connect(self.pc_nmgen_on_click)

        # Race selection combobox
        self.races = self.get_races()

        for i in range(len(self.get_races())):
            self.race_combo.addItem(self.races[i])

        self.race_combo.setCurrentIndex(15)
        self.race_combo.activated[str].connect(self.race_cb_onActivated)
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

        # Set widget sizes
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
        self.pc_nmgen_but.setMaximumWidth(50)
        self.race_combo.setMaximumWidth(100)
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
        self.center_form_layout.addRow("Race: ", self.race_combo)
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
        # I don't think this is necessary
        self.setLayout(self.vbox_layout)
        self.hbox_cont_layout.addStretch(1)

    # This is vital - sets the race correctly
    def set_race(self):
        return self.race_combo.currentText()

    # Run when the races combobox is activated
    @pyqtSlot()
    def race_cb_onActivated(self):
        return self.set_race()

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
        self.nmgen.race = self.race_combo.currentText()
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
        class_list = []

        for i in cs:
            class_list.append(i[0])
        return class_list

    # Get current class
    def get_class(self):
        return self.pc_class_cb.currentText()

    # Get the hd from database
    def get_hd(self):
        hd = self.curs.execute("SELECT hit_dice FROM classes where class = '" +
                               self.pc_class + "'").fetchall()
        hd = str(hd[0][0])
        return hd
