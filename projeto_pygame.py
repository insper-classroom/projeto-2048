import pygame
from funcoes import * 


# Função principal do jogo
def main():
    # Chama a função que inicializa a grade 4x4 com blocos iniciais
    grid = initialize_grid()
    # Define a variável de controle do loop principal do jogo
    running = True

    # Loop principal do jogo
    while running:
        # Itera sobre todos os eventos que ocorrem no jogo (como teclas pressionadas ou o fechamento da janela)
        for event in pygame.event.get():
            # Verifica se o evento é fechar a janela do jogo
            if event.type == pygame.QUIT:
                # Interrompe o loop principal, fechando o jogo
                running = False
            # Verifica se alguma tecla foi pressionada
            elif event.type == pygame.KEYDOWN:
                # Chama a função para capturar as entradas do teclado e processar os movimentos da grade
                handle_input(grid, event)
        
        # Renderiza a grade atualizada na tela
        draw_grid(grid)
        # Atualiza a tela para exibir as mudanças
        pygame.display.flip()
        # Controla a velocidade do loop para rodar a 30 quadros por segundo
        clock.tick(30)
    
    # Encerra o Pygame ao sair do loop
    pygame.quit()

if __name__ == "__main__":
    # Chama a função principal do jogo
    main()
