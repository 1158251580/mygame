import pygame

class Block:
    def __init__(self, raw, col, name):
        self.role = None
        self.cur_raw = raw
        self.cur_col = col
        self.name = name
        self.step = 0

    def get_cur_index(self):
        return self.cur_raw, self.cur_col

    def set_cur_index(self,raw,col):
        self.cur_raw = raw
        self.cur_col = col

    def to_rbg(self,surface):
        # 备选方法，将图像转成RBG
        return pygame.image.tostring(surface, "RGB"),surface.get_size()

    def to_image(self,rbg,size):
        # 备选方法，将RBG转成图像
        return pygame.image.fromstring(rbg, size, "RGB")