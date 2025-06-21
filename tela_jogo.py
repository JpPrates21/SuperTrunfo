# tela_jogo.py

import pygame
import sys
import time


def mostrar_tela_jogo(tela, jogo, caminho_fundo):
    pygame.font.init()
    fonte_titulo = pygame.font.Font(None, 60)
    fonte_texto = pygame.font.Font(None, 36)

    # Carregar o fundo animado específico da dificuldade
    fundo_jogo = pygame.image.load(caminho_fundo).convert()
    x1 = 0
    x2 = fundo_jogo.get_width()
    velocidade = 2  # Ajuste a velocidade conforme necessário

    clock = pygame.time.Clock()

    def desenhar_carta(carta, x, y, destaque=False):
    
        cor_fundo = (255, 255, 255) if not destaque else (230, 255, 230)
        pygame.draw.rect(tela, cor_fundo, (x, y, 300, 400))
        pygame.draw.rect(tela, (0, 0, 0), (x, y, 300, 400), 4)

        nome = fonte_titulo.render(carta.nome, True, (0, 0, 0))
        classe = fonte_texto.render(f"Classe: {carta.classe}", True, (50, 50, 50))

        tela.blit(nome, (x + 20, y + 20))
        tela.blit(classe, (x + 20, y + 70))

        atributos = {
            "Velocidade": carta.velocidade,
            "Potencia": carta.potencia,
            "Economia": carta.economia,
            "Frenagem": carta.frenagem
        }

        botoes = []
        espacamento = 60
        pos_y = y + 120

        for chave, valor in atributos.items():
            texto = fonte_texto.render(f"{chave}: {valor}", True, (0, 0, 0))
            rect = pygame.Rect(x + 20, pos_y, 260, 40)
            pygame.draw.rect(tela, (200, 200, 200), rect)
            pygame.draw.rect(tela, (0, 0, 0), rect, 2)
            tela.blit(texto, (x + 30, pos_y + 5))
            botoes.append((rect, chave))
            pos_y += espacamento

        return botoes


    def desenhar_placar():
       
        texto = fonte_texto.render(
            f"Cartas - Você: {len(jogo.jogador.cartas)}  |  CPU: {len(jogo.cpu.cartas)}",
            True, (255, 255, 255)
        )
        tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 20))


    def comparar_atributo(attr):
       
        carta_jogador = jogo.jogador.cartas[0]
        carta_cpu = jogo.cpu.cartas[0]

        attr_key = attr.lower().replace("ç", "c").replace("ã", "a").replace("é", "e").replace("í", "i")

        valor_jogador = getattr(carta_jogador, attr_key)
        valor_cpu = getattr(carta_cpu, attr_key)

        if valor_jogador > valor_cpu:
            vencedor = "jogador"
            resultado = "Você venceu!"
        elif valor_jogador < valor_cpu:
            vencedor = "cpu"
            resultado = "Você perdeu!"
        else:
            vencedor = "empate"
            resultado = "Empate!"

        return vencedor, resultado


    mostrar_cpu = False
    resultado = ""
    tempo_resultado = 0
    vencedor_rodada = None
    botoes = []

    while True:
        # Movimento do fundo animado
        x1 -= velocidade
        x2 -= velocidade
        if x1 <= -fundo_jogo.get_width():
            x1 = x2 + fundo_jogo.get_width()
        if x2 <= -fundo_jogo.get_width():
            x2 = x1 + fundo_jogo.get_width()

        # Desenha o fundo animado
        tela.blit(fundo_jogo, (x1, 0))
        tela.blit(fundo_jogo, (x2, 0))

        # Checa se acabou o jogo
        if len(jogo.jogador.cartas) == 0 or len(jogo.cpu.cartas) == 0:
            vencedor = "Você venceu o jogo!" if len(jogo.jogador.cartas) > len(jogo.cpu.cartas) else "CPU venceu o jogo!"
            texto = fonte_titulo.render(vencedor, True, (255, 255, 0))
            tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 200))
            pygame.display.update()
            pygame.time.delay(3000)
            return

        desenhar_placar()

        carta_jogador = jogo.jogador.cartas[0]

        if mostrar_cpu:
            # Mostra ambas cartas com destaque
            desenhar_carta(carta_jogador, 80, 100, destaque=True)
            carta_cpu = jogo.cpu.cartas[0]
            desenhar_carta(carta_cpu, 450, 100, destaque=True)

            texto_resultado = fonte_titulo.render(resultado, True, (255, 255, 0))
            tela.blit(texto_resultado, (tela.get_width() // 2 - texto_resultado.get_width() // 2, 520))

            if time.time() - tempo_resultado > 2:
                if vencedor_rodada == "jogador":
                    jogo.jogador.cartas.append(jogo.cpu.cartas.pop(0))
                    jogo.jogador.cartas.append(jogo.jogador.cartas.pop(0))
                elif vencedor_rodada == "cpu":
                    jogo.cpu.cartas.append(jogo.jogador.cartas.pop(0))
                    jogo.cpu.cartas.append(jogo.cpu.cartas.pop(0))
                else:
                    jogo.jogador.cartas.append(jogo.jogador.cartas.pop(0))
                    jogo.cpu.cartas.append(jogo.cpu.cartas.pop(0))

                mostrar_cpu = False
                resultado = ""
                vencedor_rodada = None
                botoes = []

        else:
            botoes = desenhar_carta(carta_jogador, 80, 100)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not mostrar_cpu:
                for botao, atributo in botoes:
                    if botao.collidepoint(evento.pos):
                        vencedor_rodada, resultado = comparar_atributo(atributo)
                        mostrar_cpu = True
                        tempo_resultado = time.time()

        pygame.display.update()
        clock.tick(60)
