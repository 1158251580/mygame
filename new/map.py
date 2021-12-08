import pygame
from terrain import grass,removable


class Map:
    def __init__(self):
        self.map_width,self.map_height = 960, 640
        self.block = 32
        self.real_width,self.real_height = self.map_width//self.block, self.map_height//self.block
        self.empty_map = [[0 for i in range(self.real_width)] for j in range(self.real_height)]
        
    @property
    def map_size(self):
        return (self.map_width,self.map_height)

    def load_map(self,status):
        raw, col = status.get_cur_index()
        self.empty_map[raw][col] = status

    def change_map(self,begin,end, status):
        self.empty_map[begin[0]][begin[1]] = removable
        self.empty_map[end[0]][end[1]] = status

    def create(self,screen):
        for i in range(self.real_height):
            for j in range(self.real_width):
                screen.blit(grass.role, (j*self.block, i*self.block))
                if self.empty_map[i][j]:
                    screen.blit(self.empty_map[i][j].role, (j*self.block, i*self.block))
                pygame.draw.line(screen, (0,0,0), (j*self.block,0), (j*self.block,self.map_height), 1)
            pygame.draw.line(screen, (0,0,0), (0,i*self.block), (self.map_width,i*self.block), 1)