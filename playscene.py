#! /usr/bin/env python3
import pygame
import pygame.mixer
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

    # create hero1 and monster, and set monster location
    hero1 = players.Player("hero1")
    (background, monster_list) = rand_scene(bg_list, hero1)

    clock = pygame.time.Clock()

    player_list = pygame.sprite.Group()
    player_list.add(hero1)

    frame_count = 0
    attack_frame = 0
    randx = random.randint(-60, 60)
    randy = random.randint(-30, 30)
    """game loop"""
    while True:
        frame_count += 1
        '''death detection. comment these lines if you wish'''
        if hero1.isDead():
            break

        if len(monster_list) == 0:
            # play switch level sound
            sls = pygame.mixer.Sound('found_sound/switch_level.wav')
            sls.play()
            time.sleep(.5)
            (background, monster_list) = rand_scene(bg_list, hero1)

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

        # play attack sound
        if attack:
            attack_sound = pygame.mixer.Sound('found_sound/attack.wav')
            attack_sound.play()
            (text_surface, damage_list) = hero1.attack_monster(
                collide_monsters, monster_list)

        if attack or attack_frame > 0:
            # attack animation
            attack_frame += 1
            if attack_frame == 25:
                attack_frame = 0
            surface.blit(text_surface, (hero1.rect.x, hero1.rect.y))
            for d in damage_list:
                surface.blit(d[0], (d[1] + 5, d[2] - 30))

        for m in monster_list:
            if frame_count == 20:
                randx = random.randint(-60, 60)
                randy = random.randint(-30, 30)
            m.update(hero1.rect.x + randx,
                     hero1.rect.y + randy)
            m.rect.x = m.x
            m.rect.y = m.y

        monster_list.draw(surface)
        pygame.display.flip()


def rand_scene(bg_list, hero):
    index = random.randint(0, len(bg_list)-1)
    last = bg_list[index]
    background = pygame.image.load(last).convert()
    resx = 1024
    resy = 0
    if last == 'image/bg0.png':
        resy = 450
        hero.setPlayGround(resx, resy)
        hero.setPos(100, 500)
    elif last == 'image/bg4.png':
        resy = 0
        hero.setPlayGround(resx, resy)
    monster_list = pygame.sprite.Group()
    for i in range(random.randint(4, 7)):
        x = random.randint(0, 10)
        if x < 5:
            monster = monsters.Slime()
        elif x <= 10:
            monster = monsters.Eyeball()
        monster.setPlayGround(resx, resy)
        monster_list.add(monster)

    return background, monster_list


if __name__ == "__main__":
    main()
