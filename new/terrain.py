import pygame
from block import Block

class Grass(Block):

    def set_role(self):
        self.step = 0

class Store(Block):

    def set_role(self):
        self.step = 0

class Removable(Block):

    def set_role(self):
        self.step = 0

class Attack(Block):
    
    def set_role(self):
        self.step = 0


grass = Grass('草','images/green.png')
store = Store('石头','images/store.png')
removable = Removable('可移动范围','images/blue.png')
attack = Attack('攻击范围','images/red.png')