# Disciplina: Design de Software
# Dupla: Lidia Alves e Lorran Lopes


import pygame
import pygame.sysfont
import random
import time
from os import path

pygame.init()
pygame.mixer.init()

img_dir = path.join(path.dirname(__file__), 'img')

#gera tela
LARGURA = 956
ALTURA = 510
TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
PLAYER_LARGURA = TILE_SIZE
PLAYER_ALTURA = int(TILE_SIZE * 1.5)
PONTO_LARGURA = 80
PONTO_ALTURA = 80
ATAQUE_LARGURA = 40
ATAQUE_ALTURA = 40
GRAVIDADE = 4
FPS = 60

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Lord's Element")

PLAYER_IMG = 'player_img'
BGINSTRUCOES = 'telainstrucoes'
BGGANHADOR = 'telaganhador'
BACKGROUND = 'background_air'
BACKGROUND2 = 'background_fire'
BACKGROUND3 = 'fundoagua'
BACKGROUND4 = 'fundoterra'
ENEMY = 'enemy_img'
ENEMY2 = 'enemy2_img'
ENEMY3 = 'enemy3_img'
ENEMY4 = 'enemy4_img'
PONTOS1 = 'pontos_img'
INICIAL = 'inicio_img'
PONTOS2 = 'fire_img'
PONTOS3 = 'water_img'
PONTOS4 = 'earth_img'
ATAQUE1 = 'ataque1_img'
GAMEOVER = 'avatar_elementos'

JUMP_SIZE = TILE_SIZE
SPEED_X = 5

BLOCK = 0
PLATF = 1
EMPTY = -1
MAP1 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, PLATF, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PLATF, PLATF, PLATF, PLATF],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
]
BLOCK2 = 21
PLATF2 = 22
EMPTY = -1

MAP2 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, PLATF2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK2, BLOCK2, BLOCK2, BLOCK2, EMPTY, EMPTY, EMPTY, BLOCK2, BLOCK2,BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK2, BLOCK2, BLOCK2,BLOCK2, BLOCK2, BLOCK2],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, PLATF2, PLATF2, PLATF2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2],    
    [BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2, BLOCK2],
]
BLOCK3 = 12
PLATF3 = 13
EMPTY = -1

MAP3 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY, EMPTY, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3],    
    [BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3, BLOCK3],
]
BLOCK4 = 18
PLATF4 = 19
EMPTY = -1

MAP4 = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4,BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4],    
    [BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4, BLOCK4],
]
STILL = 0
JUMPING = 1
FALLING = 2

class Tile(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row

class Player(pygame.sprite.Sprite): #classe do jogador, Aang

    def __init__(self, player_img, row, column, platforms, blocks, all_ataque, ataque_img, pew_sound):

        pygame.sprite.Sprite.__init__(self)
        self.state = STILL
        player_img = pygame.transform.scale(player_img, (PLAYER_LARGURA, PLAYER_ALTURA))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.all_ataque = all_ataque
        self.ataque_img = ataque_img
        self.platforms = platforms
        self.blocks = blocks
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE
        self.speedx = 0
        self.speedy = 0
        self.highest_y = self.rect.bottom
        self.health = 3
        self.pontos = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 1000
        self.contato = False
        self.contato_ponto = False
        self.last_update_ponto = pygame.time.get_ticks()
        self.direcao = 1
        self.row = row
        self.column = column
        self.pew_sound = pew_sound #som de tiro
    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        elapsed_ticks_ponto = now - self.last_update_ponto
        if elapsed_ticks > self.frame_ticks:
            self.contato = False
            self.last_update = now

        if elapsed_ticks_ponto > self.frame_ticks:
            self.contato_ponto = False
            self.last_update_ponto = now
        self.speedy += GRAVIDADE
        if self.speedy > 0:
            self.state = FALLING
        self.rect.y += self.speedy
        if self.state != FALLING:
            self.highest_y = self.rect.bottom

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = STILL
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                self.speedy = 0
                self.state = STILL

        if self.speedy > 0:  # Está indo para baixo
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            for platform in collisions:
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    self.highest_y = self.rect.bottom
                    self.speedy = 0
                    self.state = STILL

        self.rect.x += self.speedx
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= LARGURA:
            self.rect.right = LARGURA - 1

        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

    def jump(self):
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING
    def shoot(self):
        new_ataque = Ataque(self.ataque_img, self.rect.centerx, self.rect.bottom, self.direcao)
        self.all_ataque.add(new_ataque)
        self.pew_sound.play()
        
        # ataques_lista = []
        # ataques_lista.append(new_ataque)

class Ataque(pygame.sprite.Sprite):
    def __init__(self, img, centerx, bottom, direcao):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.transform.scale(img, (ATAQUE_LARGURA, ATAQUE_ALTURA))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.speedx = 10*direcao 
        self.rect.bottom = bottom

    def update(self):
        self.rect.x += self.speedx

        if self.rect.right < 0 or self.rect.left < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,enemy_img):
        pygame.sprite.Sprite.__init__(self)
        enemy_img = pygame.transform.scale(enemy_img, (PLAYER_LARGURA, PLAYER_ALTURA))
        self.image = enemy_img
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0
        self.health = 3
        self.contato_ataque = False

    def move(self):
        distance = 80
        speed = 1
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
        self.counter += 1

