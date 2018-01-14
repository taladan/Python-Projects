#!/usr/bin/python3
# -*- coding utf-8 -*-
"""
This file builds the attributes layout and contents of
the attributes tab in PyCGen.

Author: Taladan
Last Edited: December 22, 2017
"""
import random
from PyQt5 import QtWidgets
# from PyQt5 import QtGui
from PyQt5 import QtCore
from pycgFont import setFont as Font
from images import images
from pycgError import ErrorDialog as Err
from tools import Debugger as Debug


"""

Template class definition:


class template(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
"""


# Roll method selection
class RollMethod(QtWidgets.QWidget):

    def __init__(self):
        super().__init__(parent=None)

        # Call in the font class
        self.font = Font()

        # Set up widgets
        self.combobox_label = QtWidgets.QLabel("Pick a roll method:")
        self.combobox_label.setFont(self.font.text_font)
        self.combobox = QtWidgets.QComboBox()

        # Populate roll method list
        self._methods = ["Point Buy", "3d6", "3d6+3 Drop the Lowest", "4d6 Drop the Lowest", "5d6 Drop the Lowest 2"]

        # add items to the combobox
        self.combobox.addItems(self._methods)

        # Layout setup
        self.layoutContainer= QtWidgets.QVBoxLayout()
        self.layoutContainer.addWidget(self.combobox_label)
        self.layoutContainer.addWidget(self.combobox)

        self.setLayout(self.layoutContainer)
        self.show()

    def roll_method(self):
        return self.combobox.currentText()


# Handle the roll stuff
class DiceRoller:

    def __init__(self, parent=None):

        self.parent = parent

    def rolls(self, roll_method):

        if roll_method == "3d6":

            attrs = []
            for i in range(6):
                attrs.append(self.td6())

            return attrs

        elif roll_method == "3d6+3 Drop the Lowest":

            attrs = []
            for i in range(6):
                attrs.append(self.td6plus3())

            return attrs

        elif roll_method == "4d6 Drop the Lowest":

            attrs = []
            for i in range(6):
                attrs.append(self.frd6())

            return attrs

        elif roll_method == "5d6 Drop the Lowest 2":

            attrs = []
            for i in range(6):
                attrs.append(self.fvd6())

            return attrs

    def td6(self):

        rolls = []
        for i in range(3):
            rolls.append(self.roll())

        total = sum(rolls)
        return total

    def td6plus3(self):

        rolls = []
        for i in range(3):
            rolls.append(self.roll())
        rolls.remove(min(rolls))
        total = sum(rolls)

        return total + 3

    def frd6(self):

        rolls = []
        for i in range(4):
            rolls.append(self.roll())
        rolls.remove(min(rolls))
        total = sum(rolls)

        return total

    def fvd6(self):

        rolls = []
        for i in range(5):
            rolls.append(self.roll())

        rolls.remove(min(rolls))
        rolls.remove(min(rolls))
        total = sum(rolls)

        return total
    def roll(self):
        return random.randrange(1, 7)


# Handles the title and roll display
class RollsDisplayWidget(QtWidgets.QWidget):

    def __init__(self, rolls, parent=None):
        super().__init__()

        # set up the fonts
        self.parent = parent
        f = Font()
        self.title_font = f.title_font
        self.number_font = f.number_font

        # Update the labels
        self.currentRolls(rolls)

        # set up layout
        self.title_line_layout = QtWidgets.QHBoxLayout()
        self.roll_line_layout = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QVBoxLayout()

        # Widgets
        self.title = QtWidgets.QLabel("Your Rolls")
        self.title.setFont(self.title_font)

        # Label creation
        self.roll_label = QtWidgets.QLabel()
        self.roll_label.setFont(self.number_font)
        self.roll_label.setText(self.currentRolls(rolls))

        # Roll line
        self.roll_line_layout.addWidget(self.roll_label)
        self.roll_line_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Put layouts into widgets
        self.title_line_layout.addWidget(self.title)
        self.title_line_layout.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addLayout(self.title_line_layout)
        self.layout.addStretch(1)
        self.layout.addLayout(self.roll_line_layout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)
        self.show()

    # Update the labels
    def currentRolls(self, rolls):
        temp_rolls = []
        for roll in rolls:
            temp_rolls.append(str(roll))
        return ' '.join(temp_rolls)


