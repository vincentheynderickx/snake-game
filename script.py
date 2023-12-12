import pygame
import numpy.random as rd

def init_board():
    screen.fill( (0, 0, 0) )
    for k in range (32):
        for i in range (24):
            color = (255, 255, 255) 
            left=40*k
            if (i%2==0):
                left+=20
            top=20*i
            width=20
            height=20
            rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, color, rect)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 300))
pygame.init()
pygame.display.set_caption("snake")
init_board()

class Snake:
    def __init__(self):
        self.position = [[5,10],[6,10],[7,10]]
        self.length = 3
        self.direction = [-1,0]
        self.display()
    def display(self):
        for square in self.position:
            pygame.draw.rect(screen, 'green', pygame.Rect(20*square[0], 20*square[1], 20, 20))
    def is_movement_possible(self):
        if (self.position[0][0]==0) and (self.direction==[-1,0]):
            return(False)
        if (self.position[0][0]==19) and (self.direction==[1,0]):
            return(False)
        if (self.position[0][1]==0) and (self.direction==[0,-1]):
            return(False)
        if (self.position[0][1]==14) and (self.direction==[0,1]):
            return(False)
        return(True)
    def move(self, fruit):
        if self.position[0] == fruit.position:
            new_head = [self.position[0][0] + self.direction[0],self.position[0][1] + self.direction[1]]
            self.position = [new_head] + self.position
            fruit.new_position()
        else:
            new_head = [self.position[0][0] + self.direction[0],self.position[0][1] + self.direction[1]]
            self.position = self.position[:-1]
            self.position = [new_head] + self.position
    def fin_partie(self):
        if not(self.is_movement_possible()):
            return(True)
        if (self.position[0] in self.position[1:]):
            return(True)
        

class Fruit:
    def __init__(self, snake):
        self.new_position()
        self.display()
    def display(self):
        pygame.draw.rect(screen, 'red', pygame.Rect(20*self.position[0], 20*self.position[1], 20, 20))
    def new_position(self):
        squares_available = [[i,j] for i in range(20) for j in range(15) if [i,j] not in snake.position]
        self.position = squares_available[rd.randint(0,len(squares_available))]


snake = Snake()
fruit = Fruit(snake)

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key == (pygame.K_LEFT) and snake.direction!=[1,0]:
                snake.direction=[-1,0]
            if event.key == (pygame.K_RIGHT) and snake.direction!=[-1,0]:
                snake.direction=[1,0]
            if event.key == (pygame.K_UP) and snake.direction!=[0,1]:
                snake.direction=[0,-1]
            if event.key == (pygame.K_DOWN) and snake.direction!=[0,-1]:
                snake.direction=[0,1]
    if snake.fin_partie():
            pygame.quit()
    snake.move(fruit)
    init_board()
    fruit.display()
    snake.display()
    
    pygame.display.update()