"""Main file to run the Tic Tac Toe game."""

import pygame

from ttanh_games.tictactoe.game import Game


def run_game() -> None:
    """Initializes and runs the Tic Tac Toe game."""
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    run_game()
    pygame.quit()
