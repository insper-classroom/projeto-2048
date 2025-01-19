import random
import pygame


###################################################################################################
######################################### Configurações iniciais ##################################
###################################################################################################

# Define o tamanho da janela do jogo em pixels
TAMANHO_TELA = 400

# Define o tamanho da grade (4x4)
TAMANHO_GRADE = 4

# Calcula o tamanho de cada célula na grade com base no tamanho da janela e da grade
TAMANHO_CELULA = TAMANHO_TELA // TAMANHO_GRADE

# Define a cor de fundo da tela
COR_FUNDO = (187, 173, 160)

# Dicionário que associa valores dos blocos as cores
CORES_BLOCOS = {
    0: (205, 193, 180),   # Cor para blocos vazios (valor 0)
    2: (238, 228, 218),   # Cor para blocos com valor 2
    4: (237, 224, 200),   # Cor para blocos com valor 4
    # Adicionar mais cores para valores maiores, como 8, 16, 32, etc.
}

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo com o tamanho definido
tela = pygame.display.set_mode((TAMANHO_TELA, TAMANHO_TELA))

# Define o título da janela do jogo
pygame.display.set_caption("2048")

# Configura a fonte padrão que será usada para exibir os números nos blocos
fonte = pygame.font.Font(None, 48)  # O valor 48 é o tamanho da fonte

# Cria um relógio do Pygame para controlar a taxa de atualização do jogo
relogio = pygame.time.Clock()

###################################################################################################
####################################### Bloco de funções ##########################################
###################################################################################################

# Mover blocos para cima
def mover_para_cima(grade):
    """
    Move todos os blocos para cima e combina valores iguais.
    """
    # ----Atual---
    # [0][0][0][0]
    # [0][0][2][0]
    # [0][0][2][4]
    # [0][0][0][0]

    # ---Passo 1--   Subir os numeros diferentes de 0 aonde tem 0 acima
    # [0][0][2][4]
    # [0][0][2][0]
    # [0][0][0][0]
    # [0][0][0][0]

    # ---Passo 2--  Combinar os números iguais
    # [0][0][4][4]
    # [0][0][0][0]
    # [0][0][0][0]
    # [0][0][0][0]
 
    n = len(grade)  # Pega o tamanho da grade 
    print("Apertou pra cima, grade recebida: ",grade)
    for coluna in range(n):  # Percorre cada coluna
        # Processa de baixo para cima
        for linha in range(1, n):
            if grade[linha][coluna] != 0:  # Se o bloco atual não for zero 
                linha_atual = linha
                while (linha_atual > 0) and (grade[linha_atual - 1][coluna] == 0):
                    #Move o bloco pra cima enquanto a célula de cima for zero
                    grade[linha_atual - 1][coluna] = grade[linha_atual][coluna]
                    grade[linha_atual][coluna] = 0
                    linha_atual -= 1
                    
                
                if linha_atual > 0 and grade[linha_atual - 1][coluna] == grade[linha_atual][coluna]:
                    # Combina os valores iguais                   
                    grade[linha_atual - 1][coluna] *= 2
                    grade[linha_atual][coluna] = 0
                 
    print("grade devolvida: ",grade)
       
    


# Mover blocos para baixo
def mover_para_baixo(grade):
    """
    Move todos os blocos para baixo e combina valores iguais.
    """
     # ----Atual---
    # [0][0][0][0]
    # [0][0][2][0]
    # [0][0][2][4]
    # [0][0][0][0]

    # ---Passo 1--   Descer os numeros diferentes de 0 aonde tem 0 abaixo
    # [0][0][0][0]
    # [0][0][0][0]
    # [0][0][2][0]
    # [0][0][2][4]

    # ---Passo 2--  Combinar os números iguais
    # [0][0][0][0]
    # [0][0][0][0]
    # [0][0][0][0]
    # [0][0][4][4]
 
 
    print (grade)

# Mover blocos para a esquerda
def mover_para_esquerda(grade):
    """
    Move todos os blocos para a esquerda e combina valores iguais.
    """
    # ----Atual---
    # [0][0][0][0]
    # [0][0][4][0]
    # [0][0][2][2]
    # [0][0][0][0]

    # ---Passo 1--   Mover para a esquerda os numeros diferentes de 0 aonde tem 0 a direita
    # [0][0][0][0]
    # [4][0][0][0]
    # [2][2][0][0]
    # [0][0][0][0]

    # ---Passo 2--  Se tiver, combinar os números iguais
    # [0][0][0][0]
    # [2][0][0][0]
    # [4][0][0][0]
    # [0][0][0][0]


    print (grade)

