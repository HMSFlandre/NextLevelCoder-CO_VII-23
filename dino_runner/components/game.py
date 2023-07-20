import pygame
from dino_runner.components.obstacles.obstacle_handler import ObstacleHandler
from dino_runner.components.pickups.pickup_handler import PickupHandler

from dino_runner.utils.constants import (
    BG, 
    ICON, 
    SCREEN_HEIGHT, 
    SCREEN_WIDTH, 
    TITLE, 
    FPS,
    CLOUD,
    MOYAI
    )
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.bg_elements import Bg_elements


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.font = pygame.font.SysFont('Comic Sans MS', 20)
        self.score = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.bg_extras = Bg_elements()
        self.obstacle_handler = ObstacleHandler()
        self.pickup_handler = PickupHandler()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.score += 1
        if self.score < 0:
            self.score = 0
        self.bg_extras.update(self)
        self.player.update(pygame.key.get_pressed())
        self.obstacle_handler.update(self)
        self.pickup_handler.update(self)

    def draw(self):
        score_text = self.font.render("Score: " + str(self.score), False, (127, 127, 127))
        self.clock.tick(FPS)
        self.screen.fill(self.bg_extras.chose_color())
        self.bg_extras.draw_back(self.screen)
        self.draw_background()
        self.bg_extras.draw(self.screen)
        self.player.draw(self.screen)
        self.obstacle_handler.draw(self.screen)
        self.pickup_handler.draw(self.screen)
        self.player.draw_ui(self.screen)
        self.screen.blit(score_text, (10, 20))
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
