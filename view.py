import pygame
# import mechanics

START_SCREEN = 0

class SurvivalGame:
    
    def __init__(self):
        pygame.display.set_caption("Survival of the Fittest")
        self._running = True
        self._mode = START_SCREEN
        
    
    def run(self):
        pygame.init()
        
        while self._running:
            if self._mode == START_SCREEN:
                self._draw_start_screen()
            
            self._handle_events()
#             self._draw()
            pygame.display.flip()
            
        pygame.quit()
        
        
    def _draw_start_screen(self):
        pygame.display.set_mode((800, 800))
        surface = pygame.display.get_surface()
        pixel_width = surface.get_width()
        pixel_height = surface.get_height()
        
        start_button = pygame.draw.rect(surface, pygame.color.Color("#60cadb"), (200,500,400,100))
         
        
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
        
        
        
            
            
SurvivalGame().run()
            

    