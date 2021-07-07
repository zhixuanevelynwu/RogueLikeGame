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
            print("next level")
            return True
        return False


class Club(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg0.png', 1024, 450, 550, 730, 450, 520)


class Street(Scene):
    def __init__(self):
        Scene.__init__(self, 'image/bg/bg1.png', 1024, 0, 840, 950, 600, 680)
