"""
Ball class for the Pong game.
"""

import random

from ttanh_games.pong import constants
import pygame


class Ball:
    """
    Represents the ball in the Pong game.
    """

    def __init__(self) -> None:
        """
        Initializes the ball.
        """
        self.x = constants.WIDTH // 2
        self.y = constants.HEIGHT // 2
        self.radius = constants.BALL_RADIUS
        self.speed_x = constants.BALL_SPEED_X
        self.speed_y = constants.BALL_SPEED_Y

    def start(self) -> None:
        """
        Starts the ball in a random direction.
        """
        random_direction_x = random.choice([-1, 1])
        random_direction_y = random.choice([-1, 1])
        self.speed_x = constants.BALL_SPEED_X * random_direction_x
        self.speed_y = constants.BALL_SPEED_Y * random_direction_y

    def move(self) -> None:
        """
        Moves the ball and handles collisions.
        """
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off top and bottom
        if self.y - self.radius < 0 or self.y + self.radius > constants.HEIGHT:
            self.speed_y *= -1

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the ball on the screen.

        :param screen: The Pygame screen object.

        :param screen: The Pygame screen object.
        """
        pygame.draw.circle(screen, constants.WHITE, (self.x, self.y), self.radius)
