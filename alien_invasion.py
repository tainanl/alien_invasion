import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    #游戏初始化
    pygame.init()
    
    #设置窗口大小及标题
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    
    #创建飞船
    ship = Ship(screen)

    #游戏主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()

