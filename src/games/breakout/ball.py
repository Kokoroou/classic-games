"""
Ball for the Breakout game.
"""

import constants
import pygame


class Ball:
    """
    Ball class.
    """

    def __init__(self) -> None:
        """
        Initializes the ball.

        :rtype: None
        """
        self.x: int = constants.WIDTH // 2
        self.y: int = constants.HEIGHT // 2
        self.radius: int = constants.BALL_RADIUS
        self.speed_x: int = 0
        self.speed_y: int = int(5 * 0.8)

    def move(self) -> None:
        """
        Moves the ball.

        :rtype: None
        """
        self.x += self.speed_x
        self.y += self.speed_y

        if self.x < self.radius or self.x > constants.WIDTH - self.radius:
            self.speed_x *= -1
        if self.y < self.radius or self.y > constants.HEIGHT - self.radius:
            self.speed_y *= -1

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the ball.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        :rtype: None
        """
        pygame.draw.circle(screen, constants.WHITE, (self.x, self.y), self.radius)
