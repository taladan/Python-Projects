#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyCGen v0.1

This is a character generation program for 5th Edition
Dungeons and Dragons.

Author: Taladan
Last Edited: November 20, 2017
"""

from PyQt5.QtWidgets import (QAction, QApplication, QMainWindow, QTabWidget,
                             QVBoxLayout, QWidget)
# from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui
import sys


class Cgen(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Create the menu bar
        menu = self.menuBar()
        fileMenu = menu.addMenu('&File')
        editMenu = menu.addMenu('&Edit')
        viewMenu = menu.addMenu('&View')
        toolsMenu = menu.addMenu('&Tools')

        # File Menu Setup
        newAct = QAction('&New', self)
        openAct = QAction('&Open', self)
        saveasAct = QAction('Save as', self)
        saveAct = QAction('&Save', self)

        fileMenu.addAction(newAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveasAct)
        fileMenu.addAction(saveAct)

        # Edit Menu Setup

        # View Menu Setup

        # Tools Menu Setup

        # Handle the status bar
        self.statusBar().showMessage('Status: ')

        # Set Window Geometry and display it
        self.showMaximized()
        self.setWindowIcon(QtGui.QIcon('pycgen_icon.png'))
        self.setWindowTitle('PyCgen')

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.details = QWidget()
        self.attributes = QWidget()
        self.skills = QWidget()
        self.feats = QWidget()
        self.spells = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.details, "Details")
        self.tabs.addTab(self.attributes, "Attributes")
        self.tabs.addTab(self.skills, "Skills")
        self.tabs.addTab(self.feats, "Feats")
        self.tabs.addTab(self.spells, "Spells")

        # Create Details Tab
        self.details.layout = QVBoxLayout(self)
        self.details.setLayout(self.details.layout)

        # Create Attributes Tab
        self.attributes.layout = QVBoxLayout(self)
        self.attributes.setLayout(self.attributes.layout)

        # Create Skills Tab
        self.skills.layout = QVBoxLayout(self)
        self.skills.setLayout(self.skills.layout)

        # Create Feats Tab
        self.feats.layout = QVBoxLayout(self)
        self.feats.setLayout(self.feats.layout)

        # Create Spells Tab
        self.spells.layout = QVBoxLayout(self)
        self.spells.setLayout(self.spells.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    cg = Cgen()
    sys.exit(app.exec_())
