import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Class to manage the game."""
    
    def __init__(self):
        """Creating game modules."""
        pygame.init()
        
        self.clock=pygame.time.Clock()
        self.settings=Settings()
        
        self.screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship=Ship(self)
        self.bullets = pygame.sprite.Group()
        
        self.bg_color=(230,230,230)
        
    def run_game(self):
        "Loop for the game."
        while True:
            """Track the keyboard."""
            self._check_events()
            self.ship.update()
            self.bullets.update()
            
            #Get rid of bullets
            for bullet in self.bullets.copy():
                if bullet.rect.bottom<=0:
                    self.bullets.remove(bullet)
            
            print(len(self.bullets))
            
            
            self._update_screen()
            #Make recent screen visible        
            self.clock.tick(60)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
                    
    
    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            #Moving the ship to the right
            self.ship.moving_right=True            
        elif event.key==pygame.K_LEFT:
            #Moving the ship to the right
            self.ship.moving_left=True
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
    
    
    def _check_keyup_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False                 
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False
            
    def _fire_bullet(self):
        """New bullet create and added"""
        
        new_bullet=Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
         #Redraw the screen
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.ship.blitme()
            pygame.display.flip()

if __name__=='__main__':
    #Make a game isntance
    ai=AlienInvasion()
    ai.run_game()