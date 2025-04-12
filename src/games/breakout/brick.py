"""
Brick for the Breakout game.
"""

import constants
import pygame


class Brick:
    """
    Brick class.
    """

    def __init__(self, x: int, y: int, color: tuple[int, int, int]) -> None:
        """
        Initializes the brick.

        :param x: The x position of the brick.
        :type x: int
        :param y: The y position of the brick.
        :type y: int
        :param color: The color of the brick.
        :type color: tuple[int, int, int]
        :rtype: None
        """
        self.x: int = x
        self.y: int = y
        self.width: int = constants.BRICK_WIDTH
        self.height: int = constants.BRICK_HEIGHT
        self.color: tuple[int, int, int] = color

    def draw(self, screen: pygame.Surface) -> None:
        """
        Draws the brick.

        :param screen: The screen to draw on.
        :type screen: pygame.Surface
        :rtype: None
        """
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
