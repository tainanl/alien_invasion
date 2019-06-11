class Settings():
    def __init__(self):
        '''初始化遊戲的靜態設置'''
        #屏幕設這
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230,230)
        
        #剩餘飛船設置.算上初始化的飛船共３個
        self.ship_limit = 2 

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #外星人设置
        self.fleet_drop_speed = 10
        
        #以什麼樣的速度加快遊戲節奏
        self.speedup_scale = 1.1
        #外星人點數的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化隨遊戲進行而變化的設置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction爲１表示向右；爲－１表示向左
        self.fleet_direction = 1

        #記分
        self.alien_points = 50

    def increase_speed(self):
        '''提高速度設置'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
