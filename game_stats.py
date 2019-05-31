class GameStats():
    '''跟踪游戏统计信息'''
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def rest_stats(self):
        self.ships_left = self.ai_settings.ship_limit
