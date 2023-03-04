import pygame

class Ship:
    """Manages the ship"""
    
    def __init__(self,ai_game):
        """"Initialise and set the coordinates"""
        
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()
        
        #load the ship image
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        
        #New ship at the bottom of the screen
        self.rect.midbottom=self.screen_rect.midbottom
        
        #Store a float for the ship
        self.x=float(self.rect.x)
        
        #Movement flag;start with unmoving ship
        self.moving_right=False
        self.moving_left=False
        
    def blitme(self):
        """Draw the ship at the current location"""
        self.screen.blit(self.image,self.rect)
        
    def update(self):
        """Update the ship's postion based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x=self.x+self.settings.ship_speed
            
        if self.moving_left and self.rect.left > 0:
            self.x=self.x-self.settings.ship_speed
        
        self.rect.x=self.x