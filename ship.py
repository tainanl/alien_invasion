import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置初始位置'''
        #设置整个窗口为活动范围（自理解）
        super().__init__()
        self.screen = screen
        self.settings = ai_settings
        
        #加载图片，无image类，返回Surfade对象（官方文档指出）
        self.image = pygame.image.load('images/ship.bmp')
        
        #获取外接矩形(飞船及整个窗口)
        self.rect =self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #每艘飞船放置整个窗口底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #存储小数
        self.center = float(self.rect.centerx)

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        #更新center，加上速度指，许多属性只接受整数（官方文档）
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
