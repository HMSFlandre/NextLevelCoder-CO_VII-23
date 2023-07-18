from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD

import random

class Pterodactyl(Obstacle):
    def __init__(self):
        self.step = 0
        super().__init__(BIRD[0])
        self.rect.y = random.choice([380, 320]) - self.sprite.get_height()
    
    def update(self, game):
        self.rect.x -= game.game_speed * random.choice([0.9, 1, 1.1])
        self.step += 1
        self.sprite = BIRD[0] if self.step < 15 else BIRD[1]
        if self.step >= 30:
            self.step = 0
        return self.rect.x >= -self.sprite.get_width()