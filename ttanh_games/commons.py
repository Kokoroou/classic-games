import pygame

from ttanh_games.constants import BLACK, HEIGHT, WHITE, WIDTH


def countdown(screen: pygame.Surface) -> None:
    """
    Shows a countdown before the game starts.
    """
    for i in range(3, 0, -1):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 72)
        text = font.render(str(i), True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)


def show_result(screen: pygame.Surface, result: str) -> None:
    """
    Shows the result screen.
    """
    screen.fill(BLACK)
    font = pygame.font.Font(None, 72)
    text = font.render(result, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)
