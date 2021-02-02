import sys
import pygame
class AlienInvasion:
    def __init__(self):
        pygame.init()
        
        self.screen=pygame.display.set_mode(1200,800)
        pygame.display.set.caption("Alien Invasion")
        
        def run_game(self):
            while True:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        sys.exit()
                        
                    pygame.display.flip()
                    
                    