import sys

import pygame
from game import Game


def main() -> None:
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
