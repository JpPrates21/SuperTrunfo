import pygame
import sys
import time

def mostrar_tela_jogo(tela, jogo, caminho_fundo, dificuldade):
    pygame.font.init()
    fonte_titulo = pygame.font.Font("fontes/Pixelscapes.ttf", 80)
    fonte_placar = pygame.font.Font("fontes/Pixelon.otf", 40)
    fonte_nome = pygame.font.Font(None, 60)
    fonte_texto = pygame.font.Font(None, 36)
    fonte_botoes_jogo = pygame.font.Font(None, 28)
    
    # --- ALTERAÇÃO DE POSIÇÃO DOS BOTÕES ---
    # Ambos os botões foram movidos para a parte inferior da tela
    largura_tela = tela.get_width()
    altura_tela = tela.get_height()
    botao_voltar_dificuldade = pygame.Rect(largura_tela - 240, altura_tela - 50, 120, 40)
    botao_pause = pygame.Rect(largura_tela - 110, altura_tela - 50, 100, 40)

    if dificuldade == "fácil":
        COR_PRINCIPAL = (0, 200, 0)
    elif dificuldade == "média":
        COR_PRINCIPAL = (100, 149, 237)
    else:
        COR_PRINCIPAL = (255, 255, 0)
        
    COR_TEXTO_CARTA = (255, 255, 255)

    fundo_jogo = pygame.image.load(caminho_fundo).convert()
    x1 = 0
    x2 = fundo_jogo.get_width()
    velocidade = 2
    clock = pygame.time.Clock()

    # Estado de pause (continua o mesmo)
    jogo_pausado = False

    def desenhar_carta(carta, x, y, destaque=False):
        cor_fundo = (50, 50, 50) if not destaque else (80, 80, 80)
        pygame.draw.rect(tela, cor_fundo, (x, y, 300, 400))
        pygame.draw.rect(tela, (200, 200, 200), (x, y, 300, 400), 4)
        nome = fonte_nome.render(carta.nome, True, COR_TEXTO_CARTA)
        classe = fonte_texto.render(f"Classe: {carta.classe}", True, COR_TEXTO_CARTA)
        tela.blit(nome, (x + 20, y + 20))
        tela.blit(classe, (x + 20, y + 70))
        atributos = {"Velocidade": carta.velocidade, "Potencia": carta.potencia, "Economia": carta.economia, "Frenagem": carta.frenagem}
        botoes = []
        espacamento = 60
        pos_y = y + 120
        for chave, valor in atributos.items():
            texto = fonte_texto.render(f"{chave}: {valor}", True, COR_TEXTO_CARTA)
            rect = pygame.Rect(x + 20, pos_y, 260, 40)
            pygame.draw.rect(tela, (80, 80, 80), rect)
            pygame.draw.rect(tela, (200, 200, 200), rect, 2)
            tela.blit(texto, (x + 30, pos_y + 5))
            botoes.append((rect, chave))
            pos_y += espacamento
        return botoes

    def desenhar_placar():
        # Placar movido de volta para o centro do topo
        texto = fonte_placar.render(f"Você: {len(jogo.jogador.mao)}   |   CPU: {len(jogo.cpu.mao)}", True, COR_PRINCIPAL)
        tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 20))

    def comparar_atributo(attr, quem_escolheu):
        carta_jogador = jogo.jogador.mao[0]
        carta_cpu = jogo.cpu.mao[0]
        attr_key = attr.lower().replace("ç", "c").replace("ã", "a").replace("é", "e").replace("í", "i")
        if carta_jogador.classe.upper() == "A" and carta_cpu.super_trunfo: return "jogador", "Você venceu o SUPERTRUNFO!"
        if carta_cpu.classe.upper() == "A" and carta_jogador.super_trunfo: return "cpu", "Você perdeu com o SUPERTRUNFO!"
        if carta_jogador.super_trunfo and carta_cpu.classe.upper() != "A": return "jogador", "Você venceu com o SUPERTRUNFO!"
        if carta_cpu.super_trunfo and carta_jogador.classe.upper() != "A": return "cpu", "Você perdeu para o SUPERTRUNFO!"
        valor_jogador, valor_cpu = getattr(carta_jogador, attr_key), getattr(carta_cpu, attr_key)
        prefixo = f"{'CPU' if quem_escolheu == 'cpu' else 'Você'} escolheu {attr}: Você: {valor_jogador} | CPU: {valor_cpu} - "
        if valor_jogador > valor_cpu: return "jogador", prefixo + "Você venceu!"
        elif valor_jogador < valor_cpu: return "cpu", prefixo + "CPU venceu!"
        else: return "empate", prefixo + "Empate!"

    def cpu_escolher_melhor_atributo():
        carta_cpu = jogo.cpu.mao[0]
        atributos = {"Velocidade": carta_cpu.velocidade, "Potencia": carta_cpu.potencia, "Economia": carta_cpu.economia, "Frenagem": carta_cpu.frenagem}
        return max(atributos, key=atributos.get)

    mostrar_cpu, resultado, tempo_resultado, vencedor_rodada, botoes, vez_cpu = False, "", 0, None, [], False

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(), sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # --- LÓGICA DE PAUSE SIMPLIFICADA ---
                # Apenas inverte o estado da variável 'jogo_pausado'
                if botao_pause.collidepoint(evento.pos):
                    jogo_pausado = not jogo_pausado
                
                # O botão de voltar continua funcionando da mesma forma
                elif botao_voltar_dificuldade.collidepoint(evento.pos):
                    return # Volta para a tela de dificuldade
                
                # Os cliques do jogo só funcionam se o jogo NÃO estiver pausado
                if not jogo_pausado and not mostrar_cpu:
                    for botao, atributo in botoes:
                        if botao.collidepoint(evento.pos):
                            if atributo == "mostrar_cpu":
                                vencedor_rodada, resultado = comparar_atributo(cpu_escolher_melhor_atributo(), "cpu")
                            else:
                                vencedor_rodada, resultado = comparar_atributo(atributo, "jogador")
                            mostrar_cpu, tempo_resultado, vez_cpu = True, time.time(), (vencedor_rodada == "cpu")

        # A lógica do jogo (movimento e timers) só roda se NÃO estiver pausado
        if not jogo_pausado:
            x1 -= velocidade
            x2 -= velocidade
            if x1 <= -fundo_jogo.get_width(): x1 = x2 + fundo_jogo.get_width()
            if x2 <= -fundo_jogo.get_width(): x2 = x1 + fundo_jogo.get_width()

        tela.blit(fundo_jogo, (x1, 0))
        tela.blit(fundo_jogo, (x2, 0))

        if len(jogo.jogador.mao) == 0 or len(jogo.cpu.mao) == 0:
            vencedor = "Você venceu o jogo!" if len(jogo.jogador.mao) > len(jogo.cpu.mao) else "CPU venceu o jogo!"
            texto = fonte_titulo.render(vencedor, True, COR_PRINCIPAL)
            tela.blit(texto, (tela.get_width() // 2 - texto.get_width() // 2, 200))
            pygame.display.update()
            pygame.time.delay(3000)
            return

        desenhar_placar()
        
        # Desenha os botões na nova posição (embaixo)
        pygame.draw.rect(tela, (0, 0, 200), botao_voltar_dificuldade)
        texto_btn_voltar = fonte_botoes_jogo.render("VOLTAR", True, (255, 255, 255))
        tela.blit(texto_btn_voltar, (botao_voltar_dificuldade.centerx - texto_btn_voltar.get_width() // 2, botao_voltar_dificuldade.centery - texto_btn_voltar.get_height() // 2))

        # Altera a cor e o texto do botão de pause de acordo com o estado
        if jogo_pausado:
            cor_botao_pause = (0, 180, 0) # Verde para "Continuar"
            texto_do_botao = "CONTINUAR"
        else:
            cor_botao_pause = (200, 0, 0) # Vermelho para "Pausar"
            texto_do_botao = "PAUSAR"
            
        pygame.draw.rect(tela, cor_botao_pause, botao_pause)
        texto_btn_pause = fonte_botoes_jogo.render(texto_do_botao, True, (255, 255, 255))
        tela.blit(texto_btn_pause, (botao_pause.centerx - texto_btn_pause.get_width() // 2, botao_pause.centery - texto_btn_pause.get_height() // 2))


        if mostrar_cpu:
            desenhar_carta(jogo.jogador.mao[0], 80, 100, destaque=True)
            desenhar_carta(jogo.cpu.mao[0], tela.get_width() - 380, 100, destaque=True)
            texto_resultado = fonte_texto.render(resultado, True, COR_PRINCIPAL)
            tela.blit(texto_resultado, (tela.get_width() // 2 - texto_resultado.get_width() // 2, 520))
            
            # O timer do resultado também só avança se o jogo NÃO estiver pausado
            if not jogo_pausado and time.time() - tempo_resultado > 3:
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
                mostrar_cpu, resultado, vencedor_rodada, botoes = False, "", None, []
        else:
            if vez_cpu:
                desenhar_carta(jogo.jogador.mao[0], 80, 100)
                botao_cpu = pygame.Rect(tela.get_width() // 2 - 150, 520, 300, 50)
                pygame.draw.rect(tela, (100, 100, 255), botao_cpu)
                pygame.draw.rect(tela, (0, 0, 0), botao_cpu, 3)
                texto_botao = fonte_texto.render("Mostrar carta CPU", True, (255, 255, 255))
                tela.blit(texto_botao, (botao_cpu.x + 40, botao_cpu.y + 10))
                botoes = [(botao_cpu, "mostrar_cpu")]
            else:
                botoes = desenhar_carta(jogo.jogador.mao[0], 80, 100)

        # Se o jogo estiver pausado, mostra um texto grande na tela
        if jogo_pausado:
            texto_grande_pause = fonte_titulo.render("PAUSADO", True, (255, 255, 255))
            # Escurece a tela para dar destaque ao texto
            overlay = pygame.Surface((tela.get_width(), tela.get_height()), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            tela.blit(overlay, (0, 0))
            tela.blit(texto_grande_pause, (tela.get_width() // 2 - texto_grande_pause.get_width() // 2, tela.get_height() // 2 - 100))

        pygame.display.update()
        clock.tick(60)