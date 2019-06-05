class GameStats():
    '''跟踪游戏统计信息'''
    def __init__(self, ai_settings):
        '''初始化統計信息'''
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #讓遊戲一開始處於非活動狀態
        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
