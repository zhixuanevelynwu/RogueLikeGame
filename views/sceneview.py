import random
import pygame


class Scene():

    def __init__(self, bg, border_x, border_y, door_xl, door_xr, door_yl, door_yh):
        self.border_x = border_x
        self.border_y = border_y
        self.background = pygame.image.load(bg).convert()
        self.door_xl = door_xl
        self.door_xr = door_xr
        self.door_yl = door_yl
        self.door_yh = door_yh

    def next_level(self, hero):
        if self.door_xl <= hero.rect.x <= self.door_xr and self.door_yl <= hero.rect.y <= self.door_yh:
            return True
        return False


class Club(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg0.png', 1024, 450, 550, 730, 450, 520)


class Street(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg1.png', 1024, 0, 840, 950, 600, 680)


class GameOver(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg4.png', 1024, 400, 550, 730, 450, 520)
        myfontobj = setup_fonts(25)
        over_text = '''     Game Over
        but you can always try again
        hit "return" key to start all over
        to quit the game, hit "Q"'''
        self.gameover_rect = pygame.Rect(260, 240, 500, 200)
        self.gameover_surface = word_wrap(
            self.gameover_rect, myfontobj, (255, 255, 255), over_text)


class Menu(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg1.png', 1024, 0, 550, 810, 470, 550)
        self.start_btn = pygame.image.load(
            'image/icons/menu/start_btn.png')
        self.help_btn = pygame.image.load(
            'image/icons/menu/help_btn.png')
        self.title = []
        self.title.append(pygame.image.load(
            'image/icons/menu/title/title_0.png'))
        self.title.append(pygame.image.load(
            'image/icons/menu/title/title_1.png'))
        '''help menu'''
        TEXT = '''Hello Warrior, 
        Welcome. Your quest is to hunt down all monsters escaped from the harddrive of our game company.
        
        Use "W" "A" "S" "D" to move arround. Press "K" to fight with monsters. Whenever you have cleared all monsters of a level, move to the indicated door area and hit "Return".
        
        To quit this page, hit "Return" button again.
        
        Have fun hunting...'''
        myfontobj = setup_fonts(21)
        self.wrapped_rect = pygame.Rect(170, 120, 700, 360)
        self.wrapped_surface = word_wrap(
            self.wrapped_rect, myfontobj, (255, 255, 255), TEXT)

    def help(self, hero):
        if 140 <= hero.rect.x <= 400 and 470 <= hero.rect.y <= 555:
            return True
        return False


def word_wrap(rect, font, color, text):
    ''' Wrap the text into the space of the rect, using the font object provided.
        Returns a surface of rect size with the text rendered in it.
    '''
    padding = 20
    max_width = rect.width - padding
    max_height = rect.height
    text_surface = pygame.Surface((max_width, max_height))
    # words in each line
    lines = [word.split(' ') for word in text.splitlines()]
    # size of a space that splits words
    space = font.size(' ')[0]
    x, y = (padding, 15)
    for line in lines:
        for word in line:
            font_surface = font.render(word, True, color)
            x_offset, y_offset = font_surface.get_size()
            if x + x_offset >= max_width:  # new line
                x = padding
                y += y_offset
                if y >= max_height:  # no more space
                    return text_surface
            text_surface.blit(font_surface, (x, y))
            x += x_offset + space
        # new line
        x = padding
        y += y_offset
    return text_surface


def setup_fonts(font_size, bold=False, italic=False):
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
