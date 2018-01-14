#!/usr/bin/python3
# -*- coding: utf8 -*-

"""
ndl.py - name downloader

this will (hopefully) go out and get names from fantasygenerator.com
and dump them somehow.

Author: Taladan
Last Edited: December 8, 2017
"""
import requests

races = ['Aarakocra', 'Aasimar', 'Bugbear', 'Changeling', 'Dragonborn', 'Dwarf',
         'Elf', 'Firbolg', 'Genasi', 'Gnome', 'Goblin', 'Goliath', 'Halfling',
         'Halfelf', 'Halforc', 'Human', 'Hobgoblin', 'Kenku', 'Kobold', 'Kor',
         'Lizardfolk', 'Merfolk', 'Minotaur', 'Orc', 'Shifter', 'Tabaxi',
         'Tieflig', 'Triton', 'Vampire', 'Warforged', 'Yuan-ti']


def drow_script():
    f = open('Goblin.txt', 'w')
    url = "http://www.fantasynamegenerators.com/scripts/goblinNormal.js"
    results = requests.get(url)

    for result in results:
        f.write(str(result))

    f.close()


def get_script(rl):
    url_tp = ["http://www.fantasynamegenerators.com/scripts/dnd", ".js"]

    for i in enumerate(rl):
        race = i[1]
        url = [url_tp[0], race, url_tp[1]]
        url = ''.join(url)
        print(url)
        results = requests.get(url)

        f = open(race + '.txt', 'w')
        for result in results:
            f.write(str(result))

        f.close()


if __name__ == '__main__':

    drow_script()
