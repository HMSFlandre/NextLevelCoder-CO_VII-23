from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BULLETS

import pygame

class Bullet(Obstacle):
    def __init__(self, color, pos, vel, speed=25):
        self.speed = speed
        self.vel = vel
        if color < 0:
            color = 0
        if color > 3:
            color = 3
        option = BULLETS[color]
        super().__init__(option)
        self.rect.centerx = pos.x
        self.rect.centery = pos.y
    
    def collision(self, game):
        if game.player.barrier_collision(self):
            game.player.barrier -= 60
            game.player.continuous_point_collection -= 4
            self.kill()
            return
        
        if game.player.shield_collision(self):
            game.player.protoshield -= 1
            game.score -= (500 + int(game.score / 100))
            game.player.continuous_point_collection = 1
            self.kill()
            return

        if game.player.collision(self):
            game.playing = False
    
    def update(self, game):
        self.rect.x += self.vel.x * self.speed
        self.rect.y += self.vel.y * self.speed
        return self.rect.x >= -self.sprite.get_width()
    
    def draw(self, screen):
        screen.blit(self.sprite, self.rect)