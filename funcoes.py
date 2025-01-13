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
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid


# Adicionar um número aleatório (2 ou 4) em uma célula vazia
def add_random_tile(grid):
    empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if grid[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        grid[r][c] = 2 if random.random() < 0.9 else 4

# Renderizar a grade
def draw_grid(grid):
    screen.fill(BACKGROUND_COLOR)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            value = grid[r][c]
            color = TILE_COLORS.get(value, (205, 193, 180))
            pygame.draw.rect(screen, color, (c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if value != 0:
                text = font.render(str(value), True, (119, 110, 101))
                text_rect = text.get_rect(center=(c * TILE_SIZE + TILE_SIZE // 2, r * TILE_SIZE + TILE_SIZE // 2))
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
