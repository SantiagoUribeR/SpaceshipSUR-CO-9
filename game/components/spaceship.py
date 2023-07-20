import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import HEART_TYPE, MACHINE_GUN_TYPE, SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_TYPE, SHIELD_TYPE

class Spaceship(Sprite):
    X_POS =  SCREEN_WIDTH // 2 - 30
    Y_POS = 500
    def __init__(self):
        self.type = SPACESHIP_TYPE
        self.image = pygame.transform.scale( SPACESHIP, (60,50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.shooting_time = 1000
        self.last_time_shoot = 0
        self.power_up_types = {}
        self.remaining_lives = 10
        

    def update(self, user_input, bullet_manager):
        self.go_left = user_input[pygame.K_LEFT]
        self.go_right = user_input[pygame.K_RIGHT]
        self.go_down = user_input[pygame.K_DOWN]
        self.go_up = user_input[pygame.K_UP]
        self.fire = user_input[pygame.K_SPACE]
        self.move()
        if self.fire:
            self.shoot(bullet_manager)

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

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if not self.power_up_types.get(MACHINE_GUN_TYPE):
            if current_time  > self.shooting_time:
                if  len(bullet_manager.spaceship_bullets) < bullet_manager.enemy_by_level:
                    self.shooting_time = current_time + (500 - bullet_manager.enemy_by_level * 2)
                    self.last_time_shoot = current_time
                    bullet_manager.add_bullet(self)
        else:
            bullet_manager.add_bullet(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def on_pick_power_up(self, time_up, type, image):
        if not self.power_up_types.get(SHIELD_TYPE):
            self.image = pygame.transform.scale( image , (60,50))
        if type == HEART_TYPE:
            self.remaining_lives += 1
        else:
            self.power_up_types[type] = {"power_up_time_up": time_up}

    def draw_power_up(self, game):
        if self.power_up_types:
            messages = []
            for type in list(self.power_up_types):
                time_left = round((self.power_up_types[type]["power_up_time_up"] - pygame.time.get_ticks()) / 1000 ,2)
                if time_left >= 0:
                    messages.append(f"{type.capitalize()} is enable for  {time_left}  seconds")
                else:
                    self.power_up_types.pop(type)
                    self.image = pygame.transform.scale( SPACESHIP, (60, 50))
            game.menu.power_up_message(messages, game.screen)
