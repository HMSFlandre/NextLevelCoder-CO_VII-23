from dino_runner.components.pickups.pickup import Pickup
from dino_runner.utils.constants import SHIELD

import random

class Shield(Pickup):
    def __init__(self):
        super().__init__(SHIELD)
        self.appear_chance = 2.5
        self.rect.y = random.randrange(180, 360) - self.sprite.get_height()
    
    def collision(self, game):
        if game.player.pickup_collision(self):
            game.player.protoshield = 5
            return True
        else:
            return False