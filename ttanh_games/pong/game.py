"""
Game logic for the Pong game.
"""

import pygame

from ttanh_games.commons import show_result
from ttanh_games.constants import BLACK, HEIGHT, WHITE, WIDTH
from ttanh_games.pong import ball, paddle
from ttanh_games.pong.constants import PADDLE_HEIGHT, PADDLE_WIDTH


class Game:
    """
    Represents the Pong game.
    """

    def __init__(self) -> None:
        """
        Initializes the game.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()
        self.player1 = paddle.Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.player2 = paddle.Paddle(
            WIDTH - 50 - PADDLE_WIDTH,
            HEIGHT // 2 - PADDLE_HEIGHT // 2,
        )
        self.ball = ball.Ball()
        self.player1_score = 0
        self.player2_score = 0
        self.winning_score = 10
        self.winner = None
        self.running = True
        self.font = pygame.font.Font(None, 36)

    def show_instructions(self) -> None:
        """
        Shows the instructions screen.
        """
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        instructions = [
            "Welcome to Pong!",
            "",
            "Player 1: Use W and S to move up and down",
            "Player 2: Use UP and DOWN arrows to move up and down",
            "",
            "First to 10 points wins!",
            "---Press any key to start---",
        ]
        y = HEIGHT // 4
        for line in instructions:
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(WIDTH // 2, y))
            self.screen.blit(text, text_rect)
            y += 50
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def run(self) -> None:
        """
        Runs the main game loop.
        """
        self.show_instructions()

        while self.running:
            # Event handling
            if (
                self.player1_score >= self.winning_score
                or self.player2_score >= self.winning_score
            ):
                self.running = False
                if self.player1_score >= self.winning_score:
                    self.winner = 1
                else:
                    self.winner = 2
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Player input
            keys = pygame.key.get_pressed()
            player1_direction = 0
            player2_direction = 0
            if keys[pygame.K_w]:
                player1_direction = -1
            if keys[pygame.K_s]:
                player1_direction = 1
            if keys[pygame.K_UP]:
                player2_direction = -1
            if keys[pygame.K_DOWN]:
                player2_direction = 1

            self.player1.move(player1_direction)
            self.player2.move(player2_direction)

            # Ball movement and collision
            self.ball.move()

            # Collision with paddles
            if self.ball.x > WIDTH or self.ball.x < 0:
                if self.ball.x < 0:
                    self.player2_score += 1
                else:
                    self.player1_score += 1
                self.ball = ball.Ball()
                self.ball.start()
            else:
                # Calculate the distance between the center of the ball
                # and the center of the paddle
                # Collision with paddles
                if (
                    self.ball.x + self.ball.radius > self.player1.x
                    and self.ball.x - self.ball.radius < self.player1.x + PADDLE_WIDTH
                    and self.ball.y + self.ball.radius > self.player1.y
                    and self.ball.y - self.ball.radius < self.player1.y + PADDLE_HEIGHT
                ) or (
                    self.ball.x + self.ball.radius > self.player2.x
                    and self.ball.x - self.ball.radius < self.player2.x + PADDLE_WIDTH
                    and self.ball.y + self.ball.radius > self.player2.y
                    and self.ball.y - self.ball.radius < self.player2.y + PADDLE_HEIGHT
                ):
                    self.ball.speed_x *= -1

            # Drawing
            self.screen.fill(BLACK)
            self.player1.draw(self.screen)
            self.player2.draw(self.screen)
            self.ball.draw(self.screen)

            # Draw scores
            text = self.font.render(
                f"{self.player1_score} - {self.player2_score}", True, WHITE
            )
            text_rect = text.get_rect(center=(WIDTH // 2, 30))
            self.screen.blit(text, text_rect)

            # Update display
            pygame.display.flip()

            # Control frame rate
            self.clock.tick(60)

        if self.winner:
            show_result(screen=self.screen, result=f"Player {self.winner} wins!")
