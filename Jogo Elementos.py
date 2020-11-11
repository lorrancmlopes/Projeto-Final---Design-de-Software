import pygame
import random
import time

pygame.init()

#gera tela
WIDTH = 956
HEIGHT = 510
AANG_WIDTH = 135
AANG_HEIGHT = 105

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lord's Element")
image = pygame.image.load('fundo1.png').convert()
image = pygame.transform.scale(image, (956, 510))
aang = pygame.image.load('player1.png').convert_alpha()
aang = pygame.transform.scale(aang, (AANG_WIDTH, AANG_HEIGHT))


# Definindo os novos tipos
class Aang(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 1
        self.speedx = 0

    def update(self):
        # Atualização da posição do jogador
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

# Criando um grupo
all_sprites = pygame.sprite.Group()
# Criando o jogador
player = Aang(aang)
all_sprites.add(player)

game = True

while game:
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 4
            if event.key == pygame.K_RIGHT:
                player.speedx += 4
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 4
            if event.key == pygame.K_RIGHT:
                player.speedx -= 4

    # ----- Atualiza estado do jogo
    # Atualizando a posição do player
    all_sprites.update()

    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    # Desenhando o jogador
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

