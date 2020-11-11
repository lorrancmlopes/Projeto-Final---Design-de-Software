import pygame
import random
import time

pygame.init()

#gera tela
WIDTH = 956
HEIGHT = 510
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lord's Element")
image = pygame.image.load('fundo1.png').convert()
image = pygame.transform.scale(image, (956, 510))


game = True

while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

