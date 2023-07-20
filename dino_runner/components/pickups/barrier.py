from dino_runner.components.pickups.pickup import Pickup
from dino_runner.utils.constants import S_BARRIER

import random

class Barrier(Pickup):
    def __init__(self):
        super().__init__(S_BARRIER)
        self.appear_chance = 3.5
        self.rect.y = random.randrange(180, 360) - self.sprite.get_height()
    
    def collision(self, game):
        if game.player.pickup_collision(self):
            if game.player.barrier <= 0:
                game.player.barrier = 300
            else: 
                game.player.barrier += 150
            return True
        else:
            return False