"""
Main entry point for the Pong game.
"""

from ttanh_games.pong.game import Game


def run_game() -> None:
    """
    Main function to run the Pong game.
    """
    game = Game()
    game.run()


if __name__ == "__main__":
    run_game()
