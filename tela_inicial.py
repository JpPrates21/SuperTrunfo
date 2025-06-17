import pygame
import sys
from regras import mostrar_tela_regras

def mostrar_tela_inicial(tela):
    # Inicializa o mixer para sons
    pygame.mixer.init()
    som_clique = pygame.mixer.Sound("audios/SomClick.wav")
    som_clique.set_volume(0.4)

    # Carregar a imagem do céu para o fundo animado (deve ser larga)
    ceu = pygame.image.load("imagens/tela_inicial.png").convert()

    # Criar botões
    botao_iniciar = pygame.Rect(540, 400, 200, 60)
    botao_regras = pygame.Rect(540, 500, 200, 60)

    fonte = pygame.font.Font("fontes/Pixelon.otf", 40)
    texto_iniciar = fonte.render("INICIAR", True, (255, 255, 255))
    texto_regras = fonte.render("REGRAS", True, (255, 255, 255))

    # Fonte grande para o título
    fonte_titulo = pygame.font.Font("fontes/Pixelscapes.ttf", 80)
    texto_titulo = fonte_titulo.render("SUPERTRUNFO", True, (255, 255, 255))

    # Variáveis para controle do fundo animado
    x1 = 0
    x2 = ceu.get_width()
    velocidade = 2 # Ajuste a velocidade do movimento do céu

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_regras.collidepoint(evento.pos):
                    som_clique.play()
                    mostrar_tela_regras(tela)
                elif botao_iniciar.collidepoint(evento.pos):
                    som_clique.play()
                    print("Aqui você pode chamar a tela de dificuldade")

        # Movimento do fundo animado
        x1 -= velocidade
        x2 -= velocidade

        # Reinicia posição quando sai da tela para o efeito loop
        if x1 <= -ceu.get_width():
            x1 = x2 + ceu.get_width()
        if x2 <= -ceu.get_width():
            x2 = x1 + ceu.get_width()

        # Desenha o fundo animado
        tela.blit(ceu, (x1, 0))
        tela.blit(ceu, (x2, 0))

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

        pygame.display.update()
        clock.tick(60)  # FPS
