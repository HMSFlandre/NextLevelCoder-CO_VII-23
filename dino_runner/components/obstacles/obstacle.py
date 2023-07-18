from pygame.sprite import Sprite
from dino_runner.utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)

class Obstacle(Sprite):
    def __init__(self, sprite):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game_speed):
        self.rect.x -= game_speed
        return self.rect.x >= -self.sprite.get_width()

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)