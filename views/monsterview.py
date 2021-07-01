import random
import pygame
import math


class Enemy(pygame.sprite.Sprite):

    def __init__(self, race):
        pygame.sprite.Sprite.__init__(self)
        self.race = race
        if self.race == "slime":
            self.image = pygame.image.load(
                'image/slime_monster.png').convert()
        elif self.race == "eyeball":
            self.image = pygame.image.load(
                'image/eyeball_monster.png').convert()

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.rand_point_x = self.x + random.randint(50, 300)
        self.rand_point_y = self.y + random.randint(40, 200)

    def walk(self, x, y):
        x += 30
        y += 30
        distx = self.x - x
        disty = self.y - y
        '''diagonal_dist = math.sqrt(distx**2 + disty**2)
        if diagonal_dist < 300:
            self.approach(distx, disty)
        else:
            self.stroll()'''
        self.approach(distx, disty)

    def approach(self, distx, disty):
        if distx > 0:
            self.x -= self.vel
        elif distx <= 0:
            self.x += self.vel
        if disty > 0:
            self.y -= self.vel
        elif disty <= 0:
            self.y += self.vel

    def stroll(self):
        '''distx = self.x - self.rand_point_x
        disty = self.y - self.rand_point_y
        if distx < 10 or disty < 10:
            self.rand_point_x = self.x + random.randint(50, 400)
            self.rand_point_y = self.y + random.randint(40, 200)
        if self.x - self.vel < 100:
            distx = -random.randint(50, 400)
        elif self.x + self.vel > 850:
            distx = random.randint(50, 400)
        if self.y - self.vel < 50:
            disty = -random.randint(50, 400)
        elif self.y + self.vel > 600:
            disty = random.randint(50, 400)
        self.approach(distx, disty)'''
        pass

    def update(self, x, y) -> None:
        self.walk(x, y)
