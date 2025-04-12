import pygame
import constants
from game import show_instructions, countdown, game_loop

def run_game() -> None:
    pygame.init()
    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption("Pong")
    show_instructions(screen)
    countdown(screen)
    game_loop(screen)

if __name__ == "__main__":
    run_game()
