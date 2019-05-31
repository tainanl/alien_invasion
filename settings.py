class Settings():
    def __init__(self):
        '''设置整个窗口大小及背景颜色'''
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #1设置为右移，-1为左移
        self.fleet_direction = 1
