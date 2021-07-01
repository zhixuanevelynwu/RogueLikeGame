#! /usr/bin/env python3
import random
from models import weapons
from views import playerview

""" start player classes """


class Player(playerview.Hero):
    def __init__(self, name):
        playerview.Hero.__init__(self)
        """ Initialize with a name. """
        self.name = name
        self.attack = random.randrange(1, 5)
        # weapon is temporarily set to sword by default for easier development.
        self.weapon = weapons.Sword()
        self.interval = 3
        self.frame_count = self.interval
        self.attack += self.weapon.attack
        self.gold = 0

    def __str__(self):
        s = f'{self.name} has HLTH:{self.current_health}'
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

    def attack_monster(self, collide_monsters, monster_list):
        """attacks a monster"""
        self.frame_count = 0
        for mon in collide_monsters.values():
            for monster in mon:
                monster.health -= self.attack
                if monster.health <= 0:
                    monster_list.remove(monster)
        return self.vis_attack(True)

    def get_health(self, value):
        if self.current_health < self.max_health:
            self.current_health += value
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

    def get_damage(self, value):
        if self.current_health > 0:
            self.current_health -= value
        if self.current_health <= 0:
            self.current_health = 0

    def isDead(self):
        return self.current_health == 0

    def move(self, x, y):
        self.movex += x
        self.movey += y


def main():
    pass


if __name__ == "__main__":
    main()
