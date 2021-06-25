#! /usr/bin/env python3
import random
import pygame

""" start player classes """


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        rand_monster = random.randint(1, 5)
        if rand_monster == 1:
            self.image = pygame.image.load(
                'image/pink_monster_l.png').convert()
        elif rand_monster == 2:
            self.image = pygame.image.load(
                'image/blue_monster_l.png').convert()
        elif rand_monster == 3:
            self.image = pygame.image.load(
                'image/red_monster_l.png').convert()
        elif rand_monster == 4:
            self.image = pygame.image.load(
                'image/slime_monster.png').convert()
        elif rand_monster == 5:
            self.image = pygame.image.load(
                'image/eyeball_monster.png').convert()

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()


class Monster(Enemy):

    def __init__(self, x, y, end, race, gold):
        Enemy.__init__(self)
        self.x = x
        self.y = y

        self.end = end
        self.path = [x, end]
        self.vel = 1

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

    def approach_player(self, x, y):
        if self.x - x > 0:
            self.x -= self.vel
        elif self.x - x <= 0:
            self.x += self.vel
        if self.y - y > 0:
            self.y -= self.vel
        elif self.y - y <= 0:
            self.y += self.vel

    def update(self, x, y) -> None:
        # self.move()
        self.approach_player(x, y)


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
