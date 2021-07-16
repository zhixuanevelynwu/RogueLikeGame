#! /usr/bin/env python3
import random
import pygame
from views import weaponview


class Weapon(weaponview.Arms):

    def __init__(self, type, attack, cooldown):
        weaponview.Arms.__init__(self, type)
        '''
            type - type of the weapon(e.g. sword)
            attack - damage a weapon causes
            cooldown- time interval between two continuous attacks. impacts dps of a weapon
        '''
        self.type = type
        self.attack = attack
        self.cooldown = cooldown

    def cool_down(self):
        pass


class Sword(Weapon):
    def __init__(self):
        Weapon.__init__(self, "sword1", 5, 2)


class Arrow():
    def __init__(self):
        Weapon.__init__(self, "arrow", 7, 3)


class Wand():
    def __init__(self):
        Weapon.__init__(self, "wand", 9, 6)


class Spear():
    def __init__(self):
        Weapon.__init__(self, "spear", 6, 3)


class Axe():
    def __init__(self):
        Weapon.__init__(self, "axe", 8, 5)


class Hammer():
    def __init__(self):
        Weapon.__init__(self, "hammer", 9, .8)


def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1, 4)
    return total
