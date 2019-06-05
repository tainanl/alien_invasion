import pygame.font


class Button():
    def __init__(self, ai_settings, screen, msg):
        '''初始化按鈕的屬性'''
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #設置按鈕的尺寸和其它屬性
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #創建按鈕的rect對象，並使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #按鈕的標籤只需創建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        '''將msg渲染爲圖像，並使其在按鈕上居中'''
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #繪制一個用顏色填充的按鈕，再繪制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
