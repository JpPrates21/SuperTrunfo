import json
import random
from carta import Carta

class Baralho:
    def __init__(self, caminho_json):
        self.cartas = self.carregar_cartas(caminho_json)

    def carregar_cartas(self, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return [Carta(**item) for item in dados]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def distribuir(self, qtd_jogador, qtd_cpu):
        self.embaralhar()
        cartas_jogador = self.cartas[:qtd_jogador]
        cartas_cpu = self.cartas[qtd_jogador:qtd_jogador + qtd_cpu]
        return cartas_jogador, cartas_cpu
