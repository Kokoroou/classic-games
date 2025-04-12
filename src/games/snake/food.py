import random

import pygame
from constants import (
    GRID_SIZE,
    RED,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1),
            random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1),
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            RED,
            (
                self.position[0] * GRID_SIZE,
                self.position[1] * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE,
            ),
        )
