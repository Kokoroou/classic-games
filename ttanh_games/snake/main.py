import pygame

from ttanh_games.snake.game import Game


def run_game() -> None:
    pygame.init()
    game = Game()
    game.run()


if __name__ == "__main__":
    run_game()
    pygame.quit()
