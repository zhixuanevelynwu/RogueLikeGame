#! /usr/bin/env python3
''' An demo of our game '''
import pygame
import random
import controller
from models import players
from models import monsters


def main():
    pygame.init()
    window_size_x = 640
    window_size_y = 640
    surface = pygame.display.set_mode([window_size_x, window_size_y])
    pygame.display.set_caption('Demo')
    background = pygame.image.load('image/bg2.png').convert()
    # create hero1 and monster, and set monster location
    hero1 = players.Player()

    clock = pygame.time.Clock()
    speed = 4

    player_list = pygame.sprite.Group()
    player_list.add(hero1)

    monster_list = pygame.sprite.Group()
    for i in range(random.randint(3, 6)):
        monster = monsters.Monster(random.randint(40, 600), random.randint(40, 600), 640, 'monster', 0)
        monster_list.add(monster)

    """game loop"""
    while True:

        clock.tick(60)

        quit, up, down, left, right, up_up, down_up, left_up, right_up = controller.KeyEvents.check_events()
        if quit:
            break
        elif up:
            hero1.move(0, -speed)
            hero1.begin_anim()
        elif up_up:
            hero1.move(0, speed)
            hero1.end_anim()
        elif down:
            hero1.move(0, speed)
            hero1.begin_anim()
        elif down_up:
            hero1.move(0, -speed)
            hero1.end_anim()
        elif left:
            hero1.move(-speed, 0)
            hero1.begin_anim()
        elif left_up:
            hero1.move(speed, 0)
            hero1.end_anim()
        elif right:
            hero1.move(speed, 0)
            hero1.begin_anim()
        elif right_up:
            hero1.move(-speed, 0)
            hero1.end_anim()

        hero1.update()
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


if __name__ == "__main__":
    main()
