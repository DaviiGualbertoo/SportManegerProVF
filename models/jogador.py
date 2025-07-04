# models/jogador.py

from models.pessoa import Pessoa

class Jogador(Pessoa):
    """
    Classe base para um jogador. Herda de Pessoa.
    """
    def __init__(self, nome, idade, posicao, overall, valor_mercado, altura=None, peso=None, status_lesao='Disponível', id=None):
        super().__init__(nome, idade)
        self.id = id
        self.posicao = posicao
        self.overall = overall
        self.valor_mercado = valor_mercado
        self.altura = altura
        self.peso = peso
        self.status_lesao = status_lesao

    def descrever_status(self):
        """
        Método polimórfico para descrever a categoria do jogador.
        """
        return "Jogador sem categoria definida."


class JogadorProfissional(Jogador):
    """
    Representa um jogador profissional. Herda de Jogador.
    """
    def descrever_status(self):
        return "Profissional"

    def calcular_bonus_salarial(self):
        return self.valor_mercado * (self.overall / 1000)


class JogadorBase(Jogador):
    """
    Representa um jogador da base. Herda de Jogador.
    """
    def descrever_status(self):
        return "Jogador da Base"
    
    def calcular_bonus_salarial(self):
        return 0