import pygame
from flow import God


class SceneManager():
    def __init__(self,scene):
        pygame.init()
        pygame.font.Font(None, 70)
        pygame.display.set_caption("我的战棋")

        self.screen = pygame.display.set_mode((960,640))  # 显示窗口
        self.screen.fill((0,255,255))
        self.clock = pygame.time.Clock()
        self.current_scene = scene(self.screen)

    def start(self):
        
        self.clock.tick(10)                      # 每秒执行10次
        self.current_scene.start()
    
    def ChangeScene(self,Scene):
        if hasattr(self.CurrentScene,'Close'):self.CurrentScene.Close()
        self.CurrentScene = Scene()


SceneManager(God).start()

