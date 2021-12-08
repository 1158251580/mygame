import pygame
from block import Block
from collections import deque

class Dogface(Block):

    def set_role(self):
        self.role = pygame.image.load('../images/man/士兵.png')
        self.step = 4
    
    

class Devil(Block):
        
    def set_role(self):
        self.role = pygame.image.load('../images/man/boss.png')
        self.step = 4
        self.path = deque([])
