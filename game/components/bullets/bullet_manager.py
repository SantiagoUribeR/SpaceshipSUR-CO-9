import pygame

from game.components.bullets.bullets import Bullets
from game.utils.constants import ENEMY_TYPE, SHIELD_TYPE

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
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    game.death_count += 1
                    game.max_score = game.score if game.score > game.max_score else game.max_score

        for spaceship_bullet in self.spaceship_bullets:
            for enemy in game.enemy_manager.enemies:
                if spaceship_bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove( enemy)
                    game.score += 1
                    game.add_enemy()

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


