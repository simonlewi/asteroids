# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

from player import Player

def print_screen_width_height():
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    print("Starting asteroids!")
    print_screen_width_height()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Update game state
        player.update(dt)
        
        # Draw everything
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
