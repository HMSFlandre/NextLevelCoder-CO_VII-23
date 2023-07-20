import pygame
import random

from pygame.sprite import Sprite
from dino_runner.utils.constants import (CLOUD, MOYAI, SUNS, MOONS, SCREEN_HEIGHT, SCREEN_WIDTH)

class Bg_elements:
    # 2 frames = 1 minute
    daytime = 1080 # 0 = 12:00 AM
    hour = 0
    minutes = 0
    current_sun = random.choice(SUNS)
    sun_rect = current_sun.get_rect()
    current_moon = random.choice(MOONS)
    moon_rect = current_moon.get_rect()
    cloud_x = [0, 30, 70, 45, 105]
    cloud_y = [46, 5, 18, 78, 115]
    cloud_speed = [1.5, 1, 0.5, 1.7, 0.8]

    moyai_x = [random.randrange(0, 5000), random.randrange(0, 5000), random.randrange(0, 5000)]

    def update(self, game):
        self.daytime += 5
        if self.daytime > 2880:
            self.daytime = 0
        # print("Time:", str(int(self.map(self.daytime, 0, 2880, 0, 24))))
        universe_time = self.map(self.daytime, 0, 2880, 0, 360) - 65

        universe_center = pygame.Vector2(SCREEN_WIDTH/2, (SCREEN_HEIGHT*2)/3)
        distance_from_moon = pygame.Vector2(-(SCREEN_WIDTH/2) - (self.moon_rect.width * 1.1), 0).rotate(universe_time + 165)
        distance_from_sun = pygame.Vector2(-(SCREEN_WIDTH/2) - (self.sun_rect.width * 1.1), 0).rotate(universe_time)
        self.sun_rect.centerx = universe_center.x + distance_from_sun.x
        self.sun_rect.centery = universe_center.y + (distance_from_sun.y * 0.5)
        self.moon_rect.centerx = universe_center.x + distance_from_moon.x
        self.moon_rect.centery = universe_center.y + (distance_from_moon.y * 0.5)
        
        for cloud_id in range(len(self.cloud_speed)):
            self.cloud_x[cloud_id] -= game.game_speed * self.cloud_speed[cloud_id]
        for moyai_id in range(len(self.moyai_x)):
            self.moyai_x[moyai_id] -= game.game_speed
    
    def draw_back(self, screen):
        self.draw_universe(screen)

    def draw(self, screen):
        self.draw_cloud(screen)
        self.draw_moyai(screen)
    
    def draw_universe(self, screen):
        if self.daytime <= 500 or self.daytime >= 1950:
            screen.blit(self.current_moon, self.moon_rect)
        else:
            current_choice = random.randrange(0, 100)
            if current_choice <= 7:
                self.current_moon = MOONS[2]
            elif current_choice <= 23:
                self.current_moon = MOONS[1]
            else:
                self.current_moon = MOONS[0]
        if not self.daytime >= 1850 and self.daytime >= 375: 
            screen.blit(self.current_sun, self.sun_rect)
        else:
            current_choice = random.randrange(0, 100)
            if current_choice <= 2:
                self.current_sun = SUNS[2]
            elif current_choice <= 18:
                self.current_sun = SUNS[1]
            else:
                self.current_sun = SUNS[0]
    
    def chose_color(self):
        number = 255
        pure_day = 850
        dawn_gap = 250
        pure_night = 1850
        morning_gap = 350
        if self.daytime >= pure_day + 1 and self.daytime <= pure_night - dawn_gap - 1:
            number = 255
        elif self.daytime >= pure_night + 1 or self.daytime <= pure_day - morning_gap - 1:
            number = 0
        else:
            if self.daytime >= pure_night - dawn_gap and self.daytime <= pure_night:
                # Night Night
                number = self.map(self.daytime, pure_night, pure_night - morning_gap, 0, 255, True)
            if self.daytime >= pure_day - morning_gap and self.daytime <= pure_day:
                # Rise and shine
                number = self.map(self.daytime, pure_day - dawn_gap, pure_day, 0, 255, True)
        return (number, number, number)
    
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
    
    def map(self, val, min, max, new_min, new_max, clamp=False):
        new_value = ((new_max-new_min)*((100*(val-min))/(max-min)))/100
        if clamp:
            if new_value < new_min:
                new_value = new_min
            if new_value > new_max:
                new_value = new_max
        return new_value