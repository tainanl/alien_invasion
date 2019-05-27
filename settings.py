class Settings():
    def __init__(self):
        '''设置整个窗口大小及背景颜色'''
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230,230)
        self.ship_speed_factor = 5 

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
