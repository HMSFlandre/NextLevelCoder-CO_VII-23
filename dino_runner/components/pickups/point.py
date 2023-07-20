from dino_runner.components.pickups.pickup import Pickup
from dino_runner.utils.constants import POINT

import random

class Point(Pickup):
    def __init__(self):
        super().__init__(POINT)
        self.appear_chance = 15
        self.rect.y = random.randrange(180, 360) - self.sprite.get_height()
    
    def collision(self, game):
        if game.player.pickup_collision(self):
            game.score += (100 * game.player.continuous_point_collection)
            game.player.continuous_point_collection += 1
            return True
        else:
            return False