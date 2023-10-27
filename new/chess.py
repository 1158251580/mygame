import os
import pygame
import random
import json
from block import Block
from collections import deque

class Chess(Block):
    def set_role(self):

        # 加载棋子属性
        with open(os.path.dirname(__file__)+'\chess.json','r',encoding='utf8') as fp:
            config = json.load(fp).get(self.name,{})
        for key, value in config.items():
            self.__setattr__(key, value)

        

        self.path = deque([]) # 移动路径

    def attack_enemy(self, enemy):

        # 计算棋子属性
        self.hit_rate = self.speed+1.5*self.skill+0.5*self.lucky # 命中率
        self.dodge_rate = 1.5*self.speed+self.skill+0.5*self.lucky # 闪避率
        self.critical_rate = 0.5*self.speed+1*self.skill+1.5*self.lucky # 暴击率
        self.vulnerability_protection = 0.5*self.speed+1.5*self.skill+self.lucky # 弱点保护率

        # 判断是否命中
        
        if random.random() > round(self.hit_rate/(self.hit_rate+enemy.dodge_rate),2):
            self.level_up()
        else:
            # 进行攻击计算
            damage = self.magic - enemy.resistance
            damage = self.attack - enemy.defense
            
            # 暴击计算
            if random.random() <= round(self.critical_rate-enemy.vulnerability_protection,2):
                damage *= 3
            enemy.hp -= damage
            if enemy.hp > 0:
                # 敌人没死
                self.level_up()
            else:
                # 敌人死亡
                self.level_up(3)

    def level_up(self,num=1):
        pass
        
    

class Dogface(Chess):

    def level_up(self,num=1):
        # 经验值增加，触发升级条件
        self.exp += num
        if self.exp // 10:
            self.exp %= 10 
            self.hp += random.randint(0,10)
            self.attack += random.randint(0,5)
            self.defense += random.randint(0,5)
    
    

class Devil(Chess):
    
    def level_up(self,num=1):
        # 经验值增加，触发升级条件
        self.exp += num
        if self.exp // 10:
            self.exp %= 10 
            self.hp += random.randint(0,10)
            self.attack += random.randint(0,5)
            self.defense += random.randint(0,5)
        
