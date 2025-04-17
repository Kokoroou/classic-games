import pygame

from ttanh_games.commons import countdown
from ttanh_games.constants import HEIGHT, WIDTH
from ttanh_games.pong.game import game_loop, show_instructions


def run_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong")
    show_instructions(screen)
    countdown(screen)
    game_loop(screen)


if __name__ == "__main__":
    run_game()
    pygame.quit()
