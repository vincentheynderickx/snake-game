import pygame
import numpy.random as rd
import numpy as np

print("geleoe")


def init_board():
    screen.fill((100, 100, 200))
    for k in range(20):
        for i in range(20):
            color = (150, 150, 245)
            left = 40 * k
            if i % 2 == 0:
                left += 20
            top = 20 * i
            width = 20
            height = 20
            rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, color, rect)


clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.init()
pygame.display.set_caption("snake")
init_board()


class Snake:
    def __init__(self):
        self.position = [[5, 10], [6, 10], [7, 10]]
        self.position = [[5, 10], [6, 10], [7, 10]]
        self.length = 3
        self.direction = [-1, 0]
        self.newdir = self.direction
        self.speed = 4
        self.score = 0

    def display_snake(self):
        for square in self.position:
            pygame.draw.rect(
                screen, "green", pygame.Rect(20 * square[0], 20 * square[1], 20, 20)
            )

            pygame.draw.rect(
                screen, "green", pygame.Rect(20 * square[0], 20 * square[1], 20, 20)
            )

    def is_movement_possible(self):
        if (self.position[0][0] == 0) and (self.newdir == [-1, 0]):
            return False
        if (self.position[0][0] == 19) and (self.newdir == [1, 0]):
            return False
        if (self.position[0][1] == 0) and (self.newdir == [0, -1]):
            return False
        if (self.position[0][1] == 14) and (self.newdir == [0, 1]):
            return False
        return True

    def move(self, fruit):
        self.direction = self.newdir
        if self.position[0] == fruit.position:
            new_head = [
                self.position[0][0] + self.direction[0],
                self.position[0][1] + self.direction[1],
            ]

            self.position = [new_head] + self.position
            self.score += 1
            self.speed = 10 - 10 * np.exp(-self.score)
            fruit.new_position()
        else:
            new_head = [
                self.position[0][0] + self.direction[0],
                self.position[0][1] + self.direction[1],
            ]
            new_head = [
                self.position[0][0] + self.direction[0],
                self.position[0][1] + self.direction[1],
            ]
            self.position = self.position[:-1]
            self.position = [new_head] + self.position
            self.lastpos = self.position[-1]

    def display_score(self, score):
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

    def is_game_over(self):
        if not (self.is_movement_possible()):
            return True
        if self.position[0] in self.position[1:]:
            return True

        if not (self.is_movement_possible()):
            return True
        if self.position[0] in self.position[1:]:
            return True

    def display_game_over(self):
        screen.fill((0, 0, 0))
        screen.fill((0, 0, 0))
        end_font = pygame.font.Font(None, 36)
        end_text = end_font.render(
            f"Game Over! Your Score: {self.score}", True, (255, 255, 255)
        )
        end_text_rect = end_text.get_rect(
            center=(screen.get_width() // 2, screen.get_height() // 2)
        )
        screen.blit(end_text, end_text_rect)
        pygame.display.flip()


class Fruit:
    def __init__(self, snake):
        self.new_position()
        self.display_fruit()

    def display_fruit(self):
        pygame.draw.rect(
            screen,
            "red",
            pygame.Rect(20 * self.position[0], 20 * self.position[1], 20, 20),
        )

        pygame.draw.rect(
            screen,
            "red",
            pygame.Rect(20 * self.position[0], 20 * self.position[1], 20, 20),
        )

    def new_position(self):
        squares_available = [
            [i, j] for i in range(20) for j in range(15) if [i, j] not in snake.position
        ]
        self.position = squares_available[rd.randint(0, len(squares_available))]
        squares_available = [
            [i, j] for i in range(20) for j in range(15) if [i, j] not in snake.position
        ]
        self.position = squares_available[rd.randint(0, len(squares_available))]


snake = Snake()
fruit = Fruit(snake)
font = pygame.font.Font(None, 36)
game_over = False
game_over = False

while True:
    # speed = 4 + 2 * (score // 10)
    clock.tick(snake.speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == (pygame.K_LEFT) and snake.direction != [1, 0]:
                snake.newdir = [-1, 0]
            if event.key == (pygame.K_RIGHT) and snake.direction != [-1, 0]:
                snake.newdir = [1, 0]
            if event.key == (pygame.K_UP) and snake.direction != [0, 1]:
                snake.newdir = [0, -1]
            if event.key == (pygame.K_DOWN) and snake.direction != [0, -1]:
                snake.newdir = [0, 1]
    if snake.is_game_over():
        snake.display_game_over()
        pygame.time.wait(3000)
        pygame.time.wait(3000)
        break
    snake.move(fruit)

    init_board()
    fruit.display_fruit()
    snake.display_snake()
    snake.display_score(snake.score)
    pygame.display.update()
