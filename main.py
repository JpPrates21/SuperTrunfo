import pygame
from tela_inicial import mostrar_tela_inicial

pygame.init()
pygame.mixer.init()

LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("SuperTrunfo")

# Carregar e tocar música de fundo uma vez 
pygame.mixer.music.load("audios/MusicaTelaInicial.wav")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

mostrar_tela_inicial(tela)
