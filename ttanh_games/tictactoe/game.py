"""Game logic for the Tic Tac Toe game."""

import pygame

from ttanh_games.commons import show_result
from ttanh_games.constants import BLACK, HEIGHT, WHITE, WIDTH


class Game:
    """
    Represents the Tic Tac Toe game.
    """

    def __init__(self) -> None:
        """
        Initializes the game.
        """
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.board: list[list[str]] = [[""] * 3 for _ in range(3)]
        self.player: str = "X"
        self.game_over: bool = False
        self.font: pygame.font.Font = pygame.font.Font(None, 72)
        self.offset_x: int = (WIDTH - 600) // 2
        self.offset_y: int = (HEIGHT - 600) // 2
        self.running: bool = True

    def show_instructions(self) -> None:
        """
        Shows the instructions screen.
        """
        self.screen.fill(BLACK)
        font: pygame.font.Font = pygame.font.Font(None, 36)
        instructions: list[str] = [
            "Welcome to Tic Tac Toe!",
            "",
            "Player 1: Click to place X",
            "Player 2: Click to place O",
            "",
            "First to get three in a row wins!",
            "---Press any key to start---",
        ]
        y: int = HEIGHT // 4
        for line in instructions:
            text: pygame.Surface = font.render(line, True, WHITE)
            text_rect: pygame.Rect = text.get_rect(center=(WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()

        waiting: bool = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type in [pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN]:
                    waiting = False

    def draw_board(self) -> None:
        """
        Draws the Tic Tac Toe board.
        """
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(
                    self.screen,
                    WHITE,
                    (j * 200 + self.offset_x, i * 200 + self.offset_y, 200, 200),
                    1,
                )
                if self.board[i][j] != "":
                    text: pygame.Surface = self.font.render(self.board[i][j], True, WHITE)
                    text_rect: pygame.Rect = text.get_rect(
                        center=(j * 200 + self.offset_x + 100, i * 200 + self.offset_y + 100)
                    )
                    self.screen.blit(text, text_rect)

    def check_winner(self) -> str | None:
        """
        Checks if there is a winner.

        :return: The winner (X or O) or None if there is no winner yet, or "Tie" if it's a tie.
        :rtype: str | None
        """
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]

        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != "":
                return self.board[0][j]

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]

        # Check for a tie
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return None

        return "Tie"

    def handle_input(self, event: pygame.event.Event) -> None:
        """
        Handles user input events.

        :param event: The pygame event to handle.
        :type event: pygame.event.Event
        :rtype: None
        """
        if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            mouse_x: int = event.pos[0]
            mouse_y: int = event.pos[1]
            clicked_row: int = (mouse_y - self.offset_y) // 200
            clicked_col: int = (mouse_x - self.offset_x) // 200

            if 0 <= clicked_row < 3 and 0 <= clicked_col < 3:
                if self.board[clicked_row][clicked_col] == "":
                    self.board[clicked_row][clicked_col] = self.player
                    winner: str | None = self.check_winner()
                    if winner:
                        self.game_over = True
                    else:
                        self.player = "O" if self.player == "X" else "X"

    def update(self) -> None:
        """
        Updates the game state.
        """
        pass

    def draw(self) -> None:
        """
        Draws the game elements on the screen.
        """
        self.screen.fill(BLACK)
        self.draw_board()

        if self.game_over:
            winner: str | None = self.check_winner()
            if winner == "Tie":
                show_result(screen=self.screen, result="It's a Tie!")
            else:
                show_result(screen=self.screen, result=f"{winner} wins!")
            self.running = False

        pygame.display.flip()

    def run(self) -> None:
        """
        Runs the main game loop.
        """
        self.show_instructions()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.handle_input(event)

            self.update()
            self.draw()
            self.clock.tick(60)
