from pygame.sprite import Sprite
from dino_runner.utils.constants import (SCREEN_WIDTH, SCREEN_HEIGHT)

class Obstacle(Sprite):
    def __init__(self, sprite):
        self.dead = False
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.rect.x = SCREEN_WIDTH
    
    def update(self, game):
        self.rect.x -= game.game_speed
        return self.rect.x >= -self.sprite.get_width()
    
    def collision(self, game):
        if game.player.collision(self):
            if not game.player.protoshield:
                game.playing = False
            else:
                game.player.protoshield = False
                self.kill()

    def kill(self):
        self.dead = True

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)