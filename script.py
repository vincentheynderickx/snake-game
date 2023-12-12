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
        self.direction = [-1,0]
        self.display()
    def display(self):
        init_board()
        for square in self.position:
            pygame.draw.rect(screen, 'green', pygame.Rect(20*square[0], 20*square[1], 20, 20))
    def is_movement_possible(self):
        if (self.position[0][0]==0) and (self.direction==[-1,0]):
            return(False)
        if (self.position[0][0]==19) and (self.direction==[1,0]):
            return(False)
        if (self.position[0][1]==0) and (self.direction==[0,1]):
            return(False)
        if (self.position[0][1]==14) and (self.direction==[0,-1]):
            return(False)
        return(True)
    def move(self):
        longueur_snake=len(self.position)
        if not(self.is_movement_possible):
            pygame.quit()
        for k in range (1,longueur_snake):
            self.position[longueur_snake-k]=self.position[longueur_snake-k-1]
        self.position[0][0]+=self.direction[0]
        self.position[0][1]+=self.direction[1]

class Fruit:
    def __init__(self, snake):
        squares_available = [[i,j] for i in range(20) for j in range(15) if [i,j] not in snake.position]
        self.position = squares_available[rd.randint(0,len(squares_available))]
        self.display()
    def display(self):
        pygame.draw.rect(screen, 'red', pygame.Rect(20*self.position[0], 20*self.position[1], 20, 20))
    def is_eaten(self):


snake = Snake()
fruit = Fruit(snake)

while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    pygame.display.update()