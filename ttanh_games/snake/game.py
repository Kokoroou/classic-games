import pygame

from ttanh_games.snake.constants import (
    BLACK,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    SNAKE_SPEED,
    WHITE,
)
from ttanh_games.snake.food import Food
from ttanh_games.snake.snake import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

        self.running = True

    def run(self):
        self.show_instructions(self.screen)
        self.countdown(self.screen)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.snake.handle_input(event)

            self.update()
            self.draw()

            self.clock.tick(SNAKE_SPEED)

        self.show_game_over_screen(self.screen)
        pygame.quit()

    def update(self):
        self.snake.move()
        if (
            self.snake.body[0][0] == self.food.position[0]
            and self.snake.body[0][1] == self.food.position[1]
        ):
            self.snake.grow()
            self.food.randomize_position(self.snake.body)

        if self.snake.check_collision():
            pygame.time.delay(2000)
            self.running = False

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.update()

    def show_game_over_screen(self, screen):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)

    def show_instructions(self, screen):
        screen.fill(BLACK)
        font = pygame.font.Font(None, 36)
        instructions = [
            "Welcome to Snake Game!",
            "",
            "Use ARROW KEYS to move the snake",
            "",
            "Eat the red food to grow",
            "Avoid hitting the wall or yourself",
            "---Press any key to start---",
        ]
        y = SCREEN_HEIGHT // 4
        for line in instructions:
            text = font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, y))
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

    def countdown(self, screen):
        for i in range(3, 0, -1):
            screen.fill(BLACK)
            font = pygame.font.Font(None, 72)
            text = font.render(str(i), True, WHITE)
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()
            pygame.time.delay(1000)
