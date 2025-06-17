import pygame
import sys

def mostrar_tela_dificuldade(tela):
    # Som de clique
    pygame.mixer.init()
    som_clique = pygame.mixer.Sound("audios/SomClick.wav")
    som_clique.set_volume(0.4)

    # Fundo animado
    ceu = pygame.image.load("imagens/tela_inicial.png").convert()
    x1 = 0
    x2 = ceu.get_width()
    velocidade = 2

    # Fontes
    fonte = pygame.font.Font("fontes/Pixelon.otf", 40)
    fonte_titulo = pygame.font.Font("fontes/Pixelscapes.ttf", 80)
    texto_titulo = fonte_titulo.render("ESCOLHA A DIFICULDADE", True, (255, 255, 255))

    # Botões
    botao_facil = pygame.Rect(540, 300, 200, 60)
    botao_medio = pygame.Rect(540, 400, 200, 60)
    botao_dificil = pygame.Rect(540, 500, 200, 60)

    texto_facil = fonte.render("FÁCIL", True, (255, 255, 255))
    texto_medio = fonte.render("MÉDIA", True, (255, 255, 255))
    texto_dificil = fonte.render("DIFÍCIL", True, (255, 255, 255))

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_facil.collidepoint(evento.pos):
                    som_clique.play()
                    print("Iniciar jogo na dificuldade FÁCIL")  # Substituir por jogo_facil()
                    return
                elif botao_medio.collidepoint(evento.pos):
                    som_clique.play()
                    print("Iniciar jogo na dificuldade MÉDIA")  # Substituir por jogo_medio()
                    return
                elif botao_dificil.collidepoint(evento.pos):
                    som_clique.play()
                    print("Iniciar jogo na dificuldade DIFÍCIL")  # Substituir por jogo_dificil()
                    return

        # Animação de fundo
        x1 -= velocidade
        x2 -= velocidade
        if x1 <= -ceu.get_width():
            x1 = x2 + ceu.get_width()
        if x2 <= -ceu.get_width():
            x2 = x1 + ceu.get_width()

        tela.blit(ceu, (x1, 0))
        tela.blit(ceu, (x2, 0))

        # Título centralizado
        tela.blit(texto_titulo, (tela.get_width() // 2 - texto_titulo.get_width() // 2, 100))

        # Posição do mouse
        mouse_pos = pygame.mouse.get_pos()

        # Cores com hover
        def cor_hover(botao, cor_normal, cor_hover):
            return cor_hover if botao.collidepoint(mouse_pos) else cor_normal

        # Desenhar botões
        pygame.draw.rect(tela, cor_hover(botao_facil, (0, 0, 255), (0, 100, 255)), botao_facil)
        pygame.draw.rect(tela, cor_hover(botao_medio, (0, 0, 128), (0, 50, 180)), botao_medio)
        pygame.draw.rect(tela, cor_hover(botao_dificil, (0, 0, 255), (0, 100, 255)), botao_dificil)

        # Textos nos botões
        tela.blit(texto_facil, (botao_facil.centerx - texto_facil.get_width() // 2,
                                botao_facil.centery - texto_facil.get_height() // 2))
        tela.blit(texto_medio, (botao_medio.centerx - texto_medio.get_width() // 2,
                                botao_medio.centery - texto_medio.get_height() // 2))
        tela.blit(texto_dificil, (botao_dificil.centerx - texto_dificil.get_width() // 2,
                                  botao_dificil.centery - texto_dificil.get_height() // 2))

        pygame.display.update()
        clock.tick(60)
