#!/usr/bin/python3
# -*- coding utf-8 -*-

"""
Spud 1 - for constructing a qapplication
so I can import and use namegen.

Testing tool - not for production use

Author: Taladan
Last Edited: December 7, 2017
"""

import sys
from PyQt5 import QtWidgets
import namegen as ng
import importlib as imp

app =  QtWidgets.QApplication(sys.argv)
g = ng.NameGen('elf')
