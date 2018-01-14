#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
dicetools.py

Functions dealing with handling the various dice rolls needed
for generating a character.  Main useful function is throw() - takes a string
value in the format of '3d6' and passes it into the class object then returns
the result.

Author: Taladan
Last Edited: December 8, 2017
"""
import dice
import re


class die:

    def throw(self, player_string):

        pattern = r'^(\d+)d(\d+)([+|-]\d+)?$'
        matchObj = None
        matchObj = re.match(pattern, player_string)
        new_dice = dice.Dice(matchObj.group(2),
                             matchObj.group(1),
                             matchObj.group(3))
        result = new_dice.roll()

        return result

    def advantage(self, *args):

        if args:
            modifier = args[0]
        else:
            modifier = 0

        roll = int(max(self.throw('2d20')[1]))

        return int(roll) + modifier

    def disadvantage(self, *args):

        if args:
            modifier = args[0]
        else:
            modifier = 0
        roll = int(min(self.throw('2d20')[1]))

        return int(roll) + modifier

    def check(self, ability, modifier):

        if ability[0:3].lower() in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            return self.throw('1d20+' + modifier)
        else:
            err = str("""Ability Error: """ + ability +
                      """ not in list of character abilities""")

            return err
