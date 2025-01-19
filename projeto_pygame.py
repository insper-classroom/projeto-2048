import pygame
from funcoes import * 


def main():
     # Chama a função que inicializa a grade 4x4 com blocos iniciais
    grade = inicializar_grade()
    # Define a variável de controle do loop principal do jogo
    rodando = True

    # Loop principal do jogo
    while rodando:
        # Captura todos os eventos que ocorrem no jogo (como teclas pressionadas ou o fechamento da janela)
        for evento in pygame.event.get():
            # Verifica se o evento é fechar a janela do jogo
            if evento.type == pygame.QUIT:
                # Interrompe o loop principal, fechando o jogo
                rodando = False
            # Verifica se alguma tecla foi pressionada
            elif evento.type == pygame.KEYDOWN:
                # Chama a função para capturar as entradas do teclado 
                capturar_entrada(grade, evento)
        
        # Renderiza a grade atualizada na tela
        desenhar_grade(grade)
        # Atualiza a tela para exibir as mudanças
        pygame.display.flip()
        # Controla a velocidade do loop para rodar a 30 quadros por segundo
        relogio.tick(30)
    
    # Encerra o Pygame ao sair do loop
    pygame.quit()

if __name__ == "__main__":
    main()
