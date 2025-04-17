"""
Main file to run the Breakout game.
"""

from ttanh_games.breakout.game import Game


def run_game() -> None:
    """
    Initializes and runs the Breakout game.

    :rtype: None
    """
    game: Game = Game()
    game.run()


if __name__ == "__main__":
    run_game()
