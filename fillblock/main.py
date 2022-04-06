import pygame,sys
from map import Map
from chess import Dogface
from cursor import Cursor


def main():
    pygame.init()
    clock = pygame.time.Clock()             # 设置时钟
    clock.tick(10)
    screen = pygame.display.set_mode((320,320))  # 显示窗口
    screen.fill((0,255,255))
    m = Map()
    m.load_path()
    c = Cursor(m)
    c.set_cur_index(5,5)
    while True:
        m.create(screen)
        screen.blit(c.cursor[c.status],(c.cursor_col*m.block,c.cursor_raw*m.block))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # 如果检测到事件是关闭窗口
                sys.exit()   
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
                c.move_up()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
                c.move_down()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                c.move_left()
            elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):  
                c.move_right()
        pygame.display.update() 


if __name__ == '__main__':
    main()
