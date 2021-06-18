#! /usr/bin/env python3
import random
import view

""" start player classes """
class Player(view.Hero):
    def __init__(self, name):
        view.Hero.__init__(self)
        """ Initialize with a name.  Rolls dice for ST/IN"""
        self.name = name
        self.health = 50
        self.weapon = False
        self.gold = 0

    def __str__(self):
        s = f'{self.name} has HLTH:{self.health}'
        if self.weapon:
            s += f'\n  Wielding a {self.weapon.name}'
        return s

    def get_gold(self, gold):
        """Call when player finds gold"""
        self.gold += gold

    def arm(self, weapon=False):
        """Put on a weapon.  Call disarm to take off."""
        if not self.weapon:
            self.weapon = weapon

    def attack(self, monster):
        """atacks a monster"""
        pass

    def isDead(self):
        pass
""" end player classes """

""" start monster classes """
class Monster(view.Enemy):

    def __init__(self, x, y, end, race, gold):
        view.Enemy.__init__(self)
        self.x = x
        self.y = y

        self.end = end
        self.path = [x, end]
        self.vel = 3


        self.race = race
        self.attack = roll_3_dice()
        self.health = roll_3_dice()
        self.gold = gold

        self.move()

    def __str__(self):
        s = f'Encounter Monster {self.race} with ATK:{self.attack} HLTH:{self.health}'
        return s

    def attack(self, player):
        pass

    def isDead(self):
        pass

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1

    def update(self, *args, **kwargs) -> None:
        self.move()


# class Eyeball(Monster):
#     """
#         killing an eyeball rewards player 5 gold
#     """
#
#     def __init__(self):
#         Monster.__init__(self, "eyeball", 5)
#         self.yell = '"SsSsSSss"'
#
#     def __str__(self):
#         pass
#
# class Slime(Monster):
#     """
#         killing a slime rewards player 6 gold
#     """
#     def __init__(self):
#         Monster.__init__(self, "Slime", 6)
#         self.yell = '"#%@&$/?!"'
#
#     def __str__(self):
#         pass
#
# """ end monster classes """

def main():
    pass

def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1, 7)
    return total

if __name__ == "__main__":
    main()
