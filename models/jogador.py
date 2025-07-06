# models/jogador.py
from models.pessoa import Pessoa

class Jogador(Pessoa):
    """
    Representa um jogador, herdando características de Pessoa.
    Esta classe demonstra o pilar de Herança da Orientação a Objetos.
    Um Jogador "é uma" Pessoa.
    """
    def __init__(self, nome, idade, posicao, overall, valor_mercado, nacionalidade=None, altura=None, peso=None, status_lesao='Disponível', status_escalacao='Reserva', posicao_indice=None, foto_url='/static/img/jogador_padrao.png', id=None):
        # super().__init__() chama o construtor da classe mãe (Pessoa)
        # para que ele inicialize os atributos 'nome' e 'idade'. Isso evita reescrever código.
        super().__init__(nome, idade)
        
        # Atributos específicos da classe Jogador.
        self.id = id
        self.posicao = posicao
        self.nacionalidade = nacionalidade
        self.overall = overall
        self.valor_mercado = valor_mercado
        self.altura = altura
        self.peso = peso
        self.status_lesao = status_lesao
        self.status_escalacao = status_escalacao
        self.posicao_indice = posicao_indice
        self.foto_url = foto_url

    def descrever_status(self):
        """
        Método genérico que será sobrescrito pelas classes filhas.
        Este é o setup para o pilar de Polimorfismo.
        """
        return "Jogador sem categoria definida."


class JogadorProfissional(Jogador):
    """
    Especialização de Jogador para o time principal. Herda tudo de Jogador.
    """
    def descrever_status(self):
        # Polimorfismo: este método tem o mesmo nome do método na classe mãe (Jogador),
        # mas executa um comportamento diferente e mais específico.
        return "Profissional"


class JogadorBase(Jogador):
    """
    Especialização de Jogador para a categoria de base. Herda tudo de Jogador.
    """
    def descrever_status(self):
        # Polimorfismo: outro comportamento diferente para o mesmo método.
        return "Jogador da Base"