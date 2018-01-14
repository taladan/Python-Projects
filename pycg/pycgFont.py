#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
Font settings for Pycgen

Author: Taladan
Last Edited: December 21, 2017
"""

from PyQt5.QtGui import QFont


class setFont:
    def __init__(self):
        self.title_font = QFont("MathJax_Calligraphic", 20)
        self.text_font = QFont("MathJax_Calligraphic", 14)
        self.text_number_font = QFont("Purisa", 14)
        self.big_number_font = QFont("Purisa", 38)
        self.med_number_font = QFont("Purisa", 24)
        self.number_font = QFont("Purisa", 20)
