import pygame.font


class Scoreboard():
    '''顯示得分信息類'''

    def __init__(self, ai_settings, screen, stats):
        '''初始化顯示得分涉及的屬性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #顯示得分信息時使用的字體設置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #準備初始得分圖像
        self.prep_score()

        #最高分
        self.prep_high_score()

        self.prep_level()

    def prep_score(self):
        '''將得分轉換爲一幅渲染的圖像'''
        rounded_score = int(round(self.stats.score, -1))
        score_str = '{:,}'.format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #將得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''在屏幕上顯示得分'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.levle_rect)

    def prep_high_score(self):
        '''將最高得分轉換爲渲染的圖像'''
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = '{:,}'.format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        
        #將最高得分放在屏幕頂端中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        '''將等級轉換爲渲染的圖像'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)

        #將等級放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
