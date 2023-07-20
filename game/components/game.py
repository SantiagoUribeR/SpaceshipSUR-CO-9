import pygame
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.power_ups.power_up_magager import PowerUpManager

from game.components.spaceship import Spaceship
from game.utils.constants import BG, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, FONT_STYLE


class Game:
    def __init__(self):
        self.HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
        self.HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
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
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.power_up_manager = PowerUpManager()
        self.menu = Menu("Press any key to start")
        self.score = 0
        self.max_score = 0
        self.death_count = 0

    def run(self):
        self.running = True
        while self.running:
            self.screen.fill((0, 0, 0))
            if self.player.remaining_lives <= 0:
                image = pygame.transform.scale(GAME_OVER, (400, 40))
                image_rect = image.get_rect()
                image_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
                self.screen.blit(image, image_rect)
                pygame.display.flip()
                pygame.time.delay(2000)
                self.running = False

            elif not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()
    
    def play(self):
        self.playing = True
        self.reset()
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
        self.enemy_manager.update(self.enemy_by_level, self.bullet_manager)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_power_up(self)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self)
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

    def add_enemy(self):
        if(self.score % 5 == 0):
            self.enemy_by_level += 1
    
    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
    
    def draw_score(self):
        messages = [
            f"Your score is:  {self.score}",
            f"You have {self.player.remaining_lives} lives left",
            f"The count of deaths is:  {self.death_count}",
            f"Your max score is:  {self.max_score}",
        ]

        font = pygame.font.Font(FONT_STYLE, 15)
        for index, message in enumerate(messages):
            if index == 0 or self.death_count > 0:
                text = font.render(message, True, (255, 255, 255))
                text_rect = text.get_rect()
                text_rect.x = SCREEN_WIDTH - text_rect.width - 20
                text_rect.y =  30 + (index * 20)
                self.screen.blit(text, text_rect)

    def reset(self):
        self.score = 0
        self.player.rect.x = self.player.X_POS
        self.player.power_up_types = {}
        self.player.rect.y = self.player.Y_POS
        self.enemy_manager.reset()
        self.power_up_manager.reset()
        self.bullet_manager.reset()
        self.enemy_by_level = 2