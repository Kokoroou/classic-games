"""
Main file to run the Tic Tac Toe game.
"""

import pygame

from ttanh_games.tictactoe import constants
from ttanh_games.tictactoe.game import game_loop, show_instructions


def run_game() -> None:
    """Initializes and runs the Tic Tac Toe game.

    :rtype: None
    """
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (constants.WIDTH, constants.HEIGHT)
    )
    pygame.display.set_caption("Tic Tac Toe")
    show_instructions(screen)
    game_loop(screen)


if __name__ == "__main__":
    run_game()
    pygame.quit()
