import pygame
import sys

def mostrar_tela_regras(tela):
    # Cores
    BRANCO = (255, 255, 255)
    AZUL = (0, 100, 255)
    AZUL_CLARO = (100, 180, 255)
    AZUL_ESCURO = (0, 0, 128)

    # Carregar fundo 
    background = pygame.image.load("SuperTrunfo/imagens/tela_inicial.png").convert()

    # Fontes personalizadas
    fonte_titulo = pygame.font.Font("SuperTrunfo/fontes/Pixelscapes.ttf", 80)
    fonte_texto = pygame.font.Font("SuperTrunfo/fontes/Pixelon.otf", 32)

    # Texto do título
    texto_titulo = fonte_titulo.render("REGRAS DO JOGO", True, BRANCO)

    # Texto das regras
    regras = [
        "1. Cada jogador recebe cartas com atributos.",
        "2. Um jogador escolhe um atributo para competir.",
        "3. A carta com o maior valor vence a rodada.",
        "4. O jogo continua até que um jogador fique com todas as cartas.",
        "",
        "Clique em VOLTAR para retornar ao menu."
    ]

    # Botão voltar
    botao_voltar = pygame.Rect(540, 600, 200, 50)

    while True:
        tela.blit(background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Desenhar título
        tela.blit(texto_titulo, (tela.get_width() // 2 - texto_titulo.get_width() // 2, 50))

        # Desenhar regras
        for i, linha in enumerate(regras):
            texto = fonte_texto.render(linha, True, BRANCO)
            tela.blit(texto, (100, 200 + i * 40))

        # Desenhar botão com hover
        cor_botao = AZUL_CLARO if botao_voltar.collidepoint(mouse_pos) else AZUL_ESCURO
        pygame.draw.rect(tela, cor_botao, botao_voltar)
        texto_botao = fonte_texto.render("VOLTAR", True, BRANCO)
        tela.blit(texto_botao, (botao_voltar.x + 43, botao_voltar.y + 10))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_voltar.collidepoint(evento.pos):
                    return  # Volta para a tela inicial

        pygame.display.update()
