import pygame

class Snake():
    def __init__(self,ai_settings,screen):
        super(Snake, self).__init__()
        self.screen=screen
        self.ai_settings = ai_settings
        self.rect=pygame.Rect(screen.get_width()//2,screen.get_height()//2,20,20)
        self.color=(0,255,255)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.moving_up=False
        self.moving_right=False
        self.moving_down=False
        self.moving_left=False
        # self.rect.centerx=float(self.screen.centerx)
        # self.rect.centery=float(self.screen.centery)
        self.speed_factor = ai_settings.snake_speed_factor
    def update(self):
        if self.moving_up:
            self.y -= self.speed_factor
            self.rect.y = self.y
        elif self.moving_right:
            self.x+=self.speed_factor
            self.rect.x = self.x
        elif self.moving_left:
            self.x-=self.speed_factor
            self.rect.x = self.x
        elif self.moving_down:
            self.y += self.speed_factor
            self.rect.y = self.y
    def blitme(self):
       pygame.draw.rect(self.screen,self.color,self.rect)