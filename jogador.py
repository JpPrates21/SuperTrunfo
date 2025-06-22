class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.mao = []

    def receber_cartas(self, cartas):
        self.mao = cartas

    def mostrar_mao(self):
        for carta in self.mao:
            print(f"- {carta}")

    def tem_cartas(self):
        return len(self.mao) > 0


class JogadorCPU(Jogador):
    def escolher_melhor_atributo(self, carta):
        atributos = {
            'velocidade': carta.velocidade,
            'potencia': carta.potencia,
            'economia': carta.economia,
            'frenagem': carta.frenagem
        }
        melhor = max(atributos, key=atributos.get)
        return melhor
