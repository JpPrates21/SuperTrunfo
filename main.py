import pygame
from tela_inicial import mostrar_tela_inicial

pygame.init()
LARGURA, ALTURA = 1280, 720
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("SuperTrunfo")

mostrar_tela_inicial(tela)
