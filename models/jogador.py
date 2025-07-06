# models/jogador.py
from models.pessoa import Pessoa

class Jogador(Pessoa):
    """Classe base para todos os jogadores."""
    def __init__(self, nome, idade, posicao, overall, valor_mercado, nacionalidade=None, altura=None, peso=None, status_lesao='Disponível', status_escalacao='Reserva', posicao_indice=None, foto_url='/static/img/jogador_padrao.png', id=None):
        super().__init__(nome, idade)
        self.id = id
        self.posicao = posicao
        self.nacionalidade = nacionalidade
        self.overall = overall
        self.valor_mercado = valor_mercado
        self.altura = altura
        self.peso = peso
        self.status_lesao = status_lesao
        self.status_escalacao = status_escalacao
        self.posicao_indice = posicao_indice # MUDANÇA APLICADA AQUI
        self.foto_url = foto_url

    def descrever_status(self):
        """Retorna uma descrição básica do status do jogador."""
        return f"{self.nome}, {self.posicao}, Overall: {self.overall}"

class JogadorProfissional(Jogador):
    """Representa um jogador do time principal."""
    def descrever_status(self):
        return "Jogador Profissional"

class JogadorBase(Jogador):
    """Representa um jogador da categoria de base."""
    def descrever_status(self):
        return "Jogador da Base"