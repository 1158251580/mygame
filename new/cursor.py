import pygame
from chess import Dogface, Devil
from algorithm import flood
from terrain import Attack, Removable

class Cursor:
    def __init__(self,raw,col,map_obj):
        self.map_obj = map_obj
        self.cursor_raw = raw
        self.cursor_col = col
        self.cursor = [
            pygame.image.load('../images/未选中光标.png'),
            pygame.image.load('../images/选中光标.png'),
            ]
        self.status = 0
        self.current_obj = None


    def move_up(self):
        if self.cursor_raw > 0:
            self.cursor_raw -= 1

    def move_down(self):
        if self.cursor_raw < self.map_obj.real_height:
            self.cursor_raw += 1

    def move_left(self):
        if self.cursor_col > 0:
            self.cursor_col -= 1
        

    def move_right(self):
        if self.cursor_col < self.map_obj.real_width:
            self.cursor_col += 1

    @property
    def get_cursor_index_obj(self):
        return self.map_obj.empty_map[self.cursor_raw][self.cursor_col]
    
    def get_cur_index(self):
        return self.cursor_raw,self.cursor_col

    def set_cur_index(self,raw,col):
        self.cursor_raw = raw
        self.cursor_col = col

    def catch(self):
        # 选中的是士兵
        if isinstance(self.get_cursor_index_obj,Dogface) or \
            isinstance(self.get_cursor_index_obj,Devil) :
            print("选中")
            # 光标切换
            self.status = 1
            # 保存捕获对象
            self.current_obj = self.get_cursor_index_obj
            # 显示可移动范围
            flood(self.map_obj,self.current_obj)
        else:
            print("不是士兵，无法选中")

    def cancel(self):
        self.status = 0
        self.current_obj = None
        for i in self.map_obj.empty_map:
            for index, j in enumerate(i):
                if isinstance(j,Removable) or isinstance(j,Attack):
                    i[index] = 0
        print("取消选中")