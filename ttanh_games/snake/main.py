import sys

import pygame
from ttanh_games.snake.game import Game


def main() -> None:
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
