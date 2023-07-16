import pygame
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import (CLOUD, MOYAI)

class Bg_elements:
    cloud_x = [0, 30, 70, 45, 105]
    cloud_y = [46, 5, 18, 78, 115]
    cloud_speed = [1.5, 1, 0.5, 1.7, 0.8]

    moyai_x = [random.randrange(0, 2250), random.randrange(0, 2250), random.randrange(0, 2250)]

    def update(self, game_speed):
        for cloud_id in range(len(self.cloud_speed)):
            self.cloud_x[cloud_id] -= game_speed * self.cloud_speed[cloud_id]
        for moyai_id in range(len(self.moyai_x)):
            self.moyai_x[moyai_id] -= game_speed
    
    def draw(self, screen):
        self.draw_cloud(screen)
        self.draw_moyai(screen)
    
    def draw_cloud(self, screen):
        for cloud_id in range(len(self.cloud_x)):
            if self.cloud_x[cloud_id] + screen.get_width() <= -CLOUD.get_width():
                self.cloud_x[cloud_id] = random.randrange(0, 150)
                self.cloud_y[cloud_id] = random.randrange(0, 130)
                self.cloud_speed[cloud_id] = random.randrange(3, 17)/10
            screen.blit(CLOUD, (screen.get_width() + self.cloud_x[cloud_id], self.cloud_y[cloud_id]))

    def draw_moyai(self, screen):
        for moyai_id in range(len(self.moyai_x)):
            if self.moyai_x[moyai_id] + screen.get_width() <= -MOYAI.get_width():
                self.moyai_x[moyai_id] = random.randrange(200, 2250)
            screen.blit(MOYAI, (screen.get_width() + self.moyai_x[moyai_id], 308))