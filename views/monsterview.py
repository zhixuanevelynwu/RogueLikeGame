import random
import pygame
import math


class Enemy(pygame.sprite.Sprite):

    def __init__(self, race):
        pygame.sprite.Sprite.__init__(self)
        self.race = race
        self.sprites = []
        self.spritesl = []
        '''animation update speed'''
        self.updateSpeed = 0.09
        if self.race == "slime":
            self.updateSpeed = 0.07
            self.sprites.append(pygame.image.load(
                'image/monsters/slime/slime_r0.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/slime/slime_r1.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/slime/slime_r2.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/slime/slime_r3.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/slime/slime_l0.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/slime/slime_l1.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/slime/slime_l2.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/slime/slime_l3.png'))
        elif self.race == "eyeball":
            self.sprites.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_r0.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_r1.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_r2.png'))
            self.sprites.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_r3.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_l0.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_l1.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_l2.png'))
            self.spritesl.append(pygame.image.load(
                'image/monsters/eyeball/eyeball_l3.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        """ Play ground """
        self.restrictx = 1024
        self.restricty = 0
        self.rand_point_x = random.randint(-20, 20)
        self.rand_point_y = random.randint(-10, 10)
        self.seed_x = random.randint(-15, 15)
        self.seed_y = random.randint(-10, 10)

    def setPlayGround(self, x, y):
        self.restrictx = x
        self.restricty = y

    def walk(self, x, y):
        x += self.seed_x
        y += self.seed_y
        distx = self.x - x
        disty = self.y - y
        diagonal_dist = math.sqrt(distx**2 + disty**2)
        if distx >= 0:
            self.current = (
                self.current + self.updateSpeed) % len(self.spritesl)
            self.image = self.spritesl[int(self.current)]
        else:
            self.current = (
                self.current + self.updateSpeed) % len(self.sprites)
            self.image = self.sprites[int(self.current)]
        if diagonal_dist < 300:
            self.approach(distx, disty)
        else:
            self.stroll(x, y)

    def approach(self, distx, disty):
        back = 32
        if self.rect.x <= 0:  # Left
            self.rect.x += back
        if self.rect.x >= self.restrictx - 64:  # Right
            self.rect.x -= back
        if self.rect.y <= self.restricty:  # Up
            self.rect.y += back
        if self.rect.y >= 786 - 64:  # Bottom
            self.rect.y -= back
        if distx > 0:
            self.x -= self.vel
        elif distx <= 0:
            self.x += self.vel
        if disty > 0:
            self.y -= self.vel
        elif disty <= 0:
            self.y += self.vel

    def stroll(self, x, y):
        distx = self.x - self.rand_point_x - x
        disty = self.y - self.rand_point_y - y
        self.approach(distx, disty)
        # pass

    def vis_take_damage(self, vis, damage):
        red = 179, 35, 12
        font = setup_fonts(18)
        if vis:
            text_surface = font.render(f'-{damage}', True, red)
            return text_surface
        else:
            return font.render("", True, red)

    def update(self, x, y) -> None:
        self.walk(x, y)


def setup_fonts(font_size, bold=False, italic=False):
    ''' Load a font, given a list of preferences

        The preference list is a sorted list of strings (should probably be a parameter),
        provided in a form from the FontBook list.
        Any available font that starts with the same letters (lowercased, spaces removed)
        as a font in the font_preferences list will be loaded.
        If no font can be found from the preferences list, the pygame default will be returned.

        returns -- A Font object
    '''
    font_preferences = ['Bangers', 'Iosevka Regular',
                        'Comic Sans', 'Courier New']
    available = pygame.font.get_fonts()
    prefs = [x.lower().replace(' ', '') for x in font_preferences]
    for pref in prefs:
        a = [x
             for x in available
             if x.startswith(pref)
             ]
        if a:
            fonts = ','.join(a)
            return pygame.font.SysFont(fonts, font_size, bold, italic)
    return pygame.font.SysFont(None, font_size, bold, italic)
    # return pygame.freetype.Font("font/pokemongb.ttf", font_size)
