import pygame

from game.utils.constants import FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu: 
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message ):
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.icon = pygame.transform.scale(ICON, ( 120,80 ))
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT - 100)  
        self.update_message(message)

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw(self, screen):
        screen.fill((255, 255, 255))
        screen.blit(self.text, self.text_rect)
        screen.blit(self.icon, self.icon_rect)
        pygame.display.update()
    
    def update_message(self, message):
        self.message = message
        self.text = self.font.render(self.message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
    
    def power_up_message(self, messages, screen):
        font = pygame.font.Font(FONT_STYLE, 15)
        for index, message in enumerate(messages):
            power_up_message = font.render(message, True, (255, 255, 255))
            power_up_message_rect = power_up_message.get_rect()
            power_up_message_rect.center = (self.HALF_SCREEN_WIDTH, SCREEN_HEIGHT - power_up_message_rect.height -20 * index)
            screen.blit(power_up_message, power_up_message_rect)
