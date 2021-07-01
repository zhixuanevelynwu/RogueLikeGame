#! /usr/bin/env python3
import random
from views import monsterview

""" start monster classes """


class Monster(monsterview.Enemy):

    def __init__(self, x, y, race, gold, health, interval, vel):
        '''
            interval - how many frames a monster wait to make the next attack
            frame_count - count the number of frames that has already passed
        '''
        monsterview.Enemy.__init__(self, race)
        self.x = x
        self.y = y
        self.vel = vel
        self.race = race
        self.attack = roll_3_dice()
        self.health = health
        self.gold = gold
        self.interval = interval
        self.frame_count = self.interval

    def __str__(self):
        s = f'Monster {self.race} with ATK:{self.attack} HLTH:{self.health}'
        return s

    def attack_player(self, player):
        '''attacks a player'''
        if self.frame_count == self.interval:
            player.get_damage(self.attack)
            self.frame_count = 0
        self.frame_count += 1

    def isDead(self):
        return self.health <= 0


class Eyeball(Monster):
    """
        killing an eyeball rewards player 5 gold
    """

    def __init__(self):
        Monster.__init__(self, random.randint(
            40, 720), random.randint(40, 550), "eyeball", 5, 20, 70, 1)
        self.yell = '"SsSsSSss"'

    def __str__(self):
        pass


class Slime(Monster):
    """
        killing a slime rewards player 6 gold
    """

    def __init__(self):
        Monster.__init__(self, random.randint(
            40, 720), random.randint(40, 550), "slime", 6, 30, 80, .5)
        self.yell = '"#%@&$/?!"'

    def __str__(self):
        pass


""" end monster classes """


def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1, 3)
    return total


def main():
    pass


if __name__ == "__main__":
    main()
