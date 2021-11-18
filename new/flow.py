import pygame
import time
import sys 
import copy

from pygame.math import enable_swizzling
from map import Map
from terrain import Grass, Store, Removable, Attack
from chess import Dogface,Devil
from cursor import Cursor

pygame.init()

class God:
    def __init__(self,screen):
        self.screen = screen
        self.player_chess = []
        self.neutral_chess = []
        self.enemy_chess = []
        self.current_action = ""
        self.current_chess = []


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
            self.current_chess = len(self.neutral_chess)
        elif self.current_action == "neutral":
            # 我方回合结束
            self.current_action = "enemy"
            self.current_chess = len(self.enemy_chess)
        else:
            # 敌人回合结束或者开局
            self.current_action = "player"
            self.current_chess = len(self.player_chess)
        
    
    def start(self):
        myfont = pygame.font.Font(None, 70)
        clock = pygame.time.Clock()             # 设置时钟
        m = Map()
        d1 = Dogface(1,3,'士兵一号')
        d2 = Dogface(5,6,'士兵二号')
        boss = Devil(16,12,'大魔王')
        print(d1.role,pygame.image.load('../images/man/士兵.png'))
        m.load_map(Store(4,7))
        m.load_map(Store(8,5))
        m.load_map(Store(14,11))
        m.load_map(d1)
        m.load_map(d2)
        m.load_map(boss)
        self.load([d1,d2],[],[boss])
        c = Cursor(0,0,m)
        while True:
            clock.tick(10)                      # 每秒执行10次
            for event in pygame.event.get():
                if event.type == pygame.QUIT:   # 如果检测到事件是关闭窗口
                    sys.exit()
                else:
                    screen.fill((255,255,255))
                    m.create(screen)
                    screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                if self.current_chess:
                    if self.current_action == "player":
                        # 光标可以自由移动
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                            c.move_up()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                            c.move_down()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                            c.move_left()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                            c.move_right()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        if (event.type == pygame.KEYDOWN and event.key == pygame.K_a) and not c.status:
                            # 首次选中
                            c.catch()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                            
                            # print("我方行动：",self.current_chess.pop())
                        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_a) and c.status:
                            # 再次选中
                            if isinstance(c.get_cursor_index_obj,Removable):
                                begin = c.current_obj.get_cur_index()
                                end = c.get_cur_index()
                                # 移动
                                m.change_map(begin,end,c.current_obj)
                                # 重置棋子位置
                                c.current_obj.set_cur_index(end[0],end[1])
                                # 可移动棋子数-1
                                self.current_chess -= 1
                                print("起始坐标{}，移动坐标{},开始移动".format(begin,end))
                            c.cancel()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                    elif self.current_action == "neutral" or self.current_action == "enemy":
                        if not c.status:
                            current_chess = self.__getattribute__("_".join([self.current_action,"chess"]))[self.current_chess-1]
                            print(self.current_action,"行动：",current_chess.name)
                            raw, col = current_chess.get_cur_index()
                            c.set_cur_index(raw,col)
                            c.catch() 
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                        else:
                            time.sleep(1)
                            self.current_chess -= 1
                            c.cancel()
                            screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
                else:
                    print("回合结束")
                    self.turn()
                pygame.display.update() 
                
                
                 
                

screen = pygame.display.set_mode((960,640))  # 显示窗口
screen.fill((0,255,255))
G = God(screen)
G.start()