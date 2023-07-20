from dino_runner.components.pickups.shield import Shield
from dino_runner.components.pickups.graze import Graze
from dino_runner.components.pickups.point import Point

import random

class PickupHandler:
    def __init__(self):
        self.pickups = []
    
    def update(self, game):
        self.create_pickup()
        for pickup in self.pickups:
            if not pickup.update(game):
                self.pickups.remove(pickup)
            elif pickup.collision(game):
                self.pickups.remove(pickup)
    
    def create_pickup(self):
        for pickup in [Shield(), Graze(), Point()]:
            if pickup.appear():
                self.pickups.append(pickup)
    
    def draw(self, screen):
        for pickup in self.pickups:
            pickup.draw(screen)