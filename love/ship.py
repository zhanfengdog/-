import pygame
class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=ai_game.get_rect()
        
        self.image =pygame.img.load('ship.bmp')
        self.rect=self.img.get_rect()
        
        self.rect.midbottom=self.screen_rect.midbottom
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)