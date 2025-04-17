"""
Game logic for the Breakout game.
"""

import math

import pygame

from ttanh_games.breakout import ball, brick, paddle
from ttanh_games.breakout.constants import (
    BRICK_HEIGHT,
    BRICK_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_WIDTH,
)
from ttanh_games.commons import show_result
from ttanh_games.constants import BLACK, HEIGHT, WHITE, WIDTH
from ttanh_games.commons import countdown

class Game:
    """
    Game class for Breakout.
    """

    def __init__(self) -> None:
        """
        Initializes the game.
        """
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Breakout")
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # Initialize paddle
        self.player_paddle: paddle.Paddle = paddle.Paddle(
            WIDTH // 2 - PADDLE_WIDTH // 2,
            HEIGHT - PADDLE_HEIGHT - 20,
        )

        # Initialize ball
        self.ball_instance: ball.Ball = ball.Ball()

        # Initialize bricks
        self.bricks: list[brick.Brick] = []
        colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
        for i in range(5):
            for j in range(11):
                brick_instance = brick.Brick(
                    j * (BRICK_WIDTH + 5) + 50,
                    i * (BRICK_HEIGHT + 5) + 50,
                    colors[i],
                )
                self.bricks.append(brick_instance)

        self.running: bool = True

    def show_instructions(self) -> None:
        """
        Shows the instructions screen.
        """
        self.screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        instructions = [
            "Welcome to Breakout!",
            "",
            "Use LEFT and RIGHT arrows to move the paddle",
            "",
            "Break all the bricks to win!",
            "Don't let the ball hit the bottom!",
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
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def game_loop(self) -> None:
        """
        Main game loop.

        Args:
            screen (pygame.Surface): The game screen.
        """
        while self.running:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Player input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player_paddle.move(-1)
            if keys[pygame.K_RIGHT]:
                self.player_paddle.move(1)

            # Ball movement
            self.ball_instance.move()

            # Collision with paddle
            if (
                self.ball_instance.x + self.ball_instance.radius > self.player_paddle.x
                and self.ball_instance.x - self.ball_instance.radius
                < self.player_paddle.x + self.player_paddle.width
                and self.ball_instance.y + self.ball_instance.radius > self.player_paddle.y
                and self.ball_instance.y - self.ball_instance.radius
                < self.player_paddle.y + self.player_paddle.height
            ):
                # Calculate the distance from the center of the paddle to
                # the point of collision
                collision_point = self.ball_instance.x - (
                    self.player_paddle.x + self.player_paddle.width // 2
                )
                # Normalize the distance to a range of -1 to 1
                normalized_collision_point = collision_point / (
                    self.player_paddle.width // 2
                )
                # Calculate the bounce angle
                bounce_angle = (
                    normalized_collision_point * 75
                )  # Max bounce angle of 75 degrees
                # Update the ball's speed
                self.ball_instance.speed_x = int(
                    4 * math.sin(math.radians(bounce_angle))
                )
                self.ball_instance.speed_y *= -1

            # Collision with bricks
            for brick_instance in self.bricks:
                if (
                    self.ball_instance.x + self.ball_instance.radius > brick_instance.x
                    and self.ball_instance.x - self.ball_instance.radius
                    < brick_instance.x + brick_instance.width
                    and self.ball_instance.y + self.ball_instance.radius > brick_instance.y
                    and self.ball_instance.y - self.ball_instance.radius
                    < brick_instance.y + brick_instance.height
                ):
                    self.ball_instance.speed_y *= -1
                    self.bricks.remove(brick_instance)
                    break

            # Check if game is over
            if self.ball_instance.y > HEIGHT - self.ball_instance.radius:
                self.running = False

            if not self.bricks:
                self.running = False

            # Drawing
            self.screen.fill(BLACK)
            self.player_paddle.draw(self.screen)
            self.ball_instance.draw(self.screen)
            for brick_instance in self.bricks:
                brick_instance.draw(self.screen)

            # Update display
            pygame.display.flip()

            # Control frame rate
            self.clock.tick(60)

        if not self.bricks:
            show_result(self.screen, "You win!")
        else:
            show_result(self.screen, "You lose!")

    def run(self) -> None:
        """
        Runs the game.
        """
        self.show_instructions()

        countdown(self.screen)
        self.game_loop()
