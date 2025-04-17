"""
Paddle class for the Pong game.
"""

import pygame

from ttanh_games.pong import constants


class Paddle:
    """
    Represents a paddle in the Pong game.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes the paddle.

        :param x: The x-coordinate of the paddle.
        :param y: The y-coordinate of the paddle.
        """
        self.x = x
        self.y = y
        self.width = constants.PADDLE_WIDTH
        self.height = constants.PADDLE_HEIGHT
        self.rect = pygame.Rect(
            self.x, self.y, self.width, self.height, border_radius=5
        )

    def move(self, direction: int) -> None:
        """
        Moves the paddle up or down.

        :param direction: 1 for up, -1 for down.
        """
        self.y += direction * constants.PADDLE_SPEED
        # Keep paddle within screen bounds
        if self.y < 0:
            self.y = 0
        if self.y > constants.HEIGHT - self.height:
            self.y = constants.HEIGHT - self.height
        self.rect.y = self.y

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the paddle on the screen.

        :param screen: The Pygame screen object.
        """
        pygame.draw.rect(screen, constants.WHITE, self.rect)
