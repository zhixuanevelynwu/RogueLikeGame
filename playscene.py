#! /usr/bin/env python3
import pygame
import random
import controller
import time
from models import players
from models import monsters


def main():
    pygame.init()
    pygame.font.get_fonts()
    window_size_x = 1024
    window_size_y = 768
    surface = pygame.display.set_mode([window_size_x, window_size_y])
    pygame.display.set_caption('Demo')

    bg_list = ['image/bg0.png', 'image/bg4.png']

    (background, monster_list) = rand_scene(bg_list)

    # create hero1 and monster, and set monster location
    hero1 = players.Player("hero1")

    clock = pygame.time.Clock()

    player_list = pygame.sprite.Group()
    player_list.add(hero1)

    """game loop"""
    while True:
        '''death detection. comment these lines if you wish'''
        if hero1.isDead():
            break

        if len(monster_list) == 0:
            time.sleep(.5)
            (background, monster_list) = rand_scene(bg_list)

        speed = 3

        clock.tick(60)

        quit, up, down, left, right, up_up, down_up, left_up, right_up, attack, dash, dash_up = controller.KeyEvents.check_events()
        if quit:
            break
        if up:
            hero1.move(0, -speed)
        if up_up:
            hero1.move(0, speed)
        if down:
            hero1.move(0, speed)
        if down_up:
            hero1.move(0, -speed)
        if left:
            hero1.move(-speed, 0)
        if left_up:
            hero1.move(speed, 0)
        if right:
            hero1.move(speed, 0)
        if right_up:
            hero1.move(-speed, 0)

        hero1.update()

        collide_monsters = pygame.sprite.groupcollide(
            player_list, monster_list, False, False, collided=pygame.sprite.collide_circle)

        if collide_monsters:
            for mon in collide_monsters.values():
                for m in mon:
                    m.attack_player(hero1)

        surface.blit(background, (0, 0))
        player_list.draw(surface)

        hero1.draw_health(surface)

        if attack:
            text_surface = hero1.attack_monster(collide_monsters, monster_list)
            surface.blit(text_surface, (hero1.rect.x, hero1.rect.y))

        for m in monster_list:
            m.update(hero1.rect.x, hero1.rect.y)
            m.rect.x = m.x
            m.rect.y = m.y

        monster_list.draw(surface)
        pygame.display.flip()


def rand_scene(bg_list):
    index = random.randint(0, len(bg_list)-1)
    last = bg_list[index]
    background = pygame.image.load(last).convert()
    monster_list = pygame.sprite.Group()
    for i in range(random.randint(4, 7)):
        x = random.randint(0, 10)
        if x < 5:
            monster = monsters.Slime()
        else:
            monster = monsters.Eyeball()
        monster_list.add(monster)
    return background, monster_list


if __name__ == "__main__":
    main()
