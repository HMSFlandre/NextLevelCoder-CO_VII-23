from dino_runner.components.pickups.pickup import Pickup
from dino_runner.utils.constants import GRAZE

import random

class Graze(Pickup):
    def __init__(self):
        super().__init__(GRAZE)
        self.appear_chance = 5
        self.rect.y = random.randrange(180, 360) - self.sprite.get_height()
    
    def collision(self, game):
        if game.player.pickup_collision(self):
            game.player.graze = 300
            return True
        else:
            return False