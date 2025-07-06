# models/time.py
class Time:
    """
    Representa um time de futebol com suas informações e lista de jogadores.
    """
    def __init__(self, nome, orcamento=5000000.0, escudo_url='/static/img/escudo_padrao.png', id=None):
        self.id = id
        self.nome = nome
        # O '_' indica um atributo "protegido" (Encapsulamento).
        # Ele não deve ser alterado diretamente de fora da classe.
        self._orcamento = orcamento
        self.escudo_url = escudo_url
        self.jogadores = [] # Lista que conterá os objetos Jogador do time.

    def get_orcamento(self):
        """Método "getter" para acessar o orçamento de forma segura."""
        return self._orcamento

    def calcular_forca_time(self):
        """Calcula a média de overall de todos os jogadores do elenco."""
        if not self.jogadores:
            return 0
        soma_overall = sum(jogador.overall for jogador in self.jogadores)
        return round(soma_overall / len(self.jogadores), 2)