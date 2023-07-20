import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
MACHINE_GUN_TYPE = 'machine_gun'
ENEMY_TYPE = 'enemy'
SPACESHIP_TYPE = 'spaceship'
HEART_TYPE = 'heart'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_MACHINE_GUN = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_machine_gun.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
MACHINE_GUN = pygame.image.load(os.path.join(IMG_DIR, "Bullet/machine_gun.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_IMAGES = [pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")), pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))]

GAME_OVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

FONT_STYLE = 'game/assets/Other/space_invaders.ttf'
