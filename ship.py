import pygame

class Ship():
    def __init__(self, screen):
        '''初始化飞船并设置初始位置'''
        #设置整个窗口为活动范围（自理解）
        self.screen = screen
        
        #加载图片，无image类，返回Surfade对象（官方文档指出）
        self.image = pygame.image.load('images/ship.bmp')
        
        #获取外接矩形(飞船及整个窗口)
        self.rect =self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #每艘飞船放置整个窗口底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        '''根据移动标志调整飞船位置'''
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
