# Asteroid class

import pygame
import random
from circleshape import *
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    # Draw the asteroids
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    # Update position
    def update(self, dt):
        self.position += (self.velocity * dt)

    # Split function
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new velocity vectors at angles from the original
        split_angle = random.uniform(20, 50)
        vel1 = self.velocity.rotate(split_angle) * 1.2
        vel2 = self.velocity.rotate(-split_angle) * 1.2

        # Create two new smaller asteroids
        Asteroid(self.position.x, self.position.y, new_radius, vel1)
        Asteroid(self.position.x, self.position.y, new_radius, vel2)

        self.kill()
