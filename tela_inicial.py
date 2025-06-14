import pygame
import sys
from regras import mostrar_tela_regras

def mostrar_tela_inicial(tela):
    # Carregar a imagem de fundo (sem redimensionar)
    background = pygame.image.load("SuperTrunfo/imagens/tela_inicial.png").convert()

    # Criar botões
    botao_iniciar = pygame.Rect(540, 400, 200, 60)
    botao_regras = pygame.Rect(540, 500, 200, 60)

    fonte = pygame.font.Font("SuperTrunfo/fontes/Pixelon.otf", 40)
    texto_iniciar = fonte.render("INICIAR", True, (255, 255, 255))
    texto_regras = fonte.render("REGRAS", True, (255, 255, 255))

    # Fonte grande para o título
    fonte_titulo = pygame.font.Font("SuperTrunfo/fontes/Pixelscapes.ttf", 80)
    texto_titulo = fonte_titulo.render("SUPERTRUNFO", True, (255, 255, 255))

    while True:
        tela.blit(background, (0, 0))  # Desenha o fundo
        
        # Centraliza o texto no topo da tela
        tela.blit(texto_titulo, (tela.get_width() // 2 - texto_titulo.get_width() // 2, 50))

        mouse_pos = pygame.mouse.get_pos()

        # Define cores para botões com hover
        cor_botao_iniciar = (0, 0, 255) if not botao_iniciar.collidepoint(mouse_pos) else (0, 100, 255)
        cor_botao_regras = (0, 0, 128) if not botao_regras.collidepoint(mouse_pos) else (0, 50, 180)

        # Desenha botões com cores que mudam no hover
        pygame.draw.rect(tela, cor_botao_iniciar, botao_iniciar)
        pygame.draw.rect(tela, cor_botao_regras, botao_regras)

        # Desenha textos centralizados nos botões
        tela.blit(texto_iniciar, (botao_iniciar.centerx - texto_iniciar.get_width() // 2,
                                  botao_iniciar.centery - texto_iniciar.get_height() // 2))
        tela.blit(texto_regras, (botao_regras.centerx - texto_regras.get_width() // 2,
                                 botao_regras.centery - texto_regras.get_height() // 2))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_regras.collidepoint(evento.pos):
                    mostrar_tela_regras(tela)
                elif botao_iniciar.collidepoint(evento.pos):
                    print("Aqui você pode chamar a tela de dificuldade")

        pygame.display.update()