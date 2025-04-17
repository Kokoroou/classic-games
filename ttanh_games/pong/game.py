"""
Game logic for the Pong game.
"""

import pygame

from ttanh_games.constants import HEIGHT, WIDTH
from ttanh_games.pong import ball, paddle
from ttanh_games.pong.constants import BLACK, PADDLE_HEIGHT, PADDLE_WIDTH, WHITE


def show_instructions(screen: pygame.Surface) -> None:
    """
    Shows the instructions screen.
    """
    screen.fill(BLACK)
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
        screen.blit(text, text_rect)
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


def game_loop(screen: pygame.Surface) -> None:
    """
    Main game loop.

    Args:
        screen (pygame.Surface): The game screen.
    """
    # Initialize paddles
    player1 = paddle.Paddle(50, HEIGHT // 2 - PADDLE_HEIGHT // 2)
    player2 = paddle.Paddle(
        WIDTH - 50 - PADDLE_WIDTH,
        HEIGHT // 2 - PADDLE_HEIGHT // 2,
    )

    # Initialize ball
    ball_instance = ball.Ball()
    player1_score = 0
    player2_score = 0
    winning_score = 10  # Score needed to win
    running = True
    font = pygame.font.Font(None, 36)  # Initialize font outside the loop
    winner = None  # None, 1, or 2
    while running:
        # Event handling
        if player1_score >= winning_score or player2_score >= winning_score:
            running = False
            if player1_score >= winning_score:
                winner = 1
            else:
                winner = 2
            continue

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        player1.move(player1_direction)
        player2.move(player2_direction)

        # Ball movement and collision
        ball_instance.move()

        # Collision with paddles
        if ball_instance.x > WIDTH or ball_instance.x < 0:
            if ball_instance.x < 0:
                player2_score += 1
            else:
                player1_score += 1
            ball_instance = ball.Ball()
            ball_instance.start()
        else:
            # Calculate the distance between the center of the ball
            # and the center of the paddle
            # Collision with paddles
            if (
                ball_instance.x + ball_instance.radius > player1.x
                and ball_instance.x - ball_instance.radius < player1.x + PADDLE_WIDTH
                and ball_instance.y + ball_instance.radius > player1.y
                and ball_instance.y - ball_instance.radius < player1.y + PADDLE_HEIGHT
            ) or (
                ball_instance.x + ball_instance.radius > player2.x
                and ball_instance.x - ball_instance.radius < player2.x + PADDLE_WIDTH
                and ball_instance.y + ball_instance.radius > player2.y
                and ball_instance.y - ball_instance.radius < player2.y + PADDLE_HEIGHT
            ):
                ball_instance.speed_x *= -1

        # Drawing
        screen.fill(BLACK)
        player1.draw(screen)
        player2.draw(screen)
        ball_instance.draw(screen)

        # Draw scores
        text = font.render(f"{player1_score} - {player2_score}", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, 30))
        screen.blit(text, text_rect)

        # Update display
        pygame.display.flip()

        # Control frame rate
        pygame.time.Clock().tick(60)

    if winner:
        screen.fill(BLACK)
        font = pygame.font.Font(None, 72)
        text = font.render(f"Player {winner} wins!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
