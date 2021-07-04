import random
import pygame
import math


class Enemy(pygame.sprite.Sprite):

    def __init__(self, race):
        pygame.sprite.Sprite.__init__(self)
        self.race = race
        self.sprites = []
        if self.race == "slime":
            self.sprites.append(pygame.image.load('image/slime_monster.png'))
            self.sprites.append(pygame.image.load('image/slime_monsterl.png'))
        elif self.race == "eyeball":
            self.sprites.append(pygame.image.load('image/eyeball_monster.png'))
            self.sprites.append(pygame.image.load(
                'image/eyeball_monsterl.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        """ Play ground """
        self.restrictx = 1024
        self.restricty = 0
        self.rand_point_x = random.randint(-20, 20)
        self.rand_point_y = random.randint(-10, 10)

    def setPlayGround(self, x, y):
        self.restrictx = x
        self.restricty = y

    def walk(self, x, y):
        x += 30
        y += 30
        distx = self.x - x
        disty = self.y - y
        diagonal_dist = math.sqrt(distx**2 + disty**2)
        if distx < 0:
            self.current = 0
        else:
            self.current = 1
        self.image = self.sprites[int(self.current)]
        if diagonal_dist < 300:
            self.approach(distx, disty)
        else:
            self.stroll(x, y)
        #self.approach(distx, disty)

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
            # SysFont expects a string with font names in it
            fonts = ','.join(a)
            return pygame.font.SysFont(fonts, font_size, bold, italic)
    return pygame.font.SysFont(None, font_size, bold, italic)
    # return pygame.freetype.Font("font/pokemongb.ttf", font_size)