# Layout for the current rolls in the roll popup
class CurrentRoll(QtWidgets.QWidget):
    def __init__(self, stats):
        super().__init__()

        self.stat_rolls = stats

        # Font setup
        f = Font()
        self.number_font = f.big_number_font

        # Widgets setup
        self.title = QtWidgets.QLabel("Current Roll")
        self.title.setFont(f.title_font)

        self.cr_lbl = QtWidgets.QLabel()
        self.cr_lbl.setFont(self.number_font)
        self.update_lbl(self.stat_rolls)
        self.cr_lbl.setAlignment(QtCore.Qt.AlignCenter)

        # Add widgets to layout
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.title)
        self.vbox.addWidget(self.cr_lbl)
        self.vbox.addStretch(1)
        self.setLayout(self.vbox)

    def update_lbl(self, rolls):
        try:
            self.cr_lbl.setText(str(rolls[0]))
        except TypeError:
            error = Err()
            error.popup("Rolled on a wrong type")
            error.setGeometry(200, 200, 200, 200)


# Handle the roll popup window
class RollWindow(QtWidgets.QDialog):

    def __init__(self, attrs, roll_method, parent=None):

        super().__init__()
        self.parent = parent
        self.attrs = attrs
        self.stat_rolls = DiceRoller()
        self.rolls = self.stat_rolls.rolls(roll_method)

        # Set the window title
        self.setWindowTitle("Your Attribute Rolls")

        # Setup layout stuff
        self.bbox = QtWidgets.QHBoxLayout()
        self.vbox = QtWidgets.QVBoxLayout()
        self.hbox = QtWidgets.QHBoxLayout()
        self.grid = QtWidgets.QGridLayout()

        # Lock to check for reroll
        self.roll_lock = False

        # Roll stuff
        self.current_roll = CurrentRoll(self.rolls)

        # Radio button setup
        self.rb_widget = RadioButtonGroup(self.attrs)

        # Title rolls setup
        self.title_rolls = RollsDisplayWidget(self.rolls)

        # Button stuff
        self.apply_button = QtWidgets.QPushButton('&Apply')
        self.cancel_button = QtWidgets.QPushButton('&Cancel')
        self.reroll_button = QtWidgets.QPushButton('&Reroll')
        self.apply_button.clicked.connect(self.on_apply)
        self.cancel_button.clicked.connect(self.on_cancel)
        self.reroll_button.clicked.connect(self.on_reroll)

        # Add widgets to layout and display
        self.bbox.addWidget(self.reroll_button)
        self.bbox.addStretch(1)
        self.bbox.addWidget(self.apply_button)
        self.bbox.addWidget(self.cancel_button)
        self.vbox.addWidget(self.title_rolls)
        self.vbox.addStretch(1)
        self.hbox.addWidget(self.current_roll)
        self.hbox.addWidget(self.rb_widget)
        self.vbox.addLayout(self.hbox)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.bbox)
        self.setLayout(self.vbox)
        self.show()

    # run the cancel button
    def on_cancel(self):

        if all(v is not False for v in self.attrs.values()):
            self.close()
        else:
            for k in self.attrs.keys():
                self.attrs[k] = None
                self.close()

    # run the reroll button
    def on_reroll(self):
        if self.roll_lock:
            font = Font()
            self.w = Err()
            self.w.popup("No rerolls after setting attribute")
            self.w.setFont(font.text_font)
            self.w.setGeometry(QtCore.QRect(100, 100, 150, 150))
            self.w.show()
        else:
            die = DiceRoller()
            self.stat_rolls = die.rolls(self.roll_method)
            self.title_rolls.update_lbls(self.stat_rolls)
            self.current_roll.cr_lbl.setText(str(self.stat_rolls[0]))

    # run the apply button
    def on_apply(self):
        # disable reroll button
        self.reroll_button.setEnabled(False)

        # Get the button that's checked
        key = self.rb_widget.get_checked()

        # disable the assigned button
        self.rb_widget.update_buttons(self.attrs)

        # Remove current roll and set it to attributes and update the labels
        self.attrs[key] = self.stat_rolls.pop(0)
        self.title_rolls.update_lbls(self.stat_rolls)
        try:
            self.current_roll.update_lbl(self.stat_rolls)
        except IndexError:
            self.apply_button.setEnabled(False)
            self.cancel_button.setText('Finish')

        self.roll_lock = True
        self.uncheck_button(key)

    def uncheck_button(self, key):

        button = self.rb_widget.buttons[key]
        button.setAutoExclusive(False)
        button.setChecked(False)
        button.setAutoExclusive(True)


