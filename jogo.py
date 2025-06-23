import json
import random
from carta import Carta
from jogador import Jogador, JogadorCPU  

class Jogo:
    def __init__(self, dificuldade):
        self.dificuldade = dificuldade.lower()
        self.jogador = Jogador("Você")
        self.cpu = JogadorCPU("CPU")  # Usa JogadorCPU para CPU
        self.cartas_disponiveis = []

    def carregar_cartas(self, caminho_arquivo="cartas.json"):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        cartas = []
        for carta in dados:
            carta['super_trunfo'] = (carta.get('classe', '').lower() == "super trunfo")
            cartas.append(Carta(**carta))
        self.cartas_disponiveis = cartas

    def distribuir_cartas(self):
        if self.dificuldade == "fácil":
            qtd_voce, qtd_cpu = 13, 7
        elif self.dificuldade == "média":
            qtd_voce, qtd_cpu = 10, 10
        else:
            qtd_voce, qtd_cpu = 7, 13

        total = qtd_voce + qtd_cpu
        sorteadas = random.sample(self.cartas_disponiveis, total)
        self.jogador.receber_cartas(sorteadas[:qtd_voce])
        self.cpu.receber_cartas(sorteadas[qtd_voce:])

    def iniciar(self):
        self.carregar_cartas()
        self.distribuir_cartas()

        print(f"Cartas do {self.jogador.nome}:")
        self.jogador.mostrar_mao()

        print(f"\nCartas do {self.cpu.nome}:")
        self.cpu.mostrar_mao()

        return self.jogador.mao[0] if self.jogador.mao else None
