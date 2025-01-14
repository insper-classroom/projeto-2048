import random
import pygame

###################################################################################################
######################################### Configurações iniciais ##################################
###################################################################################################

# Define o tamanho da janela do jogo em pixels
SCREEN_SIZE = 400

# Define o tamanho da grade (4x4)
GRID_SIZE = 4

# Calcula o tamanho de cada célula na grade com base no tamanho da janela e da grade
TILE_SIZE = SCREEN_SIZE // GRID_SIZE

# Define a cor de fundo da tela 
BACKGROUND_COLOR = (187, 173, 160)

# Dicionário que associa valores dos blocos às suas respectivas cores
TILE_COLORS = {
    0: (205, 193, 180),   # Cor para blocos vazios (valor 0)
    2: (238, 228, 218),   # Cor para blocos com valor 2
    4: (237, 224, 200),   # Cor para blocos com valor 4
    # Adicionar mais cores para valores maiores, como 8, 16, 32, etc.
}

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo com tamanho definido
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

# Define o título da janela do jogo
pygame.display.set_caption("2048")

# Configura a fonte padrão que será usada para exibir os números nos blocos
font = pygame.font.Font(None, 48)  # O valor 48 é o tamanho da fonte

# Cria um relógio do Pygame para controlar a taxa de atualização do jogo
clock = pygame.time.Clock()


###################################################################################################
####################################### bloco de funções ##########################################
###################################################################################################


# Mover blocos para cima
def move_up(grid):
    """
    Move todos os blocos para cima e combina valores iguais.
    """
    return print ("Implementar lógica de movimentação para cima")

# Mover blocos para baixo
def move_down(grid):
    """
    Move todos os blocos para baixo e combina valores iguais.
    """
    return print ("Implementar lógica de movimentação para baixo")

# Mover blocos para a esquerda
def move_left(grid):
    """
    Move todos os blocos para a esquerda e combina valores iguais.
    """
    return print ("Implementar lógica de movimentação para a esquerda")

# Mover blocos para a direita
def move_right(grid):
    """
    Move todos os blocos para a direita e combina valores iguais.
    """
    return print ("Implementar lógica de movimentação para a direita")

# Verificar se ainda existem movimentos disponíveis
def has_moves_available(grid):
    """
    Retorna True se houver movimentos possíveis, False caso contrário.
    """
    return print ("Implementar lógica para verificar movimentos disponíveis")

# Calcular a pontuação
def calculate_score(grid):
    """
    Calcula a pontuação atual baseada nos valores combinados.
    """
    return print ("Implementar cálculo da pontuação")

# Exibir mensagem de vitória ou derrota
def display_end_message(win):
    """
    Exibe uma mensagem ao jogador indicando vitória ou derrota.
    """
    return print ("Implementar mensagem de fim de jogo")


# Função para inicializar a grade
def initialize_grid():
    # Inicializar o grid
    grid = []  # Lista vazia para representar a grade
    
    # Criar uma grade 4x4 cheia de zeros
    for _ in range(GRID_SIZE):  
        row = [0] * GRID_SIZE  # Cria uma linha com valores 0
        grid.append(row)       # Adiciona a linha ao grid
    
    # Adicionar blocos aleatórios no grid
    add_random_tile(grid)  # Adiciona o primeiro bloco aleatório
    add_random_tile(grid)  # Adiciona o segundo bloco aleatório



# Adicionar um número aleatório (2 ou 4) em uma célula vazia
def add_random_tile(grid):
    # Lista para armazenar as posições vazias
    empty_cells = []
    
    # Iterar pelas linhas do grid
    for x in range(GRID_SIZE):
        # Iterar pelas colunas do grid
        for y in range(GRID_SIZE):
            # Se o valor na posição (x, y) for 0 (bloco vazio)
            if grid[x][y] == 0:
                # Adiciona a posição (x, y) à lista de células vazias
                empty_cells.append((x, y))
    
    # Se existirem células vazias
    if empty_cells:
        # Escolhe aleatoriamente uma célula vazia da lista
        x, y = random.choice(empty_cells)
        # Define o valor 2 com 90% de chance, ou 4 com 10% de chance
        grid[x][y] = 2 if random.random() < 0.9 else 4


# Renderizar a grade
def draw_grid(grid):

    # Preencher o fundo da tela com a cor de fundo
    screen.fill(BACKGROUND_COLOR)

    for x in range(GRID_SIZE):  # o x representa a linha
        for y in range(GRID_SIZE):  # o y representa a coluna
            # Obter o valor na posição atual (x, y)
            value = grid[x][y]
            # Determinar a cor do bloco com base no valor
            color = TILE_COLORS.get(value, (205, 193, 180))  # Cor padrão se o valor não estiver no dicionário
            
            # Desenhar o retângulo (bloco) na tela
            pygame.draw.rect(
                screen,  # a parte onde será desenhado
                color,  # cor do retângulo
                (y * TILE_SIZE, x * TILE_SIZE, TILE_SIZE, TILE_SIZE)  # Posição e tamanho do bloco
            )
            
            # Se o bloco não estiver vazio (valor diferente de 0)
            if value != 0:
                # Renderizar o valor como texto
                text = font.render(str(value), True, (119, 110, 101))  # Texto na cor cinza escuro
                
                # Centralizar o texto dentro do bloco
                text_rect = text.get_rect(
                    center=(y * TILE_SIZE + TILE_SIZE // 2, x * TILE_SIZE + TILE_SIZE // 2)
                )
                
                # Desenhar o texto na tela
                screen.blit(text, text_rect)



# capturar os eventos do teclado
def handle_input(grid, event):
    if event.key == pygame.K_UP:
        print("Mover para cima")
    elif event.key == pygame.K_DOWN:
        print("Mover para baixo")
    elif event.key == pygame.K_LEFT:
        print("Mover para a esquerda")
    elif event.key == pygame.K_RIGHT:
        print("Mover para a direita")


# capturar os eventos do teclado
def handle_input(grid, event):
    if event.key == pygame.K_UP:
        print("Apertou tecla para cima")
        move_up(grid)
        
    elif event.key == pygame.K_DOWN:
        print("Apertou tecla para baixo")
        move_down(grid)

    elif event.key == pygame.K_LEFT:
        print("Apertou tecla para esquerda")
        move_left(grid)

    elif event.key == pygame.K_RIGHT:
        print("Apertou tecla para direita")
        move_right(grid)


# Verificar se o jogo acabou
def is_game_over(grid):
    # Implementar lógica de fim de jogo
    return False
