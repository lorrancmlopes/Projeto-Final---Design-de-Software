import pygame
import random
import time

pygame.init()

#gera tela
COMPRIMENTO = 956
ALTURA = 510
AANG_COMPRIMENTO = 135
AANG_ALTURA = 105
GROUND_COMPRIMENTO = 1100
GROUND_ALTURA = 100
GRAVIDADE = 3

window = pygame.display.set_mode((COMPRIMENTO, ALTURA))
pygame.display.set_caption("Lord's Element")
image = pygame.image.load('background air.jpg').convert()
image = pygame.transform.scale(image, (956, 510))
aang = pygame.image.load('player1.png').convert_alpha()
aang = pygame.transform.scale(aang, (AANG_COMPRIMENTO, AANG_ALTURA))
ground = pygame.image.load('ground.png').convert_alpha()
ground = pygame.transform.scale(ground, (GROUND_COMPRIMENTO, GROUND_ALTURA))

# Definindo os novos tipos
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.centerx = xloc
        #self.rect.x = xloc

class Aang(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = COMPRIMENTO / 2
        self.rect.bottom = ALTURA - 1
        self.speedx = 0
        self.vy = 0

    def update(self, plataformas):
        # Atualização da posição do jogador
        self.rect.x += self.speedx
        self.rect.bottom += GRAVIDADE
        self.rect.bottom += self.vy
        # Mantem dentro da tela
        if self.rect.right > COMPRIMENTO:
            self.rect.right = COMPRIMENTO
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > ALTURA - 1:
            self.rect.bottom = ALTURA -1
            self.vy = 0
        

# Criando um grupo
all_sprites = pygame.sprite.Group()
all_plataforms = pygame.sprite.Group()

# Criando o jogador
player = Aang(aang)
all_sprites.add(player)

# Criando a plataforma
plataforma_ground = Platform(456, (ALTURA - 60), ground)
all_plataforms.add(plataforma_ground)

#Loop principal do jogo
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
            if event.key == pygame.K_UP:
                for sprite in all_sprites:
                    sprite.vy -= 4
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 4
            if event.key == pygame.K_RIGHT:
                player.speedx -= 4
            if event.key == pygame.K_UP:
                for sprite in all_sprites:
                    sprite.vy += 4 
            

    # ----- Atualiza estado do jogo
    # Verifica se houve colisão entre personagem e plataforma
    encontro = pygame.sprite.groupcollide(all_sprites, all_plataforms, False, False)
    

        
    # Atualizando a posição do player
    all_sprites.update(all_plataforms)

    window.fill((255, 255, 255))  # Preenche com a cor branca
    window.blit(image, (0, 0))

    # Desenhando o jogador
    all_sprites.draw(window)
    # Desenhando a plataforma
    all_plataforms.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

