import pygame
import random
import time

pygame.init()

#gera tela
WIDTH = 1377
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lord's Element")

game = True

while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False