# Create the pycg radiobutton stylesheet
class RadioButtonStylesheet(QtWidgets.QWidget):

    def __init__(self, text, parent=None):
        super().__init__(parent=parent)
        self.RadioButton = QtWidgets.QRadioButton(text)
        self.RadioButton.setStyleSheet(
            """
            QRadioButton::indicator::unchecked {
            image: url(:images/rdo-unchecked.png);}
            QRadioButton::indicator::unchecked::hover {
            image: url(:images/rdo-unchecked-over.png);}
            QRadioButton::indicator::unchecked::pressed {
            image: url(:images/rdo-uncheckea-pressed.png);}
            QRadioButton::indicator::checked {
            image: url(:images/rdo-checked.png);}
            QRadioButton::indicator::checked::hover {
            image: url(:images/rdo-checked-hover.png);}
            QRadioButton::indicator::checked::pressed {
            image: url(:images/rdo-checked-pressed.png);}
            QRadioButton { width: 25px; height: 25px;}""")


# Create the pycg radiobutton widget
class RadioButtonGroup(QtWidgets.QGroupBox):

    def __init__(self, attrs, parent=None):

        super().__init__()
        self.parent = parent
        self.lay = QtWidgets.QVBoxLayout(self)
        self.buttons = dict()
        self.build_widget(attrs)

    def update_buttons(self, attrs):

        self.checked = None
        self.buttons[self.get_checked()].setEnabled(False)

    def build_widget(self, attrs):

        for k in attrs.keys():
            w = RadioButtonStylesheet(k.title())
            self.rdobtn = w.RadioButton
            self.buttons[k] = self.rdobtn
            self.lay.addWidget(self.rdobtn)
        self.setLayout(self.lay)

    def get_checked(self):
        for k, v in self.buttons.items():
            if self.buttons[k].isChecked():
                self.checked = k

        return self.checked


# Create label objects for attributes - includes attribute value and attr mod value
class AttributeModLabel(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent
        self.font = Font()

    def pycg_label(self, attr):
        _attrval = str(attr)
        _modval = str(self.calculate_mod(attr))
        self._string = _attrval + " -- " + _modval
        self.label = QtWidgets.QLabel(self._string)
        self.label.setFont(self.font.med_number_font)
        self.label.setMaximumWidth(200)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        return self.label

    def calculate_mod(self, attr):
        if attr:
            value = (self.attrs[attr] - 10) // 2
            if value >= 0:
                value = "+" + str(value)
            else:
                value = str(value)
            return value
        else:
            value = " "
            return value


# Point Buy window
class PointBuyWindow(QtWidgets.QWidget):

    def __init__(self, attrs, parent=None):
        super().__init__(parent=None)

        # Set up necessary variables
        self.font = Font()
        self.attrs = attrs
        self.parent = parent

        # Points available
        self._points = 16
        self._total_points = 75

        # Widgets setup
        self._header = QtWidgets.QLabel("Points Left:")
        self._points_remaining = QtWidgets.QLabel(str(self._points - 1))

        # TODO:
        """Fix buttons for this window and finish up layout and application"""
        self.okay_button = QtWidgets.QPushButton("Okay")
        self.close_button = QtWidgets.QPushButton("Close")

        # Layout setup
        self.layout = QtWidgets.QVBoxLayout()
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.header_layout = QtWidgets.QHBoxLayout()
        self.form_layout = QtWidgets.QFormLayout()

        # Labels fonts assignments
        self._header.setFont(self.font.text_font)
        self._points_remaining.setFont(self.font.med_number_font)

        # Set up attribute stuff
        self.attrs = attrs
        self._setAttributes()

        # Label widgets
        self._attribute_labels = {}
        self._buildWidgets()

        for label, widget in self._attribute_labels.items():
            self.form_layout.addRow(label.title() + ": ", widget)
            self.form_layout.labelForField(widget).setFont(self.font.text_font)

        self.header_layout.addWidget(self._header)
        self.header_layout.addWidget(self._points_remaining)
        self.layout.addLayout(self.header_layout)
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.buttons_layout)
        self.setLayout(self.layout)
        self.show()
        self.setWindowTitle("Attributes - Point Buy")

    # Sets attributes to a base value of 10 for our point pool
    def _setAttributes(self):

        for attribute in self.attrs.keys():
            self.attrs[attribute] = 10

    # Build the spinboxes and lock them to the range of 3-18.  Check the totals when the values are changed
    def _buildWidgets(self):

        for attribute, total in self.attrs.items():
            self._attribute_labels[attribute] = QtWidgets.QSpinBox()
            self._attribute_labels[attribute].setMaximumWidth(75)
            self._attribute_labels[attribute].setRange(3, 18)
            self._attribute_labels[attribute].setValue(total)
            self._attribute_labels[attribute].valueChanged.connect(self._calculateTotal)
            self._attribute_labels[attribute].setFont(self.font.text_number_font)

    # Calculate the total amount of points used
    def _calculateTotal(self, index):
        sender = self.sender()
        total = 0

        for label in self._attribute_labels.values():
            total = total + label.value()

        if total == self._total_points + 1:
            sender.setValue(sender.value() - 1)
        else:
            self._points = self._total_points - total
            self._points_remaining.setText(str(self._points))


