import pygame

pygame.init()

screen = pygame.display.set_mode( (640, 480) )

clock = pygame.time.Clock()

while True:

    clock.tick(1)

    for event in pygame.event.get():
        pass

    screen.fill( (0, 255, 0) )

    pygame.display.update()