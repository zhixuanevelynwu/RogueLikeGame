#! /usr/bin/env python3
import pygame
import pygame.mixer
import random
import controller
from models import players
from models import monsters
from models import items
from views import sceneview


def main():
    pygame.init()
    pygame.font.get_fonts()
    window_size_x = 1024
    window_size_y = 768
    surface = pygame.display.set_mode([window_size_x, window_size_y])
    pygame.display.set_caption('Demo')

    # load sounds
    sls = pygame.mixer.Sound('found_sound/switch_level.wav')
    pick_sound = pygame.mixer.Sound('found_sound/pick_up.wav')
    attack_sound = pygame.mixer.Sound('found_sound/attack.wav')

    # icons
    arrow = []
    arrow.append(pygame.image.load(
        'image/icons/arrow/arrow_0.png'))
    arrow.append(pygame.image.load(
        'image/icons/arrow/arrow_1.png'))

    # create hero1 and monsters
    hero1 = players.Player("hero1")
    (scene, monster_list) = rand_scene(hero1)
    background = scene.background

    clock = pygame.time.Clock()

    player_list = pygame.sprite.Group()
    player_list.add(hero1)

    frame_count = 0
    attack_frame = 0
    icon_index = 0

    item_list = pygame.sprite.Group()
    """game loop"""
    while True:
        frame_count += 1
        '''death detection. comment these lines if you wish'''
        # if hero1.isDead():
        #    break

        quit, up, down, left, right, up_up, down_up, left_up, right_up, attack, dash, dash_up, next = controller.KeyEvents.check_events()

        speed = 3

        clock.tick(60)
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
        if dash:
            print(f'{hero1.rect.x}, {hero1.rect.y}')

        hero1.update()

        collide_monsters = pygame.sprite.groupcollide(
            player_list, monster_list, False, False, collided=pygame.sprite.collide_circle)

        if collide_monsters:
            for mon in collide_monsters.values():
                for m in mon:
                    m.attack_player(hero1)

        collide_items = pygame.sprite.groupcollide(
            player_list, item_list, False, True, collided=pygame.sprite.collide_circle)

        if collide_items:
            for ite in collide_items.values():
                for i in ite:
                    pick_sound.play()
                    i.effect(hero1)

        surface.blit(background, (0, 0))
        player_list.draw(surface)

        health_data = hero1.draw_health(surface)
        surface.blit(health_data, (hero1.health_bar_length - 25, 25))

        # play attack sound
        if attack:
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
            m.update(hero1.rect.x + 20, hero1.rect.y + 20)
            m.rect.x = m.x
            m.rect.y = m.y

        if len(monster_list) == 0:
            icon_index = (icon_index + 0.04) % len(arrow)
            surface.blit(arrow[int(icon_index)],
                         ((scene.door_xl + scene.door_xr)/2, scene.door_yl))
            if next:
                next_level = scene.next_level(
                    hero1)
                if next_level:
                    # play switch level sound
                    sls.play()
                    # set new drop items
                    (scene, monster_list) = rand_scene(hero1)
                    background = scene.background
                    item_list = rand_item(hero1.restrictx, hero1.restricty)

        item_list.draw(surface)
        monster_list.draw(surface)
        pygame.display.flip()


def rand_scene(hero):
    rand = random.randint(1, 6)
    if rand <= 3:
        scene = sceneview.Club()
    else:
        scene = sceneview.Street()
    hero.setPlayGround(scene.border_x, scene.border_y)
    hero.setPos(100, 500)
    monster_list = pygame.sprite.Group()
    for _ in range(random.randint(4, 7)):
        x = random.randint(1, 10)
        if x <= 5:
            monster = monsters.Slime()
        elif x <= 10:
            monster = monsters.Eyeball()
        monster.setPlayGround(scene.border_x, scene.border_x)
        monster_list.add(monster)
    return scene, monster_list


def rand_item(x, y):
    item_list = pygame.sprite.Group()
    num_of_drops = random.randint(1, 5)
    for _ in range(num_of_drops):
        index_of_drops = random.randint(1, 3)
        if index_of_drops == 1:
            item_list.add(items.Apple(
                random.randint(0, x), random.randint(y, 768)))
        elif index_of_drops == 2:
            item_list.add(items.BloodBottle(
                random.randint(0, x), random.randint(y, 768)))
        elif index_of_drops == 3:
            item_list.add(items.ChickenLeg(
                random.randint(0, x), random.randint(y, 768)))
    return item_list


if __name__ == "__main__":
    main()
