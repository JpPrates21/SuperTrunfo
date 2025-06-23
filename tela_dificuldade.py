import pygame
import sys
from jogo import Jogo
from tela_jogo import mostrar_tela_jogo 

def mostrar_tela_dificuldade(tela):
    pygame.mixer.init()
    som_clique = pygame.mixer.Sound("audios/SomClick.wav")
    som_clique.set_volume(0.4)

    ceu = pygame.image.load("imagens/tela_inicial.png").convert()
    x1 = 0
    x2 = ceu.get_width()
    velocidade = 2

    fonte = pygame.font.Font("fontes/Pixelon.otf", 40)
    fonte_titulo = pygame.font.Font("fontes/Pixelscapes.ttf", 80)
    texto_titulo = fonte_titulo.render("ESCOLHA A DIFICULDADE", True, (255, 255, 255))

    botao_facil = pygame.Rect(540, 300, 200, 60)
    botao_medio = pygame.Rect(540, 400, 200, 60)
    botao_dificil = pygame.Rect(540, 500, 200, 60)

    texto_facil = fonte.render("FÁCIL", True, (255, 255, 255))
    texto_medio = fonte.render("MÉDIA", True, (255, 255, 255))
    texto_dificil = fonte.render("DIFÍCIL", True, (255, 255, 255))

    clock = pygame.time.Clock()

    def cor_hover(botao, cor_normal, cor_hover):
        return cor_hover if botao.collidepoint(pygame.mouse.get_pos()) else cor_normal

    def iniciar_jogo(dificuldade, caminho_fundo):
        som_clique.play()
        jogo = Jogo(dificuldade)
        jogo.iniciar()
        # A função de jogo agora pode retornar um status
        status = mostrar_tela_jogo(tela, jogo, caminho_fundo, dificuldade)
        # Se o status for 'voltar_menu', nós retornamos para sair da tela de dificuldade
        if status == 'voltar_menu':
            return True # Sinaliza para voltar ao menu principal
        return False # Permanece na tela de dificuldade


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                voltar_para_menu = False
                if botao_facil.collidepoint(evento.pos):
                    voltar_para_menu = iniciar_jogo("fácil", "imagens/fundo_facil2.png")
                elif botao_medio.collidepoint(evento.pos):
                    voltar_para_menu = iniciar_jogo("média", "imagens/fundo_medio2.png")
                elif botao_dificil.collidepoint(evento.pos):
                    voltar_para_menu = iniciar_jogo("difícil", "imagens/fundo_dificil2.png")

                # --- ALTERAÇÃO AQUI ---
                # Se a função iniciar_jogo retornar True, saia da tela de dificuldade
                if voltar_para_menu:
                    return

        x1 -= velocidade
        x2 -= velocidade
        if x1 <= -ceu.get_width():
            x1 = x2 + ceu.get_width()
        if x2 <= -ceu.get_width():
            x2 = x1 + ceu.get_width()

        tela.blit(ceu, (x1, 0))
        tela.blit(ceu, (x2, 0))
        tela.blit(texto_titulo, (tela.get_width() // 2 - texto_titulo.get_width() // 2, 100))

        pygame.draw.rect(tela, cor_hover(botao_facil, (0, 0, 255), (0, 100, 255)), botao_facil)
        pygame.draw.rect(tela, cor_hover(botao_medio, (0, 0, 128), (0, 50, 180)), botao_medio)
        pygame.draw.rect(tela, cor_hover(botao_dificil, (0, 0, 255), (0, 100, 255)), botao_dificil)

        tela.blit(texto_facil, (botao_facil.centerx - texto_facil.get_width() // 2,
                                botao_facil.centery - texto_facil.get_height() // 2))
        tela.blit(texto_medio, (botao_medio.centerx - texto_medio.get_width() // 2,
                                botao_medio.centery - texto_medio.get_height() // 2))
        tela.blit(texto_dificil, (botao_dificil.centerx - texto_dificil.get_width() // 2,
                                  botao_dificil.centery - texto_dificil.get_height() // 2))

        pygame.display.update()
        clock.tick(60)