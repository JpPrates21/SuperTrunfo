class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_cartas(self, cartas):
        self.mao = cartas

    def mostrar_mao(self):
        for carta in self.mao:
            print(f"- {carta}")
