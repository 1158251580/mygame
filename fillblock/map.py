from os import path
import pygame
from terrain import grass,removable
from algorithm import createPath

class Map:
    def __init__(self):
        self.map_width,self.map_height = 320, 320
        self.block = 32
        self.real_width,self.real_height = self.map_width//self.block, self.map_height//self.block
        self.empty_map = [[0 for i in range(self.real_width)] for j in range(self.real_height)]
        self.path_map = [[0 for i in range(self.real_width)] for j in range(self.real_height)]

    def create(self,screen):
        for i in range(self.real_height):
            for j in range(self.real_width):
                screen.blit(grass.role, (j*self.block, i*self.block))
                if self.path_map[i][j]:
                    screen.blit(self.path_map[i][j].role, (j*self.block, i*self.block))
                if self.empty_map[i][j]:
                    screen.blit(self.empty_map[i][j].role, (j*self.block, i*self.block))
                pygame.draw.line(screen, (0,0,0), (j*self.block,0), (j*self.block,self.map_height), 1)
            pygame.draw.line(screen, (0,0,0), (0,i*self.block), (self.map_width,i*self.block), 1)

    def load_map(self,status):
        raw, col = status.get_cur_index()
        self.empty_map[raw][col] = status
    
    def load_path(self):
        path = createPath((5,5))
        for i in path:
            self.path_map[i[0]][i[1]] = removable

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
