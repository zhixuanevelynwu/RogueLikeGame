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

    clock = pygame.time.Clock()
    speed = 4

    player_list = pygame.sprite.Group()
    player_list.add(hero)

    monster_list = pygame.sprite.Group()
    for i in range(random.randint(3, 6)):
        monster = model.Monster(random.randint(40, 600), random.randint(40, 600), 640, 'monster', 0)
        monster_list.add(monster)

    """game loop"""
    while True:

        clock.tick(60)

        quit, up, down, left, right, up_up, down_up, left_up, right_up = controller.KeyEvents.check_events()
        if quit:
            break
        if up:
            hero.move(0, -speed)
            hero.begin_anim()
        if up_up:
            hero.move(0, speed)
            hero.end_anim()
        if down:
            hero.move(0, speed)
            hero.begin_anim()
        if down_up:
            hero.move(0, -speed)
            hero.end_anim()
        if left:
            hero.move(-speed, 0)
            hero.begin_anim()
        if left_up:
            hero.move(speed, 0)
            hero.end_anim()
        if right:
            hero.move(speed, 0)
            hero.begin_anim()
        if right_up:
            hero.move(-speed, 0)
            hero.end_anim()

        hero.update()
        pygame.sprite.groupcollide(
            player_list, monster_list, False, True, collided=pygame.sprite.collide_circle)
        surface.blit(background, (0, 0))
        player_list.draw(surface)

        for m in monster_list:
            m.update()
            m.rect.x = m.x
            m.rect.y = m.y

        monster_list.draw(surface)
        pygame.display.flip()


class Hero(pygame.sprite.Sprite):

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


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        if random.random() < 0.5:
            self.image = pygame.image.load('image/monster1.png').convert()
        else:
            self.image = pygame.image.load('image/monster2.png').convert()

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()


if __name__ == "__main__":
    main()
