import pygame
import sys

pygame.init()

screen = pygame.display.set_mode( (400, 300) )
pygame.display.set_caption("snake")
clock = pygame.time.Clock()

while True:
    clock.tick(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
    screen.fill( (0, 255, 0) )
    pygame.display.update()