import pygame
import time
import sys 
import copy

from pygame.math import enable_swizzling
from map import Map
from terrain import grass,store,removable,attack
from chess import Dogface,Devil
from cursor import Cursor
from algorithm import a_start,a_start_recursion,priority

pygame.init()

class God:
    def __init__(self,screen):
        self.screen = screen
        self.player_chess = []
        self.neutral_chess = []
        self.enemy_chess = []
        self.current_action = ""
        self.current_chess = []
        self.m = Map()
        self.c = Cursor(self.m)
        


    def load(self, player, neutral, enemy):
        self.player_chess = player
        self.neutral_chess = neutral
        self.enemy_chess = enemy
        self.current_action = ""
        self.current_chess = []

    def turn(self):
        if self.current_action == "player":
            # 我方回合结束
            self.current_action = "neutral"
            self.current_chess = self.neutral_chess[:]
        elif self.current_action == "neutral":
            # 友方回合结束
            self.current_action = "enemy"
            self.current_chess = self.enemy_chess[:]
        else:
            # 敌人回合结束或者开局
            self.current_action = "player"
            self.current_chess = self.player_chess[:]
        if self.current_chess:
            current_chess = self.current_chess[-1]
            raw, col = current_chess.get_cur_index()
            self.c.set_cur_index(raw,col)
            self.screen.blit(self.c.cursor[self.c.status],(self.c.cursor_col*self.m.block,self.c.cursor_raw*self.m.block))
    
    def start(self):
        myfont = pygame.font.Font(None, 70)
        clock = pygame.time.Clock()             # 设置时钟

        # 加载场景
        store.set_cur_index(14,11)
        self.m.load_map(store)
        store.set_cur_index(7,18)
        self.m.load_map(store)
        store.set_cur_index(13,5)
        self.m.load_map(store)

        # 加载人物
        d1 = Dogface('士兵一号','images/man/士兵.png')
        d1.set_cur_index(16,3)
        d2 = Dogface('士兵二号','images/man/士兵.png')
        d2.set_cur_index(15,16)
        boss = Devil('大魔王','images/man/boss.png')
        boss.set_cur_index(16,12)
        
        self.m.load_map(d1)
        self.m.load_map(d2)
        self.m.load_map(boss)

        # 加载阵营队列
        self.load([d1,d2],[],[boss])

        # 加载光标
        self.c.set_cur_index(0,0)
        clock.tick(10)                      # 每秒执行10次
        while True:
            # screen.fill((255,255,255))
            if self.current_chess:
                if self.current_action == "player":
                    # 棋子移动过程不再监听
                    if self.c.status and self.c.current_obj.path:
                        # 棋子移动
                        time.sleep(1)
                        begin = self.c.current_obj.get_cur_index()
                        end = self.c.current_obj.path.popleft()
                        self.m.change_map(begin,end,self.c.current_obj)
                        self.c.current_obj.set_cur_index(end[0],end[1])  
                        if not self.c.current_obj.path:
                            # 可移动棋子数-1
                            self.current_chess.pop(self.current_chess.index(self.c.current_obj))
                            # 移动结束，清除计数器
                            a_start_recursion.__del__()
                            # 取消选中
                            self.c.cancel() 
                    # 进入事件监听循环
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:   # 如果检测到事件是关闭窗口
                            sys.exit() 
                        # 光标可以自由移动
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                            self.c.move_up()
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                            self.c.move_down()
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            self.c.move_left()
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            self.c.move_right()
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
                            if not self.c.status:
                                # 首次选中
                                self.c.catch(self.current_chess)
                            elif self.c.status:
                                # 再次选中
                                if self.c.get_cursor_index_obj==boss or self.c.get_cursor_index_obj==removable:
                                    # 计算距离
                                    a_start_recursion(self.m,self.c.current_obj.get_cur_index(),self.c.get_cur_index(),self.c.current_obj.step)
                                    # 判断位置是否可达
                                    if a_start_recursion.count == 1 and self.c.current_obj.get_cur_index() != self.c.get_cur_index():
                                        # 位置不可达，清楚计数器，取消选中
                                        a_start_recursion.__del__()
                                        self.c.cancel()
                                    else:
                                        self.c.current_obj.path = a_start_recursion.path
                                else:
                                    self.c.cancel()
                            # screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                elif self.current_action == "neutral" or self.current_action == "enemy":
                    if not self.c.status:
                        # current_chess = self.__getattribute__("_".join([self.current_action,"chess"]))[self.current_chess-1]
                        current_chess = self.current_chess[-1]
                        print(self.current_action,"行动：",current_chess.name)
                        raw, col = current_chess.get_cur_index()
                        self.c.set_cur_index(raw,col)
                        self.c.catch(self.current_chess) 
                        # screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        target = priority(self.m,self.c.current_obj)
                        path = a_start(self.m,self.c.current_obj,target)
                        print(path)
                        self.c.current_obj.path = path
                    elif self.c.current_obj.path:
                        time.sleep(1)
                        begin = self.c.current_obj.get_cur_index()
                        end = self.c.current_obj.path.popleft()
                        self.m.change_map(begin,end,self.c.current_obj)
                        self.c.current_obj.set_cur_index(end[0],end[1])
                    else:
                        current_chess = self.current_chess.pop()
                        # self.current_chess -= 1
                        self.c.cancel()
                        # screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                self.m.create(screen)
                screen.blit(self.c.cursor[self.c.status],(self.c.cursor_col*self.m.block,self.c.cursor_raw*self.m.block))
                pygame.display.update() 
            else:
                print("回合结束")
                self.turn()
                
                
                
                 
                

screen = pygame.display.set_mode((960,640))  # 显示窗口
screen.fill((0,255,255))
G = God(screen)
G.start()