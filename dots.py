import mss
import os
import pygame
import time
import random
import pygame
import random
from ss import  screenshot

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

son_degisim_zamanı = 0
koordinatlar = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    simdiki_zaman = pygame.time.get_ticks()

    if simdiki_zaman - son_degisim_zamanı > 2000:
        koordinatlar = [
            (random.randint(0, 1280), random.randint(0, 720)), 
            (random.randint(0, 1280), random.randint(0, 720)),
            (random.randint(0, 1280), random.randint(0, 720)) 
        ]
        son_degisim_zamanı = simdiki_zaman


    screen.fill((0, 0, 0))


    if koordinatlar:
        pygame.draw.circle(screen, (255, 0, 0), koordinatlar[0], 25)
        pygame.draw.circle(screen, (0, 255, 0), koordinatlar[1], 25)
        pygame.draw.circle(screen, (0, 0, 255), koordinatlar[2], 25)


    pygame.display.flip()
    screenshot()
    clock.tick(60)

pygame.quit()
