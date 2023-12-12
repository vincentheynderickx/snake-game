import pygame

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        pass

    screen.fill( (0, 0, 0) )
    for k in range (16):
        for i in range (12):
            color = (255, 255, 255) 
            left=40*k
            top=40*i
            width=20
            height=20
            rect = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, color, rect)
    pygame.display.update()