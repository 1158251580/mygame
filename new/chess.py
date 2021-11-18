import pygame
from block import Block

class Dogface(Block):
    def __init__(self,raw,col,name):
        self.role = pygame.image.load('../images/man/士兵.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 4
    
    

class Devil(Block):
    def __init__(self,raw,col,name) -> None:
        self.role = pygame.image.load('../images/man/boss.png')
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 5