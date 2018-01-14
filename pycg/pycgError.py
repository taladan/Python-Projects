#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This holds error message dialogs/handling

Author: Taladan
Last Edited: December 18, 2017
"""
from PyQt5.QtWidgets import (QDialog, QHBoxLayout, QLabel,
                             QPushButton, QVBoxLayout)


# Errors pass through this to pop a dialog
class ErrorDialog(QDialog):

    def __init__(self):

        super().__init__()

    def popup(self, message):

        # Set the window's title:
        self.setWindowTitle("PyCGen Error")

        # Label stuff
        self.label = QLabel(message)

        # Button stuff
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.c)
        self.close_button.setMaximumWidth(100)

        # layout stuff
        layout = QVBoxLayout()
        hbox = QHBoxLayout()
        layout.addWidget(self.label)
        hbox.addStretch(1)
        hbox.addWidget(self.close_button)
        hbox.addStretch(1)
        layout.addStretch(1)
        layout.addLayout(hbox)
        self.setLayout(layout)

    def c(self):

        self.close()
