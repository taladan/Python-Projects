#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
dp.py populates the data I need into the races table
of the pycg database.

Author: Taladan
Last Edit: December 3, 2017
"""

import sqlite3
import xlrd

# Set up the database connection
db = sqlite3.connect('pycg.db')
curs = db.cursor()

# Set up the excel data sheet
book = xlrd.open_workbook('dnd_class_info.xls')
sheet = book.sheet_by_index(0)


# Worksheet header
def get_header():
    row = sheet.row(0)
    header = []
    for i in row:
        header.append(i.value)
    return header


# get_row - returns the contents of the cells in a specific row
def get_row(rownum):
    rw = []
    for i in sheet.row(rownum):
        rw.append(i.value)
    row = [rw]
    return row


# This does the biz.
def db_post():
    sql = """INSERT INTO classes (class, hit_dice, armor_prof, weapon_prof,
    tool_prof, saving_throws, skills_available) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    for i in range(1, sheet.nrows):
        row = get_row(i)
        curs.executemany(sql, row)


if __name__ == '__main__':
    db_post()
    db.commit()
