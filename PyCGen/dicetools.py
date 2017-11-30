#!/usr/bin/python3.6
# dicetools.py - Functions dealing with handling the various dice rolls needed
# for generating a character.  Main useful function is throw() - takes a string
# value in the format of '3d6' and passes it into the class object then returns
# the result.

import dice, re


def throw(player_string):
    pattern = r'^(\d+)d(\d+)([+|-]\d+)?$'
    matchObj = None
    matchObj = re.match(pattern, player_string)
    new_dice = dice.Dice(matchObj.group(2), matchObj.group(1), matchObj.group(3))
    result = new_dice.roll()
    return result


def advantage(*args):
    if args:
        modifier = args[0]
    else:
        modifier = 0
    roll = int(max(throw('2d20')[1]))
    return int(roll) + modifier


def disadvantage(*args):
    if args:
        modifier = args[0]
    else:
        modifier = 0
    roll = int(min(throw('2d20')[1]))
    return int(roll) + modifier


def check(ability, modifier):
    from character import abilities_order as abils
    if ability[0:3].lower() in abils:
        return throw('1d20+' + modifier)
    else:
        return "Ability Error: " + ability + " not in list of character abilities"
