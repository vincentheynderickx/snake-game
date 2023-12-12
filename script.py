import pygame

def init_board():
    pygame.init()
    pygame.display.set_caption("snake")
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
init_board()

class Snake:
    def __init__(self):
        self.position = [[5,10],[6,10],[7,10]]
        self.display()
    def display(self):
        for square in self.position:
            pygame.draw.rect(screen, 'green', pygame.Rect(20*square[0], 20*square[1], 20, 20))

snake = Snake()

while True:
    clock.tick(1)
    if position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
            if event.key==pygame.
    pygame.display.update()

def is_movement_possible(direction, position):
    if (position[0][0]==0) and (direction==[-1,0]):
        return(False)
    if (position[0][0]==19) and (direction==[1,0]):
        return(False)
    if (position[0][1]==0) and (direction==[0,1]):
        return(False)
    if (position[0][1]==14) and (direction==[0,-1]):
        return(False)
    return(True)

def move(direction, position):
    longueur_snake=len(position)
    if not(is_movement_possible):
        pygame.quit()
    for k in range (1,longueur_snake):
        position[longueur_snake-k]=position[longueur_snake-k-1]
    position[0][0]+=direction[0]
    position[0][1]+=direction[1]


    
