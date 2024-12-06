# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *

def print_screen_width_height():
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

def main():
    pygame.init()
    print("Starting asteroids!")
    print_screen_width_height()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()
