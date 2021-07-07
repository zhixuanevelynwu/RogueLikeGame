#! /usr/bin/env python3
import random
from views import itemview

""" start items classes """


class Item(itemview.Drop):

    def __init__(self, item, x, y):
        '''
            item - the item that dropped after monster die or randomly
        '''
        itemview.Drop.__init__(self, item, x, y)
        self.item = item

    def __str__(self):
        s = f'Drop items: {self.item}'
        return s

    def effect(self, player):
        pass


class Apple(Item):
    """
        Increase max hp
    """

    def __init__(self, x, y):
        Item.__init__(self, 'apple', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        health_ratio = player.current_health / player.max_health
        player.max_health += 20
        player.current_health = int(player.max_health * health_ratio)


class BloodBottle(Item):
    """
        restore current hp
    """

    def __init__(self, x, y):
        Item.__init__(self, 'blood_bottle', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        player.get_health(player.max_health/5)


class ChickenLeg(Item):
    """
        Increase attack
    """

    def __init__(self, x, y):
        Item.__init__(self, 'chicken_leg', x, y)

    def __str__(self):
        pass

    def effect(self, player):
        player.attack += 2
