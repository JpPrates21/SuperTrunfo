import pygame

def mostrar_tela_jogo(tela, jogo):
    carta_topo = jogo.jogador.cartas[0] if jogo.jogador.cartas else None
    fonte = pygame.font.Font("fontes/Pixelon.otf", 30)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        tela.fill((20, 20, 20))

        if carta_topo:
            pygame.draw.rect(tela, (0, 0, 255), (300, 200, 400, 300), border_radius=15)
            nome = fonte.render(f"Nome: {carta_topo.nome}", True, (255, 255, 255))
            classe = fonte.render(f"Classe: {carta_topo.classe}", True, (255, 255, 255))
            vel = fonte.render(f"Velocidade: {carta_topo.velocidade}", True, (255, 255, 255))
            pot = fonte.render(f"Potência: {carta_topo.potencia}", True, (255, 255, 255))
            eco = fonte.render(f"Economia: {carta_topo.economia}", True, (255, 255, 255))
            fre = fonte.render(f"Frenagem: {carta_topo.frenagem}", True, (255, 255, 255))

            tela.blit(nome, (320, 220))
            tela.blit(classe, (320, 260))
            tela.blit(vel, (320, 300))
            tela.blit(pot, (320, 340))
            tela.blit(eco, (320, 380))
            tela.blit(fre, (320, 420))

        pygame.display.update()
