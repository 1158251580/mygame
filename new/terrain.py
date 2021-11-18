import pygame
from block import Block

class Grass(Block):
    def __init__(self, raw, col, name='草'):
        self.role = pygame.image.load('../images/green.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 0

class Store(Block):
    def __init__(self, raw, col, name='石头'):
        self.role = pygame.image.load('../images/石头.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 0

class Removable(Block):
    def __init__(self, raw, col, name='移动范围'):
        self.role = pygame.image.load('../images/blue.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 0

class Attack(Block):
    def __init__(self, raw, col, name='攻击范围'):
        self.role = pygame.image.load('../images/red.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 0