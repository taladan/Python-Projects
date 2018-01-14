#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyCGen v0.1

This is a character generation program for 5th Edition
Dungeons and Dragons.

Author: Taladan
Last Edited: December 6, 2017
"""

import sys
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QShortcut
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from attributes import BuildAttributesTab
from details import BuildDetailsTab
from features import BuildFeaturesTab
from skills import BuildSkillsTab
from spells import BuildSpellsTab
from equipment import BuildEquipmentTab
from namegen import NameGen

# qtwidgets.qshortcut
# qtgui.qkeysequence


class Cgen(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        #Path stuff
        self.img = './images/'
        # Create the menu bar
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        # editMenu = menu.addMenu('&Edit')
        # viewMenu = menu.addMenu('&View')
        # toolsMenu = menu.addMenu('&Tools')

        # File Menu Setup
        # File Menu - New option configuration
        newAct = QtWidgets.QAction('&New', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('Create a new character')

        # File Menu - Open option configuration
        openAct = QtWidgets.QAction('&Open', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open a previously saved character')

        # File menu - Save option configuration
        saveAct = QtWidgets.QAction('&Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save character')

        # File menu - Save As option configuration
        saveasAct = QtWidgets.QAction('Sa&ve as', self)
        saveasAct.setStatusTip('Save character as')

        # File menu - Quit option configuration
        quitAct = QtWidgets.QAction('&Quit', self)
        quitAct.setShortcut('Ctrl+Q')
        quitAct.setStatusTip('Exit application')
        quitAct.triggered.connect(QtWidgets.qApp.quit)

        # Add actions to the file menu
        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveasAct)
        fileMenu.addAction(quitAct)

        """
        Menus are still a work in progress
        """
        # Edit Menu Setup
        # editMenu = menu.addMenu('&Edit')
        print("PyCGen -- main.py: InProg message -- TODO: Add edit menu stuff")

        # View Menu Setup
        # viewMenu = menu.addMenu('&View')
        print("PyCGen -- main.py: InProg message -- TODO: Add view menu stuff")

        # Tools Menu Setup
        self.ng = NameGen()
        toolsMenu = menu.addMenu('&Tools')
        nameGenAct = QtWidgets.QAction('Name &Generator', self)
        nameGenAct.setShortcut('Ctrl+G')
        # nameGenAct.triggered.connect(lambda: ng.show())

        toolsMenu.addAction(nameGenAct)

        # Handle the status bar
        self.statusBar().showMessage('Status: ')

        # Set Window Geometry and display it
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon(self.img + 'pycgen_icon.png'))
        self.setWindowTitle('PyCgen')

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QtWidgets.QWidget):

    def __init__(self, parent):
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QtWidgets.QTabWidget()
        self.details = BuildDetailsTab()
        self.attributes = BuildAttributesTab()
        self.skills = BuildSkillsTab()
        self.features = BuildFeaturesTab()
        self.spells = BuildSpellsTab()
        self.equipment = BuildEquipmentTab()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.details, "Details")

        # -- Commented out for troubleshooting

        self.tabs.addTab(self.attributes, "Attributes")
        self.tabs.addTab(self.features, "Features")
        self.tabs.addTab(self.skills, "Skills")
        self.tabs.addTab(self.spells, "Spells")
        self.tabs.addTab(self.equipment, "Equipment")

        # Add tabs to widget
        self.layout.addWidget(self.tabs)

        # Setup kb shortcuts for switching tabs
        self.tab_left_sc = QShortcut(QKeySequence("CTRL+PgUp"), self)
        self.tab_right_sc = QShortcut(QKeySequence("CTRL+PgDown"), self)
        self.tab_left_sc.activated.connect(self.tab_left)
        self.tab_right_sc.activated.connect(self.tab_right)

        """
        Current working position - I'm trying to get shortcuts in
        for switching tabs with CTRL+PGUP and CTRL+PGDN.  Currently
        it's throwing an error saying mytablewidget has no
        tab_lef
        """

    @pyqtSlot()
    def tab_left(self):
        self.tabs.setCurrentIndex(self.tabs.currentIndex() - 1)

    @pyqtSlot()
    def tab_right(self):
        self.tabs.setCurrentIndex(self.tabs.currentIndex() + 1)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    cg = Cgen()
    sys.exit(app.exec_())
