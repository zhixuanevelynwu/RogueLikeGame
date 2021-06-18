#! /usr/bin/env python3
''' An demo of our game '''
import pygame
import random
import controller
import model

def main():
    pygame.init()
    window_size_x = 640
    window_size_y = 640
    surface = pygame.display.set_mode([window_size_x, window_size_y])
    pygame.display.set_caption('Demo')
    background = pygame.image.load('image/bg.png').convert()
    # create hero and monster, and set monster location
    hero = model.Player('Adam')
    monster1 = model.Monster('monster', 0)
    monster1.rect.x = 200
    monster1.rect.y = 200
    monster2 = model.Monster('monster', 0)
    monster2.rect.x = 400
    monster2.rect.y = 400
    monster3 = model.Monster('monster', 0)
    monster3.rect.x = 300
    monster3.rect.y = 300
    speed = 1

    player_list = pygame.sprite.Group()
    player_list.add(hero)

    monster_list = pygame.sprite.Group()
    monster_list.add(monster1)
    monster_list.add(monster2)
    monster_list.add(monster3)

    while True:
        quit, up, down, left, right, up_up, down_up, left_up, right_up = controller.KeyEvents.check_events()
        if quit:
            break
        if up:
            hero.move(0, -speed)
        if up_up:
            hero.move(0, speed)
        if down:
            hero.move(0, speed)
        if down_up:
            hero.move(0, -speed)
        if left:
            hero.move(-speed, 0)
        if left_up:
            hero.move(speed, 0)
        if right:
            hero.move(speed, 0)
        if right_up:
            hero.move(-speed, 0)

        hero.update()
        pygame.sprite.groupcollide(
            player_list, monster_list, False, True, collided=pygame.sprite.collide_circle)
        surface.blit(background, (0, 0))
        player_list.draw(surface)
        monster_list.draw(surface)
        pygame.display.flip()


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/hero.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.rect.x = 100
        self.rect.y = 100

    def move(self, x, y):
        self.movex += x
        self.movey += y

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if random.randint(0, 1) == 0:
            self.image = pygame.image.load('image/monster1.png').convert()
        else:
            self.image = pygame.image.load('image/monster2.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    main()
