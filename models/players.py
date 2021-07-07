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
        self.weapon = weapons.Sword()
        self.attack += self.weapon.attack
        self.interval = 3
        self.frame_count = self.interval
        self.gold = 0

    def __str__(self):
        s = f'{self.name} has HLTH:{self.current_health}/{self.max_health}'
        s += f'\n ATTK:{self.attack}'
        '''
        if self.weapon:
            s += f'\n  Wielding a {self.weapon.name}'
        '''
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
        damage_list = []
        for mon in collide_monsters.values():
            for monster in mon:
                damage = self.attack + random.randint(-1, 3)
                monster.health -= damage
                damage_list.append((monster.vis_take_damage(
                    True, damage), monster.rect.x, monster.rect.y))
                if monster.health <= 0:
                    monster_list.remove(monster)
        return (self.vis_attack(True), damage_list)

    def get_health(self, value):
        if self.current_health + value <= self.max_health:
            self.current_health += value
        else:
            self.current_health = self.max_health

    def get_damage(self, value):
        if self.current_health > 0:
            self.current_health -= value
        if self.current_health <= 0:
            self.current_health = 0

    def isDead(self):
        return self.current_health == 0


def main():
    pass


if __name__ == "__main__":
    main()
