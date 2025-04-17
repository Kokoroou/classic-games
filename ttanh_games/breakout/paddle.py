"""
Paddle for the Breakout game.
"""

from ttanh_games.breakout import constants
import pygame


class Paddle:
    """
    Paddle class.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initializes the paddle.

        :param x: The x position of the paddle.
        :type x: int
        :param y: The y position of the paddle.
        :type y: int
        :rtype: None
        """
        self.x: int = x
        self.y: int = y
        self.width: int = constants.PADDLE_WIDTH
        self.height: int = constants.PADDLE_HEIGHT

    def move(self, direction: int) -> None:
        """
        Moves the paddle.

        :param direction: The direction to move the paddle. -1 is up, 1 is down.
        :type direction: int
        :rtype: None
        """
        self.x += direction * 5
        if self.x < 0:
            self.x = 0
        if self.x > constants.WIDTH - self.width:
            self.x = constants.WIDTH - self.width

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the paddle.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        :rtype: None
        """
        pygame.draw.rect(
            screen, constants.WHITE, (self.x, self.y, self.width, self.height)
        )
