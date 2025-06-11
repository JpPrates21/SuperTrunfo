import pygame
from tela_jogo import iniciar_jogo

def mostrar_tela_dificuldade(tela):
    while True:
        # desenha botões de dificuldade
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if facil.collidepoint(evento.pos):
                    iniciar_jogo(tela, "Fácil")
                    return
                elif dificil.collidepoint(evento.pos):
                    iniciar_jogo(tela, "Difícil")
                    return
        pygame.display.update()
