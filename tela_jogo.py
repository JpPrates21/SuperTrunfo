import pygame
import sys
import time

def mostrar_tela_jogo(tela, jogo, caminho_fundo):
    pygame.font.init()
    fonte_titulo = pygame.font.Font("fontes/Pixelscapes.ttf", 80)
    fonte_placar = pygame.font.Font("fontes/Pixelon.otf", 40)
    fonte_nome = pygame.font.Font(None, 60)
    fonte_texto = pygame.font.Font(None, 36)

    fundo_jogo = pygame.image.load(caminho_fundo).convert()
    x1 = 0
    x2 = fundo_jogo.get_width()
    velocidade = 2

    clock = pygame.time.Clock()

    def desenhar_carta(carta, x, y, destaque=False):
        cor_fundo = (255, 255, 255) if not destaque else (230, 255, 230)
        pygame.draw.rect(tela, cor_fundo, (x, y, 300, 400))
        pygame.draw.rect(tela, (0, 0, 0), (x, y, 300, 400), 4)

        nome = fonte_nome.render(carta.nome, True, (0, 0, 0))
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
        texto = fonte_placar.render(
            f"Você: {len(jogo.jogador.mao)}  |  CPU: {len(jogo.cpu.mao)}",
            True, (255, 255, 255)
        )
        tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 20))

    def comparar_atributo(attr, quem_escolheu):
        carta_jogador = jogo.jogador.mao[0]
        carta_cpu = jogo.cpu.mao[0]
        attr_key = attr.lower().replace("ç", "c").replace("ã", "a").replace("é", "e").replace("í", "i")

        if carta_jogador.classe.upper() == "A" and carta_cpu.super_trunfo:
            return "jogador", "Você venceu o SUPERTRUNFO!"
        if carta_cpu.classe.upper() == "A" and carta_jogador.super_trunfo:
            return "cpu", "Você perdeu com o SUPERTRUNFO!"

        if carta_jogador.super_trunfo and carta_cpu.classe.upper() != "A":
            return "jogador", "Você venceu com o SUPERTRUNFO!"
        if carta_cpu.super_trunfo and carta_jogador.classe.upper() != "A":
            return "cpu", "Você perdeu para o SUPERTRUNFO!"

        valor_jogador = getattr(carta_jogador, attr_key)
        valor_cpu = getattr(carta_cpu, attr_key)

        prefixo = f"{'CPU' if quem_escolheu == 'cpu' else 'Você'} escolheu {attr}: Você: {valor_jogador} | CPU: {valor_cpu} - "

        if valor_jogador > valor_cpu:
            return "jogador", prefixo + "Você venceu!"
        elif valor_jogador < valor_cpu:
            return "cpu", prefixo + "CPU venceu!"
        else:
            return "empate", prefixo + "Empate!"

    def cpu_escolher_melhor_atributo():
        carta_cpu = jogo.cpu.mao[0]
        atributos = {
            "Velocidade": carta_cpu.velocidade,
            "Potencia": carta_cpu.potencia,
            "Economia": carta_cpu.economia,
            "Frenagem": carta_cpu.frenagem
        }
        melhor_atributo = max(atributos, key=atributos.get)
        return melhor_atributo

    mostrar_cpu = False
    resultado = ""
    tempo_resultado = 0
    vencedor_rodada = None
    botoes = []
    vez_cpu = False

    while True:
        x1 -= velocidade
        x2 -= velocidade
        if x1 <= -fundo_jogo.get_width():
            x1 = x2 + fundo_jogo.get_width()
        if x2 <= -fundo_jogo.get_width():
            x2 = x1 + fundo_jogo.get_width()

        tela.blit(fundo_jogo, (x1, 0))
        tela.blit(fundo_jogo, (x2, 0))

        if len(jogo.jogador.mao) == 0 or len(jogo.cpu.mao) == 0:
            vencedor = "Você venceu o jogo!" if len(jogo.jogador.mao) > len(jogo.cpu.mao) else "CPU venceu o jogo!"
            texto = fonte_titulo.render(vencedor, True, (255, 255, 0))
            tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 200))
            pygame.display.update()
            pygame.time.delay(3000)
            return

        desenhar_placar()
        carta_jogador = jogo.jogador.mao[0]

        if mostrar_cpu:
            desenhar_carta(carta_jogador, 80, 100, destaque=True)
            carta_cpu = jogo.cpu.mao[0]
            desenhar_carta(carta_cpu, tela.get_width() - 380, 100, destaque=True)
            texto_resultado = fonte_texto.render(resultado, True, (255, 255, 0))
            tela.blit(texto_resultado, (tela.get_width() // 2 - texto_resultado.get_width() // 2, 520))

            if time.time() - tempo_resultado > 3:
                if vencedor_rodada == "jogador":
                    jogo.jogador.mao.append(jogo.cpu.mao.pop(0))
                    jogo.jogador.mao.append(jogo.jogador.mao.pop(0))
                    vez_cpu = False
                elif vencedor_rodada == "cpu":
                    jogo.cpu.mao.append(jogo.jogador.mao.pop(0))
                    jogo.cpu.mao.append(jogo.cpu.mao.pop(0))
                    vez_cpu = True
                else:
                    jogo.jogador.mao.append(jogo.jogador.mao.pop(0))
                    jogo.cpu.mao.append(jogo.cpu.mao.pop(0))

                mostrar_cpu = False
                resultado = ""
                vencedor_rodada = None
                botoes = []

        else:
            if vez_cpu:
                desenhar_carta(carta_jogador, 80, 100)
                botao_cpu = pygame.Rect(tela.get_width() // 2 - 150, 520, 300, 50)
                pygame.draw.rect(tela, (100, 100, 255), botao_cpu)
                pygame.draw.rect(tela, (0, 0, 0), botao_cpu, 3)
                texto_botao = fonte_texto.render("Mostrar carta CPU", True, (255, 255, 255))
                tela.blit(texto_botao, (botao_cpu.x + 40, botao_cpu.y + 10))
                botoes = [(botao_cpu, "mostrar_cpu")]
            else:
                botoes = desenhar_carta(carta_jogador, 80, 100)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not mostrar_cpu:
                for botao, atributo in botoes:
                    if botao.collidepoint(evento.pos):
                        if atributo == "mostrar_cpu":
                            atributo_cpu = cpu_escolher_melhor_atributo()
                            vencedor_rodada, resultado = comparar_atributo(atributo_cpu, "cpu")
                            mostrar_cpu = True
                            tempo_resultado = time.time()
                        else:
                            vencedor_rodada, resultado = comparar_atributo(atributo, "jogador")
                            mostrar_cpu = True
                            tempo_resultado = time.time()
                            vez_cpu = (vencedor_rodada == "cpu")

        pygame.display.update()
        clock.tick(60)
