# Player class inherits from CircleShape

from circleshape import *

from constants import (
    PLAYER_RADIUS, 
    PLAYER_TURN_SPEED, 
    PLAYER_SPEED,
    PLAYER_BOUNDARY_OFFSET, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT,
    )

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    # Player rotation with A, D
    def rotate(self, dt):
        self.rotation = self.rotation + (PLAYER_TURN_SPEED * dt)
    
    # Player movement back and forth
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        new_position = self.position + (forward * PLAYER_SPEED * dt)

    # Move only if within bounds (extra feature)
        if (0 <= new_position.x <= SCREEN_WIDTH - PLAYER_BOUNDARY_OFFSET and 0 <= new_position.y <= SCREEN_HEIGHT - PLAYER_BOUNDARY_OFFSET):
            self.position = new_position
            
        


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


        