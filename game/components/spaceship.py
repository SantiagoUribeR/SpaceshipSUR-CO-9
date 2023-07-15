import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class Spaceship(Sprite):
    X_POS =  SCREEN_WIDTH // 2 - 30
    Y_POS = 500

    def __init__(self):
        self.image = pygame.transform.scale( SPACESHIP, (60,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def update(self, user_input):
        self.go_left = user_input[pygame.K_LEFT]
        self.go_right = user_input[pygame.K_RIGHT]
        self.go_down = user_input[pygame.K_DOWN]
        self.go_up = user_input[pygame.K_UP]
        self.move()

    def move(self):
        if(self.go_left):
            self.rect.x = (SCREEN_WIDTH, self.rect.x - 10)[self.rect.left > 0]

        if(self.go_right):
            self.rect.x = (-50, self.rect.x + 10)[self.rect.left < SCREEN_WIDTH]

        if(self.go_down):
            if(self.rect.bottom < SCREEN_HEIGHT):
                self.rect.y += 10

        if(self.go_up):
            if(self.rect.top > 0):
                self.rect.y -= 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))