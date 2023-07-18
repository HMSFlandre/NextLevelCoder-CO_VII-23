from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import (SMALL_CACTUS, LARGE_CACTUS)

import random

class Cactus(Obstacle):
    def __init__(self):
        image_list = SMALL_CACTUS + LARGE_CACTUS
        option = random.choice(image_list)
        super().__init__(option)
        self.rect.y = 400 - option.get_height()