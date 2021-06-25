#! /usr/bin/env python3
import random
import pygame

""" start player classes """


class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)
        self.animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('image/hero_f1.png'))
        self.sprites.append(pygame.image.load('image/hero_f2.png'))
        self.sprites.append(pygame.image.load('image/hero_f3.png'))
        self.out_of_pic = False
        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.rect.x = 100
        self.rect.y = 100
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

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.animating = False
        self.sprites = []
        self.sprites.append(pygame.image.load('image/hero_f1.png'))
        self.sprites.append(pygame.image.load('image/hero_f2.png'))
        self.sprites.append(pygame.image.load('image/hero_f3.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.rect.x = 100
        self.rect.y = 100

    def move(self, x, y):
        self.movex += x
        self.movey += y

    def begin_anim(self):
        self.animating = True

    def end_anim(self):
        self.animating = False

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        if self.animating:
            self.current += 0.1
            if self.current >= len(self.sprites):
                self.current = 0
            self.image = self.sprites[int(self.current)]
        if self.rect.x > 1024 or self.rect.y > 768:
            self.out_of_pic = True
            # print(self.out_of_pic)


def main():
    pass


def roll_3_dice():
    total = 0
    for _ in range(3):
        total += random.randrange(1, 7)
    return total


if __name__ == "__main__":
    main()
