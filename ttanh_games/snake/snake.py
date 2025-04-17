import pygame

from ttanh_games.snake.constants import (
    DOWN,
    GREEN,
    GRID_SIZE,
    LEFT,
    RIGHT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    UP,
)


class Snake:
    def __init__(self):
        self.body = [
            ((SCREEN_WIDTH // GRID_SIZE) // 2, (SCREEN_HEIGHT // GRID_SIZE) // 2)
        ]
        self.direction = RIGHT
        self.add_segment = False

    def move(self):
        if self.direction == RIGHT:
            new_head = (self.body[0][0] + 1, self.body[0][1])
        elif self.direction == LEFT:
            new_head = (self.body[0][0] - 1, self.body[0][1])
        elif self.direction == UP:
            new_head = (self.body[0][0], self.body[0][1] - 1)
        elif self.direction == DOWN:
            new_head = (self.body[0][0], self.body[0][1] + 1)

        if self.add_segment:
            self.body.insert(0, new_head)
            self.add_segment = False
        else:
            self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.add_segment = True

    def check_collision(self):
        if not 0 <= self.body[0][0] < (SCREEN_WIDTH // GRID_SIZE) or not 0 <= self.body[
            0
        ][1] < (SCREEN_HEIGHT // GRID_SIZE):
            return True

        if self.body[0] in self.body[1:]:
            return True

        return False

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and self.direction != LEFT:
                self.direction = RIGHT
            elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                self.direction = LEFT
            elif event.key == pygame.K_UP and self.direction != DOWN:
                self.direction = UP
            elif event.key == pygame.K_DOWN and self.direction != UP:
                self.direction = DOWN

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(
                screen,
                GREEN,
                (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
            )
