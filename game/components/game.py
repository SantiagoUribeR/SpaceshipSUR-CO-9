import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu

from game.components.spaceship import Spaceship
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.enemy_by_level = 2
        self.player = Spaceship()
        self.enemy = EnemyManager(self.add_enemy)
        self.bullet_manager = BulletManager()
        self.menu = Menu("Press any key to start")
        self.score = 0
        self.deth_count = 0

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
    def play(self):
        self.playing = True
        self.score = 0
        self.enemy.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy.update(self.enemy_by_level, self.bullet_manager)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def add_enemy(self, deleted_enemies):
        if(deleted_enemies % 10 == 0):
            self.enemy_by_level += 1
    
    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)

    
    def on_close(self):
        self.playing = False
        self.running = False
    
    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Your score is {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center= (1000, 50)
        self.screen.blit(text, text_rect)