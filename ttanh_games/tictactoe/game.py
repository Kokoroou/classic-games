"""
Game logic for the Tic Tac Toe game.
"""

import pygame

from ttanh_games.tictactoe import constants


def show_instructions(screen: pygame.Surface) -> None:
    """Shows the instructions screen.

    :param screen: The surface to draw on.
    :type screen: pygame.Surface
    :rtype: None
    """
    screen.fill(constants.BLACK)
    font = pygame.font.Font(None, 36)
    instructions: list[str] = [
        "Welcome to Tic Tac Toe!",
        "",
        "Player 1: Click to place X",
        "Player 2: Click to place O",
        "",
        "First to get three in a row wins!",
        "---Press any key to start---",
    ]
    y: int = constants.HEIGHT // 4
    for line in instructions:
        text: pygame.Surface = font.render(line, True, constants.WHITE)
        text_rect: pygame.Rect = text.get_rect(center=(constants.WIDTH // 2, y))
        screen.blit(text, text_rect)
        y += 50
    pygame.display.flip()

    waiting: bool = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False


def game_loop(screen: pygame.Surface) -> None:
    """Main game loop.

    :param screen: The surface to draw on.
    :type screen: pygame.Surface
    :rtype: None
    """
    board: list[list[str]] = [[""] * 3 for _ in range(3)]  #: The Tic Tac Toe board.
    player: str = "X"  #: The current player.
    game_over: bool = False  #: Whether the game is over.
    font: pygame.font.Font = pygame.font.Font(None, 72)  #: The font to use.

    def draw_board() -> None:
        """Draws the Tic Tac Toe board.

        :rtype: None
        """
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(
                    screen,
                    constants.WHITE,
                    (j * 200, i * 200, 200, 200),
                    1,
                )
                if board[i][j] != "":
                    text: pygame.Surface = font.render(
                        board[i][j], True, constants.WHITE
                    )
                    text_rect: pygame.Rect = text.get_rect(
                        center=(j * 200 + 100, i * 200 + 100)
                    )
                    screen.blit(text, text_rect)

    def check_winner() -> str | None:
        """Checks if there is a winner.

        :rtype: str | None
        """
        # Check rows
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]

        # Check columns
        for j in range(3):
            if board[0][j] == board[1][j] == board[2][j] != "":
                return board[0][j]

        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]

        # Check for a tie
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    return None

        return "Tie"

    running: bool = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_x: int = event.pos[0]
                mouse_y: int = event.pos[1]
                clicked_row: int = mouse_y // 200
                clicked_col: int = mouse_x // 200

                if board[clicked_row][clicked_col] == "":
                    board[clicked_row][clicked_col] = player
                    winner: str | None = check_winner()
                    if winner:
                        game_over = True
                    else:
                        player = "O" if player == "X" else "X"

        screen.fill(constants.BLACK)
        draw_board()

        if game_over:
            screen.fill(constants.BLACK)
            if winner == "Tie":
                text: pygame.Surface = font.render("It's a Tie!", True, constants.WHITE)
            else:
                text: pygame.Surface = font.render(
                    f"{winner} wins!", True, constants.WHITE
                )
            text_rect: pygame.Rect = text.get_rect(
                center=(constants.WIDTH // 2, constants.HEIGHT // 2)
            )
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

        pygame.display.flip()

    if __name__ == "__main__":
        pygame.quit()
