"""
Ball for the Breakout game.
"""

import pygame

from ttanh_games.breakout.constants import BALL_RADIUS
from ttanh_games.constants import HEIGHT, WHITE, WIDTH


class Ball:
    """
    Ball class.
    """

    def __init__(self) -> None:
        """
        Initializes the ball.

        :rtype: None
        """
        self.x: int = WIDTH // 2
        self.y: int = HEIGHT // 2
        self.radius: int = BALL_RADIUS
        self.speed_x: int = 0
        self.speed_y: int = int(5 * 0.8)

    def move(self) -> None:
        """
        Moves the ball.

        :rtype: None
        """
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.speed_x *= -1
        if self.y < self.radius or self.y > HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the ball.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        :rtype: None
        """
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
