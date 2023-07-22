import random
import pygame

from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT,  SPACESHIP
from pygame.sprite import Sprite

class PowerUp(Sprite):

    def __init__(self, image, type, spaceship_image = SPACESHIP):
        self.type = type
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = random.randint(100, SCREEN_WIDTH - 100)
        self.rect.y = 0
        self.spaceship_image = spaceship_image

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        # if self.type == HEART_TYPE:
        #     self.rect.y += 20
        if self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)
        pass
    
    def draw(self, game):
        game.screen.blit(self.image, self.rect)