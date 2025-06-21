import json
import random

class Carta:
    def __init__(self, nome, classe, velocidade, potencia, economia, frenagem, super_trunfo=False):
        self.nome = nome
        self.classe = classe
        self.velocidade = velocidade
        self.potencia = potencia
        self.economia = economia
        self.frenagem = frenagem
        self.super_trunfo = super_trunfo

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []

class Jogo:
    def __init__(self, dificuldade):
        self.dificuldade = dificuldade.lower()  # minúsculas para consistência
        self.jogador = Jogador("Você")
        self.cpu = Jogador("CPU")
        self.cartas_disponiveis = []

    def carregar_cartas(self):
        with open("cartas.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        cartas = []
        for carta in dados:
            # Define super_trunfo True se a classe for "Super Trunfo" (ignora maiúsculas)
            carta['super_trunfo'] = (carta.get('classe', '').lower() == "super trunfo")
            cartas.append(Carta(**carta))
        self.cartas_disponiveis = cartas

    def distribuir_cartas(self):
        if self.dificuldade == "fácil":
            qtd_voce = 13
            qtd_cpu = 7
        elif self.dificuldade == "média":
            qtd_voce = 10
            qtd_cpu = 10
        else:  # difícil
            qtd_voce = 7
            qtd_cpu = 13

        total_cartas = qtd_voce + qtd_cpu
        cartas_sorteadas = random.sample(self.cartas_disponiveis, total_cartas)
        self.jogador.cartas = cartas_sorteadas[:qtd_voce]
        self.cpu.cartas = cartas_sorteadas[qtd_voce:]

    def iniciar(self):
        self.carregar_cartas()
        self.distribuir_cartas()

        # Log simples no terminal
        print(f"Cartas do {self.jogador.nome}:")
        for carta in self.jogador.cartas:
            print(f"- {carta.nome} ({carta.classe})")

        print(f"\nCartas do {self.cpu.nome}:")
        for carta in self.cpu.cartas:
            print(f"- {carta.nome} ({carta.classe})")

        # Retorna a carta do topo do jogador para exibição inicial
        return self.jogador.cartas[0] if self.jogador.cartas else None
