import pygame
import random
from block import Block
from collections import deque

class Chess(Block):
    def set_role(self, exp, hp, attack, defense):
        self.exp = exp
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    def attack_enemy(self, enemy):
        # 进行攻击计算
        damage = self.attack - enemy.defense
        enemy.hp -= damage
        if enemy.hp:
            self.level_up()
        else:
            self.level_up(3)
    
    def level_up(self,num=1):
        # 经验值增加，触发升级条件
        self.exp += num
        if self.exp % 10 == 0:
            self.hp += random.randint(0,10)
            self.attack += random.randint(0,5)
            self.defense += random.randint(0,5)


class Dogface(Block):

    def set_role(self):
        self.role = pygame.image.load('images/man/士兵.png')
        self.step = 4

    
    

class Devil(Block):
        
    def set_role(self):
        self.role = pygame.image.load('images/man/boss.png')
        self.step = 4
        self.path = deque([])
