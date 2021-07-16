import random
import pygame
import math


class Arms(pygame.sprite.Sprite):

    def __init__(self, item):
        pygame.sprite.Sprite.__init__(self)
        self.item = item
        self.sprites = []
        if self.item == "sword1":
            self.sprites.append(pygame.image.load('image/weapons/null.png'))
            self.sprites.append(pygame.image.load('image/weapons/sword1.png'))
            self.sprites.append(pygame.image.load('image/weapons/sword1_L.png'))

        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = -100
        self.rect.y = -100

        self.ani_x = 0

        self.attacking = False
        self.attack_range = 2

    def update(self, x, y) -> None:
        pass

    def vis_attack(self, left):
        self.attacking = True
        if left:
            self.ani_x -= self.attack_range
            self.image = self.sprites[2]
        else:
            self.ani_x += self.attack_range
            self.image = self.sprites[1]

    def vis_def(self):
        self.attacking = False
        self.ani_x = 0
        self.image = self.sprites[0]

    def upgrade(self, new_range):
        self.attack_range = new_range


