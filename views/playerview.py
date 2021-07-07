import pygame
import os
os.environ['PYGAME_FREETYPE'] = '1'


class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        """ Draw player """
        self.sprites = []
        self.sprites.append(pygame.image.load('image/hero_f1.png'))
        self.sprites.append(pygame.image.load('image/hero_f2.png'))
        self.sprites.append(pygame.image.load('image/hero_f3.png'))
        self.spritesl = []
        self.spritesl.append(pygame.image.load('image/hero_f1l.png'))
        self.spritesl.append(pygame.image.load('image/hero_f2l.png'))
        self.spritesl.append(pygame.image.load('image/hero_f3l.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.movex = 0
        self.movey = 0
        self.rect.x = 100
        self.rect.y = 500
        """ Health bar"""
        self.current_health = 100
        self.max_health = 100
        self.health_bar_length = 400
        self.health_ratio = self.health_bar_length / self.max_health
        """ Play ground """
        self.restrictx = 1024
        self.restricty = 0

    def setPlayGround(self, x, y):
        self.restrictx = x
        self.restricty = y

    def setPos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.movex += x
        self.movey += y

    def stop(self):
        self.movex = 0
        self.movey = 0

    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        self.current += 0.1
        if self.movex > 0 or self.movey != 0:
            if self.current >= len(self.sprites):
                self.current = 0
            self.image = self.sprites[int(self.current)]
        if self.movex < 0:
            if self.current >= len(self.spritesl):
                self.current = 0
            self.image = self.spritesl[int(self.current)]
        # go back if touch the boundry
        back = 32
        if self.rect.x <= 0:  # Left
            self.rect.x += back
        if self.rect.x >= self.restrictx - 64:  # Right
            self.rect.x -= back
        if self.rect.y <= self.restricty:  # Up
            self.rect.y += back
        if self.rect.y >= 786 - 64:  # Bottom
            self.rect.y -= back

    def draw_health(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (50, 50, int(
            self.current_health / self.max_health * self.health_bar_length), 25))
        pygame.draw.rect(surface, (255, 255, 255),
                         (50, 50, self.health_bar_length, 25), 4)
        font = setup_fonts(18)
        return font.render(f"Health: {int(self.current_health)}/{self.max_health}", True, (255, 255, 255))

    def vis_attack(self, vis):
        black = (0, 0, 0)
        white = (255, 255, 255)
        font = setup_fonts(18)
        if vis:
            text_surface = font.render("ATK", True, white, black)
            return text_surface
        else:
            return font.render("", True, white, black)

    def vis_take_damage(self, vis, damage):
        red = 179, 35, 12
        font = setup_fonts(18)
        if vis:
            text_surface = font.render(f'-{damage}', True, red)
            return text_surface
        else:
            return font.render("", True, red)


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
