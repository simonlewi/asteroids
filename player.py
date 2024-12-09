# Player class

import pygame
from pygame.math import Vector2
from circleshape import *
from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED,
    PLAYER_BOUNDARY_OFFSET, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN
    )
from shot import Shot
test_vector = Vector2(1, 1)

class Player(CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.cooldown_timer = 0
        
    # Player shape and color
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Draw player
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Player rotation with A, D
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    # Player movement back and forth with W, S
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = self.position + (forward * PLAYER_SPEED * dt)
        # Move only if within bounds (extra feature)
        if (0 <= new_position.x <= SCREEN_WIDTH - PLAYER_BOUNDARY_OFFSET and 0 <= new_position.y <= SCREEN_HEIGHT - PLAYER_BOUNDARY_OFFSET):
            self.position = new_position
    
    # Shooting mechanism
    def shoot(self):
        if self.cooldown_timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shots_group.add(shot)
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.cooldown_timer = max(0, self.cooldown_timer - dt)


        