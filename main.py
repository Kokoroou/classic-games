"""
Main module for the game launcher.
"""

import sys

import pygame

from ttanh_games.breakout import main as breakout_main
from ttanh_games.constants import HEIGHT, WIDTH
from ttanh_games.pong import main as pong_main
from ttanh_games.snake import main as snake_main
from ttanh_games.tictactoe import main as tictactoe_main


def main() -> None:
    """
    Initializes pygame and creates the game selection menu.
    :return: None
    """
    pygame.init()

    screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Classic Games Launcher")
    font_instruction: pygame.font.Font = pygame.font.Font(None, 24)
    instruction_color: tuple[int, int, int] = (200, 200, 200)
    instruction_text: str = "Click on a game to play!"
    instruction_surface: pygame.Surface = font_instruction.render(
        instruction_text, True, instruction_color
    )
    instruction_rect: pygame.Rect = instruction_surface.get_rect(
        center=(WIDTH // 2, HEIGHT - 50)
    )

    font: pygame.font.Font = pygame.font.Font(None, 36)
    text_color: tuple[int, int, int] = (255, 255, 255)
    background_color: tuple[int, int, int] = (0, 0, 0)

    game_options: list[tuple[str, callable]] = [
        ("Breakout", breakout_main.run_game),
        ("Pong", pong_main.run_game),
        ("Snake", snake_main.main),
        ("Tic Tac Toe", tictactoe_main.run_game),
    ]

    while True:
        pygame.init()
        font: pygame.font.Font = pygame.font.Font(None, 36)
        screen.fill(background_color)

        for i, (game_name, _) in enumerate(game_options):
            text_surface: pygame.Surface = font.render(game_name, True, text_color)
            text_rect: pygame.Rect = text_surface.get_rect(
                center=(WIDTH // 2, HEIGHT // 4 + i * 50)
            )
            screen.blit(text_surface, text_rect)
        screen.blit(instruction_surface, instruction_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
                for i, (game_name, game_function) in enumerate(game_options):
                    text_surface: pygame.Surface = font.render(
                        game_name, True, text_color
                    )
                    text_rect: pygame.Rect = text_surface.get_rect(
                        center=(WIDTH // 2, HEIGHT // 4 + i * 50)
                    )
                    if text_rect.collidepoint(mouse_pos):
                        game_function()  # Run the selected game
                        pygame.quit()

        pygame.display.flip()


if __name__ == "__main__":
    main()