# Mover blocos para a direita
def mover_para_direita(grade):
    """
    Move todos os blocos para a direita e combina valores iguais.
    """
        # ----Atual---
    # [0][0][0][0]
    # [0][0][4][0]
    # [0][0][2][2]
    # [0][0][0][0]

    # ---Passo 1--   Mover para a direita os numeros diferentes de 0 aonde tem 0 a direita
    # [0][0][0][0]
    # [0][0][0][4]
    # [0][0][2][2]
    # [0][0][0][0]

    # ---Passo 2--  Combinar os números iguais
    # [0][0][0][0]
    # [0][0][0][4]
    # [0][0][0][4]
    # [0][0][0][0]
    print (grade)

# Verificar se ainda existem movimentos disponíveis
def tem_movimentos_disponiveis(grade):
    """
    Retorna True se houver movimentos possíveis, False caso contrário.
    """
    print(grade)

# Calcular a pontuação
def calcular_pontuacao(grade):
    """
    Calcula a pontuação atual baseada nos valores combinados.
    """
    print(grade)

# Exibir mensagem de vitória ou derrota
def exibir_mensagem_final(vitoria):
    """
    Exibe uma mensagem ao jogador indicando vitória ou derrota.
    """
    print("Implementar mensagem de fim de jogo")

# Função para inicializar a grade
def inicializar_grade():
    # Inicializar a grade
    grade = []  # Lista vazia para representar a grade

    # Criar uma grade 4x4 cheia de zeros
    for _ in range(TAMANHO_GRADE):
        linha = [0] * TAMANHO_GRADE  # Cria uma linha com valores 0
        grade.append(linha)         # Adiciona a linha à grade

    adicionar_bloco_aleatorio(grade)  # Adiciona o primeiro bloco aleatório
    adicionar_bloco_aleatorio(grade)  # Adiciona o segundo bloco aleatório
    return grade
    

# Adicionar um número aleatório (2 ou 4) em uma célula vazia
def adicionar_bloco_aleatorio(grade):
    # Lista para armazenar as posições vazias
    celulas_vazias = []

    for x in range(TAMANHO_GRADE):
        for y in range(TAMANHO_GRADE):
            # Se o valor na posição (x, y) for 0 (bloco vazio)
            if grade[x][y] == 0:
                # Adiciona a posição a lista de células vazias
                celulas_vazias.append((x, y))

    # Se existirem células vazias
    if celulas_vazias:
        # Escolhe aleatoriamente uma célula vazia da lista
        x, y = random.choice(celulas_vazias)
        # Define o valor 2 com 80% de chance, ou 4 com 20% de chance
        grade[x][y] = 2 if random.random() < 0.8 else 4

# Renderizar a grade
def desenhar_grade(grade):
    # Preencher o fundo da tela com a cor de fundo
    tela.fill(COR_FUNDO)

    for x in range(TAMANHO_GRADE):  # O x representa a linha
        for y in range(TAMANHO_GRADE):  # O y representa a coluna
            # Obter o valor na posição atual (x, y)
            valor = grade[x][y]
            # Determinar a cor do bloco com base no valor
            cor = CORES_BLOCOS.get(valor, (205, 193, 180))  # Cor padrão se o valor não estiver no dicionário

            # Desenhar o bloco na tela
            pygame.draw.rect(
                tela, 
                cor,  
                (y * TAMANHO_CELULA, x * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)  # Posição e tamanho do bloco
            )

            # Se o bloco não estiver vazio 
            if valor != 0:
                # Renderizar o valor como texto
                texto = fonte.render(str(valor), True, (119, 110, 101))  # Texto na cor cinza escuro

                # Centralizar o texto dentro do bloco
                posicao_texto = texto.get_rect(
                    center=(y * TAMANHO_CELULA + TAMANHO_CELULA // 2, x * TAMANHO_CELULA + TAMANHO_CELULA // 2)
                )

                # Desenhar o texto na tela
                tela.blit(texto, posicao_texto)

# Capturar os eventos do teclado
def capturar_entrada(grade, evento):
    if evento.key == pygame.K_UP:
        print("Apertou tecla para cima")
        mover_para_cima(grade)

    elif evento.key == pygame.K_DOWN:
        print("Apertou tecla para baixo")
        mover_para_baixo(grade)

    elif evento.key == pygame.K_LEFT:
        print("Apertou tecla para esquerda")
        mover_para_esquerda(grade)

    elif evento.key == pygame.K_RIGHT:
        print("Apertou tecla para direita")
        mover_para_direita(grade)

# Verificar se o jogo acabou
def jogo_acabou(grade):
    # Implementar lógica de fim de jogo
    return False
