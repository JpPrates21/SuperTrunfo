class Carta:
    def __init__(self, nome, classe, velocidade, potencia, economia, frenagem, super_trunfo=False):
        self.nome = nome
        self.classe = classe
        self.velocidade = velocidade
        self.potencia = potencia
        self.economia = economia
        self.frenagem = frenagem
        self.super_trunfo = super_trunfo

    def __str__(self):
        return f"{self.nome} (Classe {self.classe})"
