# Criando a classe SerVivo com os atributos pontos de vida e pontos de ataque
class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_vida = pontos_de_vida
        self.pontos_ataque = pontos_de_ataque

# Criando a classe Personagem, derivada da classe SerVivo, com atributo adicional chamado nome
class Personagem(SerVivo):
    def __init__(self, nome, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

# Criando a classe Monstro, derivada da classe SerVivo, com atributo adicional chamado tipo
class Monstro(SerVivo):
    def __init__(self, tipo, pontos_vida, pontos_ataque):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

# Criando a classe Lobo, derivada da classe Monstro, com atributo adicional chamado força
class Lobo(Monstro):
    def __init__(self, tipo, forca, pontos_vida, pontos_ataque):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.forca = forca

# Criando a classe Globin, derivada da classe Monstro, com atributo adicional chamado inteligência
class Globin(Monstro):
    def __init__(self, tipo, inteligencia, pontos_vida, pontos_ataque):
        super().__init__(tipo, pontos_vida, pontos_ataque)
        self.inteligencia = inteligencia
