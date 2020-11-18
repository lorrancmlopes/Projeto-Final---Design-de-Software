import pygame
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
GRAVIDADE = 4
FPS = 60

window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Lord's Element")

PLAYER_IMG = 'player_img'
BACKGROUND = 'background_air'
ENEMY = 'enemy_img'
PONTOS = 'pontos_img'
INICIAL = 'inicio_img'

JUMP_SIZE = TILE_SIZE
SPEED_X = 5

BLOCK = 0
PLATF = 1
EMPTY = -1

MAP = [
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, PLATF, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
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

# Classe Jogador que representa o herói

inimigo_list = pygame.sprite.Group()
pontos_list = pygame.sprite.Group()

class Player(pygame.sprite.Sprite):

    def __init__(self, player_img, row, column, platforms, blocks):

        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL

        # Ajusta o tamanho da imagem
        player_img = pygame.transform.scale(player_img, (PLAYER_LARGURA, PLAYER_ALTURA))

        # Define a imagem do sprite. Nesse exemplo vamos usar uma imagem estática (não teremos animação durante o pulo)
        self.image = player_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Guarda os grupos de sprites para tratar as colisões
        self.platforms = platforms
        self.blocks = blocks

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = column * TILE_SIZE
        self.rect.bottom = row * TILE_SIZE

        # Inicializa velocidades
        self.speedx = 0
        self.speedy = 0

        # Define altura no mapa
        # Essa variável sempre conterá a maior altura alcançada pelo jogador
        # antes de começar a cair
        self.highest_y = self.rect.bottom
        #vida do jogador
        self.health = 3
        #pontos adquiridos
        self.pontos = 0 
        #tempo
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 1000
        self.contato = False
        self.contato_ponto = False
        self.last_update_ponto = pygame.time.get_ticks()


    # Metodo que atualiza a posição do personagem
    def update(self):
        #verifica tempo do jogo
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update
        elapsed_ticks_ponto = now - self.last_update_ponto
        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.contato = False
            self.last_update = now

        if elapsed_ticks_ponto > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.contato_ponto = False
            self.last_update_ponto = now
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVIDADE
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy

        # Atualiza altura no mapa
        if self.state != FALLING:
            self.highest_y = self.rect.bottom

        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tratamento especial para plataformas
        # Plataformas devem ser transponíveis quando o personagem está pulando
        # mas devem pará-lo quando ele está caindo. Para pará-lo é necessário que
        # o jogador tenha passado daquela altura durante o último pulo.
        if self.speedy > 0:  # Está indo para baixo
            collisions = pygame.sprite.spritecollide(self, self.platforms, False)
            # Para cada tile de plataforma que colidiu com o personagem
            # verifica se ele estava aproximadamente na parte de cima
            for platform in collisions:
                # Verifica se a altura alcançada durante o pulo está acima da
                # plataforma.
                if self.highest_y <= platform.rect.top:
                    self.rect.bottom = platform.rect.top
                    # Atualiza a altura no mapa
                    self.highest_y = self.rect.bottom
                    # Para de cair
                    self.speedy = 0
                    # Atualiza o estado para parado
                    self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= LARGURA:
            self.rect.right = LARGURA - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        # O personagem não colide com as plataformas quando está andando na horizontal
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right
        

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING

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

    def move(self):
        distance = 30
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
    assets[PONTOS] = pygame.image.load(path.join(img_dir, 'pontos.png')).convert_alpha()
    assets[ENEMY] =  pygame.image.load(path.join(img_dir, 'enemy.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.image.load(path.join(img_dir, 'player.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir, 'bloco.png')).convert_alpha()
    assets[PLATF] = pygame.image.load(path.join(img_dir, 'arzinho.png')).convert()
    bg = pygame.image.load(path.join(img_dir, 'background AR.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(bg, (LARGURA, ALTURA))
    assets["score_font"] = pygame.font.Font('font/PressStart2P.ttf', 28)
    inicial = pygame.image.load(path.join(img_dir, 'FUNDOJOGO.jpg')).convert()
    assets[INICIAL] = pygame.transform.scale(inicial, (LARGURA, ALTURA))
    return assets
# Carrega os sons do jogo
pygame.mixer.music.load('snd/game_on.mp3')
pygame.mixer.music.set_volume(0.4)

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de plataforma.
    # Sprites de plataforma são aqueles que permitem que o jogador passe quando
    # estiver pulando, mas pare quando estiver caindo.
    platforms = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador, independente
    # de onde ele está vindo
    blocks = pygame.sprite.Group()

    # Cria Sprite do jogador
    player = Player(assets[PLAYER_IMG], 12, 2, platforms, blocks)

    #criando o inimigo
    inimigo = []
    inimigo_posicoes_x = [300, 700, 400, 120]
    inimigo_posicoes_y = [420, 300, 100, 180]
    i = 0
    while i < len(inimigo_posicoes_x):
        inimigo.append(Enemy(inimigo_posicoes_x[i], inimigo_posicoes_y[i], assets[ENEMY]))
        i += 1

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type != EMPTY:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type == BLOCK:
                    blocks.add(tile)
                elif tile_type == PLATF:
                    platforms.add(tile)
    #criando os pontos de aprendizagem
    points = []
    pontos_posicoes_x = [400, 800, 600, 90, 900]
    pontos_posicoes_y = [420, 300, 100, 180, 20]
    N = 0
    while N < len(pontos_posicoes_x):
        points.append(Point(pontos_posicoes_x[N], pontos_posicoes_y[N], assets[PONTOS]))
        N += 1
    # Adiciona o jogador e inimigo no grupo de sprites por último para ser desenhado por cima das plataformas
    all_sprites.add(player)

    w = 0 
    while w < len(inimigo):
        inimigo_list.add(inimigo[w])
        w += 1
    
    B = 0 
    while B < len(points):
        pontos_list.add(points[B])
        B += 1


    INICIO = 0
    PLAYING = 1
    DONE = 2

    state = INICIO
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        if state == INICIO:
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    state = DONE

                if event.type == pygame.KEYUP:
                    state = PLAYING

            # A cada loop, redesenha o fundo e os sprites
            window.fill((255, 255, 255))
            window.blit(assets[INICIAL], (0, 0))

            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
        if state == PLAYING:
            # Ajusta a velocidade do jogo.
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
                    elif event.key == pygame.K_RIGHT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                        player.jump()

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera o estado do jogador.
                    if event.key == pygame.K_LEFT:
                        player.speedx += SPEED_X
                    elif event.key == pygame.K_RIGHT:
                        player.speedx -= SPEED_X

            for e in inimigo_list:
                    e.move()

            encontro = pygame.sprite.spritecollide(player, inimigo_list, False)
            if len(encontro) > 0 and player.contato == False:
                player.contato = True
                player.health -= 1
                player.last_update = pygame.time.get_ticks()
            if player.health <= 0:
                state = DONE
<<<<<<< HEAD

            pegou_ponto = pygame.sprite.spritecollide(player, pontos_list, True)
            if len(pegou_ponto) > 0 and player.contato == False:
                player.contato = True
                player.pontos += 1
                player.last_update = pygame.time.get_ticks()
            
            # Depois de processar os eventos.
            # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
            all_sprites.update()

            # A cada loop, redesenha o fundo e os sprites
            window.fill((0, 0, 0))
            window.blit(assets[BACKGROUND], (0, 0))

            all_sprites.draw(window)
            inimigo_list.draw(window)
            pontos_list.draw(window)

            # Desenhando as vidas
            text_surface = assets['score_font'].render(chr(9829) * player.health, True, (255, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.bottomleft = (10, ALTURA - 1)
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
=======
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X

        for e in inimigo_list:
                e.move()

        encontro = pygame.sprite.spritecollide(player, inimigo_list, False)
        if len(encontro) > 0 and player.contato == False:
            player.contato = True
            player.health -= 1
            player.last_update = pygame.time.get_ticks()
        if player.health <= 0:
            state = DONE

        pegou_ponto = pygame.sprite.spritecollide(player, pontos_list, True)
        if len(pegou_ponto) > 0 and player.contato_ponto == False:
            player.contato_ponto = True
            player.pontos += 1
            player.last_update_ponto = pygame.time.get_ticks()
            print(player.pontos)
        
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        # A cada loop, redesenha o fundo e os sprites
        window.fill((0, 0, 0))
        window.blit(assets[BACKGROUND], (0, 0))

        all_sprites.draw(window)
        inimigo_list.draw(window)
        pontos_list.draw(window)

        # Desenhando as vidas
        text_surface = assets['score_font'].render(chr(9829) * player.health, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, ALTURA - 1)
        window.blit(text_surface, text_rect)

        #Desenhando os pontos
        text_surface = assets['score_font'].render("{:08d}".format(player.pontos), True, (255, 255, 0))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (LARGURA / 2,  10)
        window.blit(text_surface, text_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
>>>>>>> aff6c7c64ae20a62a3e8d87e817e161a9a032f8a

# Comando para evitar travamentos.
try:
    game_screen(window)
finally:
    pygame.quit()




