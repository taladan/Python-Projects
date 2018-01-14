#!/usr/bin/python3.6
import random


class Dice:

    def __init__(self, sides=0, num_dice=0, mod=0):
        self.sides = int(sides)
        self.num_dice = int(num_dice)
        if mod is None:
            self.mod = 0
        else:
            self.mod = int(mod)
        self.result = []

    def roll(self):
        if self.sides == 0:
            raise ValueError("Sides cannot be Zero.")

        if self.num_dice == 0:
            raise ValueError("Number of dice cannot be Zero")

        i = 0
        while i < self.num_dice:
            self.result.append(random.randrange(1, self.sides + 1, 1))
            i += 1
        return sum(self.result) + self.mod, self.result
