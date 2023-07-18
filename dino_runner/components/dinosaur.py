import pygame

from pygame.sprite import Sprite
from dino_runner.utils.constants import (RUNNING, DUCKING, JUMPING)

class Dinosaur:

    POS_X = 130
    POS_Y = 300
    DUCKING_POS_Y = 335
    JUMP_VEL = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = self.POS_Y
        self.step_index = 0
        self.running = True
        self.ducking = False
        self.jumping = False
        self.jump_speed = self.JUMP_VEL
    

    def update(self, user_input):
        if self.jumping:
            self.jump()
        if self.ducking:
            self.duck()
        if self.running:
            self.run()

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
    

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    

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
