#! /usr/bin/env python3
import pygame
import random
import controller
import time
from models import players
from models import monsters


def rand_scene(bg_list):
    index = random.randint(0, len(bg_list)-1)
    last = bg_list[index]
    background = pygame.image.load(last).convert()
    monster_list = pygame.sprite.Group()
    for i in range(random.randint(3, 6)):
        monster = monsters.Monster(random.randint(
            40, 600), random.randint(40, 600), 'monster', 0)
        monster_list.add(monster)
    return background, monster_list, last


def main():
    pygame.init()
    window_size_x = 1024
    window_size_y = 768
    surface = pygame.display.set_mode([window_size_x, window_size_y])
    pygame.display.set_caption('Demo')

    bg_list = ['image/bg1.png', 'image/bg2.png', 'image/bg3.png']
    (background, monster_list, last) = rand_scene(bg_list)

    # create hero1 and monster, and set monster location
    hero1 = players.Player("hero1")

    clock = pygame.time.Clock()

    player_list = pygame.sprite.Group()
    player_list.add(hero1)

    """game loop"""
    while True:
        if len(monster_list) == 0:
            time.sleep(.5)
            (background, monster_list, last_bg) = rand_scene(bg_list)

        speed = 3

        clock.tick(60)

        quit, up, down, left, right, up_up, down_up, left_up, right_up = controller.KeyEvents.check_events()
        if quit:
            break
        if up:
            hero1.move(0, -speed)
            hero1.begin_anim()
        if up_up:
            hero1.move(0, speed)
            hero1.end_anim()
        if down:
            hero1.move(0, speed)
            hero1.begin_anim()
        if down_up:
            hero1.move(0, -speed)
            hero1.end_anim()
        if left:
            hero1.move(-speed, 0)
            hero1.begin_anim()
        if left_up:
            hero1.move(speed, 0)
            hero1.end_anim()
        if right:
            hero1.move(speed, 0)
            hero1.begin_anim()
        if right_up:
            hero1.move(-speed, 0)
            hero1.end_anim()

        hero1.update()

        dead_monsters = pygame.sprite.groupcollide(player_list, monster_list, False, True, collided=pygame.sprite.collide_circle)

        if dead_monsters:
            for mon in dead_monsters.values():
                hero1.get_damage(mon[0].attack)

        surface.blit(background, (0, 0))
        player_list.draw(surface)

        hero1.draw_health(surface)

        for m in monster_list:
            m.update(hero1.rect.x, hero1.rect.y)
            m.rect.x = m.x
            m.rect.y = m.y

        monster_list.draw(surface)
        pygame.display.flip()


if __name__ == "__main__":
    main()
