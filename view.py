import pygame
# import mechanics

START_SCREEN = 0
BUILD_SCREEN = 1
GAME_SCREEN = 2
END_SCREEN = 3

white = (255,255,255)

class SurvivalGame:

    def __init__(self):
        pygame.display.set_caption("Survival of the Fittest")
        self._running = True
        self._mode = START_SCREEN


    def run(self):
        pygame.init()
        pygame.display.set_mode((800, 800))

        while self._running:
            if self._mode == START_SCREEN:
                self._draw_start_screen()
                
            elif self._mode == BUILD_SCREEN:
                surface = pygame.display.get_surface()
                surface.fill((0,0,0))
                
            else:
                surface = pygame.display.get_surface()
                surface.fill(white)
                
            

            #second screen
#             self._select_choices()

            self._handle_events()
#             self._draw()
            pygame.display.flip()

        pygame.quit()


    def _draw_start_screen(self):
        surface = pygame.display.get_surface()
        pixel_width = surface.get_width()
        pixel_height = surface.get_height()

        font = pygame.font.Font(None, 100)
        start_text = font.render("Start", True, white)
        # Draws the start button
        pygame.draw.rect(surface, pygame.color.Color("#60cadb"), (200,500,400,100))

        surface.blit(start_text, (320,520))

        font = pygame.font.Font(None, 180)
        title1 = font.render("Survival", True, white)
        title2 = font.render("of the", True, white)
        title3 = font.render("Fittest", True, white)

        surface.blit(title1, (150,100))
        surface.blit(title2, (230,220))
        surface.blit(title3, (200,340))


    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_click()


    def _handle_click(self):
        if self._mode == START_SCREEN:
            cursor_x, cursor_y = pygame.mouse.get_pos()
            if cursor_x >= 200 and cursor_x <= 600 \
            and cursor_y >= 500 and cursor_y <= 600:
                self._mode = BUILD_SCREEN
        



    def _select_choices(self):

        pygame.display.set_mode((800, 800))
        surface = pygame.display.get_surface()
        skinList = pygame.draw.rect(surface, pygame.color.Color("#ffdd7f"), (45,45,200,500))

        font = pygame.font.Font(None, 200)
        n = font.render("text", False , (255,255,255))





SurvivalGame().run()
