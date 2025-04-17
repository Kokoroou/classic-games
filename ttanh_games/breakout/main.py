"""
Main file to run the Breakout game.
"""
import sys

import pygame

from . import constants
from .game import countdown, game_loop, show_instructions


def run_game() -> None:
    """
    Initializes and runs the Breakout game.

    :rtype: None
    """
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (constants.WIDTH, constants.HEIGHT)
    )
    pygame.display.set_caption("Breakout")
    show_instructions(screen)
    countdown(screen)
    game_loop(screen)


if __name__ == "__main__":
    run_game()
    pygame.quit()
    sys.exit()
