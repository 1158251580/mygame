import pygame

class Block:
    def __init__(self,name):
        self.cur_raw = 0
        self.cur_col = 0
        self.name = name
        self.step = 0
        self.set_role()

    def get_cur_index(self):
        return self.cur_raw, self.cur_col

    def set_cur_index(self,raw,col):
        self.cur_raw = raw
        self.cur_col = col

    def set_role(self):
        pass
    
    @property
    def get_role(self):
        pass
    
    def to_rbg(self,surface):
        # 备选方法，将图像转成RBG
        return pygame.image.tostring(surface, "RGB"),surface.get_size()

    def to_image(self,rbg,size):
        # 备选方法，将RBG转成图像
        return pygame.image.fromstring(rbg, size, "RGB")