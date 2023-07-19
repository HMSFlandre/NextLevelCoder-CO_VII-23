from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.bullet import Bullet
from dino_runner.utils.constants import (SPELL_CIRCLE, SCREEN_WIDTH)

import pygame

class Spell(Obstacle):
    def __init__(self):
        self.timer = 0
        self.bullets = []
        super().__init__(SPELL_CIRCLE)
        self.rect.x = SCREEN_WIDTH - SPELL_CIRCLE.get_width() - 80
        self.rect.y = 320
    
    def update(self, game):
        for bullet in self.bullets:
            bullet.update(game)
            bullet.collision(game)
            if bullet.dead:
                self.bullets.remove(bullet)
        self.timer += 1
        player_dir = pygame.Vector2(
            game.player.rect.centerx - self.rect.centerx,
            game.player.rect.centery - self.rect.centery).normalize()
        spawn_pos = pygame.Vector2(self.rect.centerx, self.rect.centery)
        if self.timer >= 20 and self.timer <= 40:
            self.rect.y -= 15
        
        if self.timer == 20:
            self.bullets.append(Bullet(0, spawn_pos, player_dir))
        if self.timer == 30:
            self.bullets.append(Bullet(1, spawn_pos, player_dir))
        if self.timer == 40:
            self.bullets.append(Bullet(2, spawn_pos, player_dir))
        
        if self.timer >= 90:
            return False
        else: 
            return True
    
    def draw(self, screen):
        screen.blit(self.sprite, self.rect)
        for bullet in self.bullets:
            bullet.draw(screen)