class Point(pygame.sprite.Sprite):
    def __init__(self,x,y,pontos_img):
        pygame.sprite.Sprite.__init__(self)
        pontos_img = pygame.transform.scale(pontos_img,((PONTO_LARGURA), (PONTO_ALTURA)))
        self.image = pontos_img
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def load_assets(img_dir):
    assets = {}
    assets[PONTOS1] = pygame.image.load(path.join(img_dir, 'pontos.png')).convert_alpha()
    point2 = pygame.image.load(path.join(img_dir, 'fire.png')).convert_alpha()
    points3 = pygame.image.load(path.join(img_dir, 'pontos3.png')).convert_alpha()
    points4 = pygame.image.load(path.join(img_dir, 'ponto4.png')).convert_alpha()
    assets[PONTOS2] = pygame.transform.scale(point2, (PONTO_LARGURA, PONTO_ALTURA))
    assets[PONTOS3] = pygame.transform.scale(points3, (PONTO_LARGURA, PONTO_ALTURA))
    assets[PONTOS4] = pygame.transform.scale(points4, (PONTO_LARGURA, PONTO_ALTURA))
    assets[ENEMY] =  pygame.image.load(path.join(img_dir, 'enemy.png')).convert_alpha()
    assets[ENEMY2] =  pygame.image.load(path.join(img_dir, 'inimigo2.png')).convert_alpha()
    assets[ENEMY3] =  pygame.image.load(path.join(img_dir, 'enemy3.png')).convert_alpha()
    assets[ENEMY4] =  pygame.image.load(path.join(img_dir, 'inimigo4.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'player.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'bloco.png')).convert_alpha()
    assets[BLOCK2] = pygame.image.load(path.join(img_dir, 'bloco2.png')).convert_alpha()
    assets[BLOCK3] = pygame.image.load(path.join(img_dir, 'bloco3.png')).convert_alpha()
    assets[BLOCK4] = pygame.image.load(path.join(img_dir, 'bloco4.jpeg')).convert_alpha()
    assets[PLATF] = pygame.image.load(path.join(img_dir, 'arzinho.png')).convert()
    assets[PLATF2] = pygame.image.load(path.join(img_dir, 'foguinho.png')).convert()
    bg = pygame.image.load(path.join(img_dir, 'background AR.jpg')).convert()
    bg2 = pygame.image.load(path.join(img_dir, 'background FOGO.jpg')).convert()
    bg3 = pygame.image.load(path.join(img_dir, 'fundoagua.png')).convert()
    bg4 = pygame.image.load(path.join(img_dir, 'background4.jpg')).convert()
    bginstrucoes = pygame.image.load(path.join(img_dir, 'telainstrucoes.png')).convert()
    bgganhou = pygame.image.load(path.join(img_dir, 'telaganhador.png')).convert()
    assets[BACKGROUND] = pygame.transform.scale(bg, (LARGURA, ALTURA))
    assets[BACKGROUND2] = pygame.transform.scale(bg2, (LARGURA, ALTURA))
    assets[BACKGROUND3] = pygame.transform.scale(bg3, (LARGURA, ALTURA))
    assets[BACKGROUND4] = pygame.transform.scale(bg4, (LARGURA, ALTURA))
    assets[BGINSTRUCOES] = pygame.transform.scale(bginstrucoes, (LARGURA, ALTURA))
    assets[BGGANHADOR] = pygame.transform.scale(bgganhou, (LARGURA, ALTURA))
    assets["score_font"] = pygame.font.Font('font/PressStart2P.ttf', 28)
    inicial = pygame.image.load(path.join(img_dir, 'inicio.png')).convert()
    assets[INICIAL] = pygame.transform.scale(inicial, (LARGURA, ALTURA))
    gameover = pygame.image.load(path.join(img_dir, 'avatar elementos.jpg')).convert()
    assets[GAMEOVER] = pygame.transform.scale(gameover, (LARGURA, ALTURA))
    assets[ATAQUE1] = pygame.image.load(path.join(img_dir, 'ataque1.png')).convert_alpha()
    return assets
