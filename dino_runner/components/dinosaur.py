import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (
    RUNNING, DUCKING, JUMPING, 
    HITBOX, P_SHIELD, SCREEN_HEIGHT, 
    SCREEN_WIDTH, SHIELD_SILOUETTE, SKULLS, 
    SKULL_BAR, BAR_FILL)
from dino_runner.components.obstacles.obstacle import Obstacle

class Dinosaur:

    POS_X = 130
    POS_Y = 300
    DUCKING_POS_Y = 335
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.skull = SKULLS[0]
        self.skull_step = 0
        self.rect = self.image.get_rect()
        self.small_hitbox = HITBOX.get_rect()
        self.shield_hitbox = P_SHIELD.get_rect()
        self.rect.x = 80
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.continuous_point_collection = 1
        self.graze = 0
        self.protoshield = 0
        self.barrier = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jump_speed = self.JUMP_VEL
        self.has_powerup = self.protoshield > 0 or self.graze > 0
    

    def update(self, user_input):
        if self.skull_step < 20:
            self.skull = SKULLS[0]
        elif self.skull_step > 40:
            self.skull = SKULLS[2]
        else:
            self.skull = SKULLS[1]

        if self.continuous_point_collection < 0:
            self.continuous_point_collection = 0
        if self.continuous_point_collection > 10:
            self.continuous_point_collection = 10

        if self.graze > 0:
            self.graze -= 1
        
        if self.barrier > 0:
            self.skull_step += 1
            self.barrier -= 1
            if self.barrier > 600:
                self.barrier = 600

        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()
        
        self.small_hitbox.x = self.rect.centerx - (self.small_hitbox.width/2)
        self.small_hitbox.y = self.rect.centery - (self.small_hitbox.height/2)

        self.shield_hitbox.x = self.rect.right - (self.shield_hitbox.width/3)
        self.shield_hitbox.y = self.rect.centery - (self.shield_hitbox.height/2)

        if user_input[pygame.K_DOWN] and not self.jumping:
            self.running = False
            self.ducking = True
            self.jumping = False
        elif user_input[pygame.K_SPACE] and not self.jumping:
            self.running = False
            self.ducking = False
            self.jumping = True
        elif not self.jumping:
            self.running = True
            self.ducking = False
            self.jumping = False
        
        if self.step_index > 10:
            self.step_index = 0
        
        if self.skull_step > 45:
            self.skull_step = 0


    def pickup_collision(self, object):
        return self.rect.colliderect(object.rect)
    
    def collision(self, object):
        if self.graze > 0:
            return self.small_hitbox.colliderect(object.rect)
        else:
            return self.rect.colliderect(object.rect)
    

    def shield_collision(self, object):
        if self.protoshield > 0:
            return self.shield_hitbox.colliderect(object.rect)
        else:
            return False


    def barrier_collision(self, object):
        barrier_size = 120
        if self.barrier > 0:
            return pygame.Rect(self.rect.centerx - (barrier_size/2), 
                self.rect.centery - (barrier_size/2), 
                barrier_size, barrier_size).colliderect(object.rect)


    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.graze > 0:
            screen.blit(HITBOX, self.small_hitbox)
        if self.protoshield > 0:
            screen.blit(P_SHIELD, self.shield_hitbox)
        if self.barrier > 0:
            base_pos = pygame.Vector2((60 + (self.skull.get_rect().width/2)) * (
                1 - self.map(self.skull_step, 0, 45, 0, 0.35, True)), 0).rotate(
                self.map(self.skull_step, 0, 45, 0, 360, True))
            for i in range(4):
                base_pos = base_pos.rotate(90*i)
                screen.blit(self.skull, (self.rect.centerx + base_pos.x - (self.skull.get_rect().width/2), 
                    self.rect.centery + base_pos.y - (self.skull.get_rect().height/2)))
    
    def draw_ui(self, screen):
        font = pygame.font.SysFont('Comic Sans MS', 15)
        bar_pos = (SCREEN_WIDTH - 170, SCREEN_HEIGHT - 40)
        screen.blit(SKULL_BAR, bar_pos)
        for i in range(int(self.map(self.barrier, 0, 600, 0, 27, True))):
            screen.blit(BAR_FILL, (bar_pos[0] + 36 + (4*i), bar_pos[1] + 8))
        if self.protoshield > 0:
            shield_text = font.render("Shield", False, (127, 127, 127))
            screen.blit(shield_text, (20, SCREEN_HEIGHT - 80))
            for i in range(5):
                if self.protoshield >= i+1:
                    screen.blit(P_SHIELD, (20 + (i * 25), SCREEN_HEIGHT - 60))
                else:
                    screen.blit(SHIELD_SILOUETTE, (20 + (i * 25), SCREEN_HEIGHT - 60))

    def run(self):
        self.image = RUNNING[0] if self.step_index < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.step_index += 1


    def jump(self):
        self.image = JUMPING
        if self.jumping:
            self.rect.y -= self.jump_speed * 4
            self.jump_speed -= 0.8
        if self.jump_speed < -self.JUMP_VEL:
            self.rect.y = self.POS_Y
            self.jumping = False
            self.jump_speed = self.JUMP_VEL

    def duck(self):
        self.image = DUCKING[0] if self.step_index < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.DUCKING_POS_Y
        self.step_index += 1
    
    def map(self, val, min, max, new_min, new_max, clamp=False):
        new_value = ((new_max-new_min)*((100*(val-min))/(max-min)))/100
        if clamp:
            if new_value < new_min:
                new_value = new_min
            if new_value > new_max:
                new_value = new_max
        return new_value
