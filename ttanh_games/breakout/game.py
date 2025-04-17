"""
Game logic for the Breakout game.
"""

import math

import pygame

from ttanh_games.breakout import ball, brick, paddle
from ttanh_games.breakout.constants import (
    BLACK,
    BRICK_HEIGHT,
    BRICK_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_WIDTH,
    WHITE,
)
from ttanh_games.constants import HEIGHT, WIDTH


def show_instructions(screen: pygame.Surface) -> None:
    """
    Shows the instructions screen.
    """
    screen.fill(BLACK)
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
        screen.blit(text, text_rect)
        y += 50
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


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


def game_loop(screen: pygame.Surface) -> None:
    """
    Main game loop.

    Args:
        screen (pygame.Surface): The game screen.
    """
    # Initialize paddle
    player_paddle = paddle.Paddle(
        WIDTH // 2 - PADDLE_WIDTH // 2,
        HEIGHT - PADDLE_HEIGHT - 20,
    )

    # Initialize ball
    ball_instance = ball.Ball()

    # Initialize bricks
    bricks: list[brick.Brick] = []
    colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255)]
    for i in range(5):
        for j in range(11):
            brick_instance = brick.Brick(
                j * (BRICK_WIDTH + 5) + 50,
                i * (BRICK_HEIGHT + 5) + 50,
                colors[i],
            )
            bricks.append(brick_instance)

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_paddle.move(-1)
        if keys[pygame.K_RIGHT]:
            player_paddle.move(1)

        # Ball movement
        ball_instance.move()

        # Collision with paddle
        if (
            ball_instance.x + ball_instance.radius > player_paddle.x
            and ball_instance.x - ball_instance.radius
            < player_paddle.x + player_paddle.width
            and ball_instance.y + ball_instance.radius > player_paddle.y
            and ball_instance.y - ball_instance.radius
            < player_paddle.y + player_paddle.height
        ):
            # Calculate the distance from the center of the paddle to
            # the point of collision
            collision_point = ball_instance.x - (
                player_paddle.x + player_paddle.width // 2
            )
            # Normalize the distance to a range of -1 to 1
            normalized_collision_point = collision_point / (player_paddle.width // 2)
            # Calculate the bounce angle
            bounce_angle = (
                normalized_collision_point * 75
            )  # Max bounce angle of 75 degrees
            # Update the ball's speed
            ball_instance.speed_x = int(4 * math.sin(math.radians(bounce_angle)))
            ball_instance.speed_y *= -1

        # Collision with bricks
        for brick_instance in bricks:
            if (
                ball_instance.x + ball_instance.radius > brick_instance.x
                and ball_instance.x - ball_instance.radius
                < brick_instance.x + brick_instance.width
                and ball_instance.y + ball_instance.radius > brick_instance.y
                and ball_instance.y - ball_instance.radius
                < brick_instance.y + brick_instance.height
            ):
                ball_instance.speed_y *= -1
                bricks.remove(brick_instance)
                break

        # Check if game is over
        if ball_instance.y > HEIGHT - ball_instance.radius:
            running = False

        if not bricks:
            running = False

        # Drawing
        screen.fill(BLACK)
        player_paddle.draw(screen)
        ball_instance.draw(screen)
        for brick_instance in bricks:
            brick_instance.draw(screen)

        # Update display
        pygame.display.flip()

        # Control frame rate
        pygame.time.Clock().tick(60)

    if not bricks:
        show_result(screen, "You win!")
    else:
        show_result(screen, "You lose!")
    pygame.quit()
