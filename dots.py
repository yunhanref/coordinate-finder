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

# Zamanı takip etmek için bir değişken (milisaniye cinsinden)
son_degisim_zamanı = 0
koordinatlar = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Şu anki zamanı al (milisaniye)
    simdiki_zaman = pygame.time.get_ticks()

    # Eğer son değişim üzerinden 1000 milisaniye (2 saniye) geçtiyse yeni koordinat üret
    if simdiki_zaman - son_degisim_zamanı > 2000:
        koordinatlar = [
            (random.randint(0, 1280), random.randint(0, 720)), # Kırmızı top için
            (random.randint(0, 1280), random.randint(0, 720)), # Yeşil top için
            (random.randint(0, 1280), random.randint(0, 720))  # Mavi top için
        ]
        son_degisim_zamanı = simdiki_zaman # Zamanı güncelle

    # Ekranı temizle (önceki kareyi sil)
    screen.fill((0, 0, 0))

    # Eğer koordinatlar belirlendiyse topları çiz
    if koordinatlar:
        pygame.draw.circle(screen, (255, 0, 0), koordinatlar[0], 25)
        pygame.draw.circle(screen, (0, 255, 0), koordinatlar[1], 25)
        pygame.draw.circle(screen, (0, 0, 255), koordinatlar[2], 25)

    # Ekranı güncelle
    pygame.display.flip()
    screenshot()
    clock.tick(60)

pygame.quit()