# Carrega os sons do jogo
pygame.mixer.music.load('snd/game_on.mp3')
pygame.mixer.music.set_volume(0.4)
pew_sound = pygame.mixer.Sound('snd/pew.wav')
pegou_sound = pygame.mixer.Sound('snd/pegou.wav')
encostou1 = pygame.mixer.Sound('snd/enemyy.wav')
kill1 = pygame.mixer.Sound('snd/kill.wav')

def DesenhaVidaEPontos(player, assets):
    # Desenhando as vidas
    textSurface = assets['score_font'].render(chr(9829) * player.health, True, (255, 0, 0))
    textRect = textSurface.get_rect()
    textRect.bottomleft = (10, ALTURA - 1)
    window.blit(textSurface, textRect)

    #Desenhando os pontos
    textSurface = assets['score_font'].render("{:08d}".format(player.pontos), True, (255, 255, 0))
    textRect = textSurface.get_rect()
    textRect.midtop = (LARGURA / 2,  10)
    window.blit(textSurface, textRect)

    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()
                
def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    all_ataque = pygame.sprite.Group()
    assets = load_assets(img_dir)

    all_sprites = pygame.sprite.Group()
    platforms = pygame.sprite.Group()
    blocks = pygame.sprite.Group()

    inimigo_list = pygame.sprite.Group()     #grupos de inimigos e pontos coletáveis
    pontos_list = pygame.sprite.Group()
    inimigo2_list = pygame.sprite.Group()
    pontos2_list = pygame.sprite.Group()
    inimigo3_list = pygame.sprite.Group()
    pontos3_list = pygame.sprite.Group()
    inimigo4_list = pygame.sprite.Group()
    pontos4_list = pygame.sprite.Group()

    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks, all_ataque, assets[ATAQUE1], pew_sound)

    inimigo = []
    inimigo2 = []
    inimigo3 = []
    inimigo4 = []
    inimigo_posicoes_x = [300, 700, 400, 120, 800, 90]
    inimigo_posicoes_y = [420, 300, 100, 180, 28, 30]

    inimigo2_posicoes_x = [300, 700, 800, 400, 800, 250]
    inimigo2_posicoes_y = [420, 300, 180, 180, 420, 60]

    inimigo3_posicoes_x = [300, 800, 600, 160, 800, 250]
    inimigo3_posicoes_y = [420, 300, 60, 180, 420, 60]
    
    inimigo4_posicoes_x = [400, 800, 700, 200, 800, 350]
    inimigo4_posicoes_y = [420, 300, 180, 180, 420, 60]
    i = 0
    while i < len(inimigo_posicoes_x):
        inimigo.append(Enemy(inimigo_posicoes_x[i], inimigo_posicoes_y[i], assets[ENEMY]))
        inimigo2.append(Enemy(inimigo2_posicoes_x[i], inimigo2_posicoes_y[i], assets[ENEMY2]))
        inimigo3.append(Enemy(inimigo3_posicoes_x[i], inimigo3_posicoes_y[i], assets[ENEMY3]))
        inimigo4.append(Enemy(inimigo4_posicoes_x[i], inimigo4_posicoes_y[i], assets[ENEMY4]))
        i += 1

    
    #criando os pontos
    points = []
    points2 = []
    points3 = []
    points4 = []

    pontos_posicoes_x = [400, 150, 800, 600, 90, 900, 150]
    pontos_posicoes_y = [420, 300, 300, 100, 180, 20, 30]

    pontos2_posicoes_x = [300, 800, 600, 800, 100, 180, 500]
    pontos2_posicoes_y = [420, 420, 300, 180, 180, 60, 180]

    pontos3_posicoes_x = [300, 800, 50, 900, 90, 150, 500]
    pontos3_posicoes_y = [420, 420, 300, 300, 180, 60, 180]

    pontos4_posicoes_x = [50, 300, 100, 750, 500, 900, 300]
    pontos4_posicoes_y = [250, 420, 40, 60, 180, 300, 60]

    N = 0
    while N < len(pontos_posicoes_x):
        points.append(Point(pontos_posicoes_x[N], pontos_posicoes_y[N], assets[PONTOS1]))
        points2.append(Point(pontos2_posicoes_x[N], pontos2_posicoes_y[N], assets[PONTOS2]))
        points3.append(Point(pontos3_posicoes_x[N], pontos3_posicoes_y[N], assets[PONTOS3]))
        points4.append(Point(pontos4_posicoes_x[N], pontos4_posicoes_y[N], assets[PONTOS4]))
        N += 1
    # Adiciona o jogador e inimigo no grupo de sprites por último para ser desenhado por cima das plataformas
    all_sprites.add(player)


    w = 0
    while w < len(inimigo):
        inimigo_list.add(inimigo[w])
        inimigo2_list.add(inimigo2[w])
        inimigo3_list.add(inimigo3[w])
        inimigo4_list.add(inimigo4[w])
        w += 1

    B = 0
    while B < len(points):
        pontos_list.add(points[B])
        pontos2_list.add(points2[B])
        pontos3_list.add(points3[B])
        pontos4_list.add(points4[B])
        B += 1

    Mapa1_criado = False #Variáveis auxiliares
    Mapa2_criado = False
    Mapa3_criado = False
    Mapa4_criado = False
    
    INICIO = 0
    TELAINSTRUCOES = 1
    TELA1 = 2
    TELA2 = 3
    TELA3 = 4
    TELA4 = 5
    TELAFINAL = 6
    TELAGANHADOR = 7  
    DONE = 8
    RESTART = 9
    state = INICIO
    
    pygame.mixer.music.play(loops=-1)
    
   
    while state != DONE:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        font = pygame.font.SysFont('Algerian', 80)
        text = font.render("Lord's Element", True, (0, 0, 0))
        font2 = pygame.font.SysFont('Cooperplate Gothic Bold', 40)
        text2 = font2.render("Pressione qualquer tecla para iniciar o jogo.", False, (255, 255, 255))
        if state == INICIO:
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE

                if event.type == pygame.KEYUP:
                    state = TELAINSTRUCOES

            # A cada loop, redesenha o fundo e os sprites
            window.fill((255, 255, 255))
            window.blit(assets[INICIAL], (0, 0))
            window.blit(text, ((LARGURA/2 - 300), (ALTURA/2 - 50)))
            window.blit(text2, ((LARGURA/2 - 300), (10)))
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
        if state == TELAINSTRUCOES:
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    state = DONE

                if event.type == pygame.KEYUP:
                    state = TELA1

            window.fill((255, 255, 255))
            window.blit(assets[BGINSTRUCOES], (0, 0))
            pygame.display.flip()

        if state == TELA1:
            # Ajusta a velocidade do jogo.
        
            if Mapa1_criado == False:
                for row in range(len(MAP1)):
                    for column in range(len(MAP1[row])):
                        tile_type = MAP1[row][column]
                        if tile_type != EMPTY:
                            tile = Tile(assets[tile_type], row, column)
                            all_sprites.add(tile)
                            if tile_type == BLOCK:
                                blocks.add(tile)
                            elif tile_type == PLATF:
                                platforms.add(tile)
                Mapa1_criado = True                
            clock.tick(FPS)
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= SPEED_X
                        player.direcao = -1
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                        player.direcao = 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    elif event.key == ord('q'):
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X

            for e in inimigo_list:
                e.move()
            
            ataque = pygame.sprite.groupcollide(all_ataque, inimigo_list, True, True)
            if len(ataque)>0:
                kill1.play()

            encontro = pygame.sprite.spritecollide(player, inimigo_list, False)
            if len(encontro) > 0 and player.contato == False:
                player.contato = True
                player.health -= 1
                player.last_update = pygame.time.get_ticks()
                encostou1.play()
            if player.health <= 0:
                state = TELAFINAL
                
            pegou_ponto = pygame.sprite.spritecollide(player, pontos_list, True)
            if len(pegou_ponto) > 0 and player.contato_ponto == False:
                player.contato_ponto = True
                player.pontos += 1
                player.last_update = pygame.time.get_ticks()
                pegou_sound.play()
                if len(pontos_list) == 0:
                    state = TELA2

            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
            all_sprites.update()
            all_ataque.update()

            # A cada loop, redesenha o fundo e os sprites
            window.fill((0, 0, 0))
            window.blit(assets[BACKGROUND], (0, 0))

            all_sprites.draw(window)
            all_ataque.draw(window)
            inimigo_list.draw(window)
            pontos_list.draw(window)

            DesenhaVidaEPontos(player, assets)
            
        if state == TELA2:
            if Mapa2_criado == False:
                player.rect.x = player.column * TILE_SIZE
                player.rect.bottom = player.row * TILE_SIZE
                all_sprites.remove(blocks, platforms)
                blocks.empty()
                platforms.empty() 
                for row in range(len(MAP2)):
                    for column in range(len(MAP2[row])):
                        tile_type = MAP2[row][column]
                        if tile_type != EMPTY:
                            tile = Tile(assets[tile_type], row, column)
                            all_sprites.add(tile)
                            if tile_type == BLOCK2:
                                blocks.add(tile)
                            elif tile_type == PLATF2:
                                platforms.add(tile)
                Mapa2_criado = True

            clock.tick(FPS)                    

            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= SPEED_X
                        player.direcao = -1
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                        player.direcao = 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    if event.key == ord('q'):
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X
            
            for e in inimigo2_list:
                e.move()

            ataque = pygame.sprite.groupcollide(all_ataque, inimigo2_list, True, True)
            if len(ataque)>0:
                kill1.play()

            encontro2 = pygame.sprite.spritecollide(player, inimigo2_list, False)
            if len(encontro2) > 0 and player.contato == False:
                player.contato = True
                player.health -= 1
                player.last_update = pygame.time.get_ticks()
                encostou1.play()
            if player.health <= 0:
                state = TELAFINAL

            pegou_fogo = pygame.sprite.spritecollide(player, pontos2_list, True)
            if len(pegou_fogo) > 0 and player.contato_ponto == False:
                player.contato_ponto = True
                player.pontos += 1
                player.last_update = pygame.time.get_ticks()
                pegou_sound.play()
                if len(pontos2_list) == 0:
                    state = TELA3
            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
            all_sprites.update()
            all_ataque.update()
            
            # A cada loop, redesenha o fundo e os sprites
            window.fill((0, 0, 0))
            window.blit(assets[BACKGROUND2], (0, 0))

            all_sprites.draw(window)
            all_ataque.draw(window)
            inimigo2_list.draw(window)
            pontos2_list.draw(window)

            DesenhaVidaEPontos(player, assets)

        if state == TELA3:
            if Mapa3_criado == False:
                player.rect.x = player.column * TILE_SIZE
                player.rect.bottom = player.row * TILE_SIZE
                all_sprites.remove(blocks, platforms)
                blocks.empty()
                platforms.empty() 
                for row in range(len(MAP3)):
                    for column in range(len(MAP3[row])):
                        tile_type = MAP3[row][column]
                        if tile_type != EMPTY:
                            tile = Tile(assets[tile_type], row, column)
                            all_sprites.add(tile)
                            if tile_type == BLOCK3:
                                blocks.add(tile)
                            elif tile_type == PLATF3:
                                platforms.add(tile)
                Mapa3_criado = True

            clock.tick(FPS)                    

            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= SPEED_X
                        player.direcao = -1
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                        player.direcao = 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    if event.key == ord('q'):
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X

            for e in inimigo3_list:
                e.move()
            ataque = pygame.sprite.groupcollide(all_ataque, inimigo3_list, True, True)
            if len(ataque)>0:
                kill1.play()

            encontro3 = pygame.sprite.spritecollide(player, inimigo3_list, False)
            if len(encontro3) > 0 and player.contato == False:
                player.contato = True
                player.health -= 1
                player.last_update = pygame.time.get_ticks()
                encostou1.play()
            if player.health <= 0:
                state = TELAFINAL

            pegou_agua = pygame.sprite.spritecollide(player, pontos3_list, True)
            if len(pegou_agua) > 0 and player.contato_ponto == False:
                player.contato_ponto = True
                player.pontos += 1
                player.last_update = pygame.time.get_ticks()
                pegou_sound.play()
                if len(pontos3_list) == 0:
                    state = TELA4
            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
            all_sprites.update()
            all_ataque.update()
            
            # A cada loop, redesenha o fundo e os sprites
            window.fill((0, 0, 0))
            window.blit(assets[BACKGROUND3], (0, 0))

            all_sprites.draw(window)
            all_ataque.draw(window)
            inimigo3_list.draw(window)
            pontos3_list.draw(window)

            DesenhaVidaEPontos(player, assets)

        if state == TELA4:

            if Mapa4_criado == False:
                player.rect.x = player.column * TILE_SIZE
                player.rect.bottom = player.row * TILE_SIZE
                all_sprites.remove(blocks, platforms)
                blocks.empty()
                platforms.empty() 
                for row in range(len(MAP4)):
                    for column in range(len(MAP4[row])):
                        tile_type = MAP4[row][column]
                        if tile_type != EMPTY:
                            tile = Tile(assets[tile_type], row, column)
                            all_sprites.add(tile)
                            if tile_type == BLOCK4:
                                blocks.add(tile)
                            elif tile_type == PLATF4:
                                platforms.add(tile)
                Mapa4_criado = True

            clock.tick(FPS)                    

            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx -= SPEED_X
                        player.direcao = -1
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                        player.direcao = 1
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()
                    if event.key == ord('q'):
                        player.shoot()
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X

            for e in inimigo4_list:
                e.move()

            ataque = pygame.sprite.groupcollide(all_ataque, inimigo4_list, True, True)
            if len(ataque)>0:
                kill1.play()

            encontro4 = pygame.sprite.spritecollide(player, inimigo4_list, False)
            if len(encontro4) > 0 and player.contato == False:
                player.contato = True
                player.health -= 1
                player.last_update = pygame.time.get_ticks()
                encostou1.play()
            if player.health <= 0:
                state = TELAFINAL

            pegou_terra = pygame.sprite.spritecollide(player, pontos4_list, True)
            if len(pegou_terra) > 0 and player.contato_ponto == False:
                player.contato_ponto = True
                player.pontos += 1
                player.last_update = pygame.time.get_ticks()
                pegou_sound.play()
                if len(pontos4_list) == 0:
                    state = TELAGANHADOR
            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
            all_sprites.update()
            all_ataque.update()
            
            # A cada loop, redesenha o fundo e os sprites
            window.fill((0, 0, 0))
            window.blit(assets[BACKGROUND4], (0, 0))

            all_sprites.draw(window)
            all_ataque.draw(window)
            inimigo4_list.draw(window)
            pontos4_list.draw(window)

            DesenhaVidaEPontos(player, assets)

        if state == TELAGANHADOR:
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_ESCAPE:
                        state = DONE
                    if event.key == ord('r'): #
                        window.fill((255, 255, 255))
                        return INICIO

            window.fill((255, 255, 255))
            window.blit(assets[BGGANHADOR], (0, 0))
            pygame.display.flip()


        if state == TELAFINAL:
            font3 = pygame.font.SysFont('Algerian', 100)
            text3 = font3.render("GAME OVER", False, (255, 255, 255))
            font4 = pygame.font.SysFont('Cooperplate Gothic Bold', 40)
            text4 = font4.render("Pressione a tecla 'R' para retornar ao inicio do jogo.", False, (255, 255, 255))
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == ord('r'): 
                        window.fill((255, 255, 255))
                        return INICIO
                        
            window.fill((255, 255, 255))
            window.blit(assets[GAMEOVER], (0, 0))
            window.blit(text3, ((LARGURA/2 - 300), (ALTURA/2 - 50)))
            window.blit(text4, ((LARGURA/2 - 350), (ALTURA/2 + 200)))
            pygame.display.flip()
INICIO = 0
TELAINSTRUCOES = 1
TELA1 = 2
TELA2 = 3
TELA3 = 4
TELA4 = 5
TELAFINAL = 6
TELAGANHADOR = 7  
DONE = 8
RESTART = 9
state = INICIO
while state != DONE:
    if state == INICIO:
        state = game_screen(window)
        print(f"Reiniciar {state}")
    else:
        state = DONE

# ===== Finalização =====
pygame.quit()




