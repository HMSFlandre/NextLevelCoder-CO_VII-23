from dino_runner.utils.constants import SCREEN_WIDTH

from pygame.sprite import Sprite
import random

class Pickup(Sprite):
    def __init__(self, sprite):
        self.appear_chance = 0.006
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 300

    def update(self, game):
        self.rect.x -= game.game_speed
        return self.rect.x >= -self.sprite.get_width()
    
    def collision(self, game):
        return game.player.pickup_collision(self)
    
    def appear(self):
        return random.randrange(0, 100000) <= (self.appear_chance * 100)

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)