import sys

import pygame

from ttanh_games.pong import constants
from ttanh_games.pong.game import countdown, game_loop, show_instructions


def run_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Pong")
    show_instructions(screen)
    countdown(screen)
    game_loop(screen)


if __name__ == "__main__":
    run_game()
    pygame.quit()
    sys.exit()
