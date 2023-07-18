import pygame

from game.components.bullets.bullets import Bullets
from game.utils.constants import ENEMY_TYPE

class BulletManager:
    
    def __init__(self):
        self.enemy_bullets = []
        self.spaceship_bullets = []
        self.enemy_by_level = 2
        
    def update(self, game):
        self.enemy_by_level = game.enemy_by_level
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.update(self.enemy_bullets)
            if enemy_bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(enemy_bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for spaceship_bullet in self.spaceship_bullets:
            spaceship_bullet.update(self.spaceship_bullets)

    def draw(self, screen):
        for enemy_bullet in self.enemy_bullets:
            enemy_bullet.draw(screen)
        
        for enemy_bullet in self.spaceship_bullets:
            enemy_bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE :
            if len(self.enemy_bullets) < self.enemy_by_level:
                self.enemy_bullets.append(Bullets(spaceship))
        else:
            self.spaceship_bullets.append(Bullets(spaceship))


