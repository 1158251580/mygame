import pygame
from block import Block

class Grass(Block):

    def set_role(self):
        self.role = pygame.image.load('images/green.png')
        self.step = 0

class Store(Block):

    def set_role(self):
        self.role = pygame.image.load('images/石头.png')
        self.step = 0

class Removable(Block):

    def set_role(self):
        self.role = pygame.image.load('images/blue.png')
        self.step = 0

class Attack(Block):
    
    def set_role(self):
        self.role = pygame.image.load('images/red.png')
        self.step = 0


grass = Grass('草')
store = Store('石头')
removable = Removable('可移动范围')
attack = Attack('攻击范围')