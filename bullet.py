import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage the bullets"""
    
    def __init__(self,ai_game):
        
        """careate bullet object at ship location"""
        super().__init__()
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color
        
        """bullet rect creation"""
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,
                              self.settings.bullet_height)
        self.rect.midtop=ai_game.ship.rect.midtop
        
        #store bullet position
        self.y=float(self.rect.y)
        
        
    def update(self):
        """move the bullet up the screen"""
        
        #update exact position
        self.y=self.y-self.settings.bullet_speed
        #Update rect
        self.rect.y=self.y
        
        
    def draw_bullet(self):
        """Draw the bullet to the screen"""
        
        pygame.draw.rect(self.screen,self.color,self.rect)
        