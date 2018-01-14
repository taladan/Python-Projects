#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This file builds the attributes layout and contents of
the attributes tab in PyCGen.

Author: Taladan
Last Edited: December 2, 2017
"""
from PyQt5.QtWidgets import (QFormLayout, QVBoxLayout, QWidget)


class BuildFeaturesTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # Declare variables necessary for attributes tab

        # Create QVBoxLayout - Whole form
        layout = QVBoxLayout()

        # Create QFormLayout - manages labeled fields and controls
        form_layout = QFormLayout()

        # Create widgets

        # Add form to container
        layout.addLayout(form_layout)
        layout.addStretch(1)

        self.setLayout(layout)
