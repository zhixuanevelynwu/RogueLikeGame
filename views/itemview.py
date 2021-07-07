import random
import pygame
import math


class Drop(pygame.sprite.Sprite):

    def __init__(self, item, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.item = item
        self.sprites = []
        if self.item == "apple":
            self.sprites.append(pygame.image.load('image/drops/apple.png'))
        elif self.item == "blood_bottle":
            self.sprites.append(pygame.image.load('image/drops/blood_bottle.png'))
        elif self.item == "chicken_leg":
            self.sprites.append(pygame.image.load('image/drops/chicken_leg.png'))

        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self, x, y) -> None:
        pass