# Handle attribute tab display
class BuildAttributesTab(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent
        self.font = Font()

        self.attrs = {'str': False, 'dex': False, 'con': False,
                      'int': False, 'wis': False, 'cha': False}

        """
        Widgets section
        """
        # Attribute labels
        self.mklbl = AttributeModLabel()
        self.strLbl = self.mklbl.pycg_label(self.attrs["str"])
        self.dexLbl = self.mklbl.pycg_label(self.attrs["dex"])
        self.conLbl = self.mklbl.pycg_label(self.attrs["con"])
        self.intLbl = self.mklbl.pycg_label(self.attrs["int"])
        self.wisLbl = self.mklbl.pycg_label(self.attrs["wis"])
        self.chaLbl = self.mklbl.pycg_label(self.attrs["cha"])

        # Labels references
        self.attr_lbls = {"str": self.strLbl, "dex": self.dexLbl,
                          "con": self.conLbl, "int": self.intLbl,
                          "wis": self.wisLbl, "cha": self.chaLbl}

        # Roll Method
        self.method_widget = RollMethod()
        self.method_widget.combobox.activated[str].connect(self.set_roll_method)
        self.roll_method = self.set_roll_method()


        # Roll button
        self.roll_but = QtWidgets.QPushButton("&Roll")
        self.roll_but.setMaximumWidth(150)
        self.roll_but.clicked.connect(self.roll)

        # Attributes layout
        self.grid = QtWidgets.QGridLayout()
        self.att_form = QtWidgets.QFormLayout()
        self.mod_form = QtWidgets.QFormLayout()
        self.button_lay = QtWidgets.QHBoxLayout()
        self.layout = QtWidgets.QVBoxLayout()

        for lbl, widget in self.attr_lbls.items():
            self.att_form.addRow(lbl.title() + ":", widget)
            self.att_form.labelForField(widget).setFont(self.font.text_font)

        # Layout buttons
        self.button_lay.addStretch(1)
        self.button_lay.addWidget(self.roll_but)
        self.button_lay.addStretch(1)

        # Layout attributes
        self.grid.addLayout(self.att_form, 0, 0)
        self.grid.addLayout(self.mod_form, 0, 1)

        # Roll method Layout
        self.button_lay.addWidget(self.method_widget)
        # overall layout
        self.layout.addLayout(self.grid)
        self.layout.addStretch(1)
        self.layout.addLayout(self.button_lay)
        self.setLayout(self.layout)

    def set_roll_method(self):
        self.roll_method = self.method_widget.roll_method()

    def roll(self):

        self.set_roll_method()

        if self.roll_method == "Point Buy":
            self.point_buy = PointBuyWindow(self.attrs)
            self.point_buy.setGeometry(200, 200, 200, 200)

        else:
            self.die = RollWindow(self.attrs, self.roll_method)
            self.die.exec_()
            self.die.setWindowTitle("Your Stat Roll")
            for key, value in self.attr_lbls.items():
               value.setText(str(self.attrs[key]))
