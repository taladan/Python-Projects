#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This file builds the attributes layout and contents of
the attributes tab in PyCGen.

Author: Taladan
Last Edited: December 2, 2017
"""
from PyQt5.QtWidgets import (QFormLayout, QLineEdit, QVBoxLayout, QWidget)


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
        pc_name_field = QLineEdit()
        pc_name_field.setMaximumWidth(200)
        pl_name_field = QLineEdit()
        pl_name_field.setMaximumWidth(200)

        form_layout.addRow("PC Name: ", pc_name_field)
        form_layout.addRow("Player Name: ", pl_name_field)

        # Add form to container
        layout.addLayout(form_layout)
        layout.addStretch(1)

        self.setLayout(layout)
