from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.bullet import Bullet
from dino_runner.utils.constants import (SPELL_CIRCLE, CHEN, SCREEN_WIDTH, SCREEN_HEIGHT)

import pygame

class Chen(Obstacle):
    def __init__(self):
        self.timer = 0
        self.phase = 0
        self.bullets = []
        super().__init__(CHEN)
        self.rect.x = SCREEN_WIDTH - (self.sprite.get_width()/2)
        self.rect.y = (SCREEN_HEIGHT/2) - (self.sprite.get_height()/2)
    
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(game)
            bullet.collision(game)
            if bullet.dead:
                self.bullets.remove(bullet)
        
        spawn_pos = pygame.Vector2(self.rect.centerx, self.rect.centery)

        if self.timer == 0:
            self.shoot(spawn_pos)
        
        self.timer += 1

        self.move()
        
        if self.timer >= 60 and self.phase >= 4:
            return False
        else: 
            return True
    
    def shoot(self, spawn_pos):
        current_direction = pygame.Vector2(1, 0)
        for i in range(6):
            self.bullets.append(Bullet(3, spawn_pos, current_direction, 35))
            current_direction = current_direction.rotate(60)
    
    def move(self):
        dimentions = pygame.Vector2(SCREEN_WIDTH, SCREEN_HEIGHT).normalize()
        true_speed = 15
        base_speed = pygame.Vector2(dimentions.x * true_speed, dimentions.y * true_speed)
        if self.phase == 0:
            self.rect.y -= base_speed.y / (self.timer/10)
            self.rect.x -= base_speed.x / (self.timer/10)
        if self.phase == 1:
            self.rect.y += base_speed.y / (self.timer/10)
            self.rect.x -= base_speed.x / (self.timer/10)
        if self.phase == 2:
            self.rect.y += base_speed.y / (self.timer/10)
            self.rect.x += base_speed.x / (self.timer/10)
        if self.phase == 3:
            self.rect.y -= base_speed.y / (self.timer/10)
            self.rect.x += base_speed.x / (self.timer/10)

        if self.timer >= 40 and self.phase < 4:
            self.phase += 1
            self.timer = 0
    
    def draw(self, screen):
        screen.blit(SPELL_CIRCLE, (
            self.rect.x - (SPELL_CIRCLE.get_width()/2) + (self.sprite.get_width()/2), 
            self.rect.y - (SPELL_CIRCLE.get_height()/2) + (self.sprite.get_height()/2)
            ))
        screen.blit(self.sprite, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)