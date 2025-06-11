import pygame

def mostrar_tela_regras(tela):
    while True:
        # tela.fill()
        # mostrar instruções
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Voltar com ESC
                    return
        pygame.display.update()
