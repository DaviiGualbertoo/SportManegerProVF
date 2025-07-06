# models/time.py
class Time:
    """
    Representa um time de futebol com suas informações financeiras e elenco.
    """
    def __init__(self, nome, orcamento=5000000.0, escudo_url='/static/img/escudo_padrao.png', id=None):
        self.id = id
        self.nome = nome
        
        # Encapsulamento: O underscore '_' no início de '_orcamento' é uma convenção em Python
        # que sinaliza que este atributo é "protegido". Ele não deve ser alterado
        # diretamente de fora da classe (ex: meu_time._orcamento = 999).
        self._orcamento = orcamento
        
        self.escudo_url = escudo_url
        self.jogadores = [] # Esta lista conterá os OBJETOS Jogador do time, não apenas os dados.

    def get_orcamento(self):
        """
        Este é um método "getter". É a maneira pública e segura de LER o valor
        do atributo encapsulado _orcamento.
        """
        return self._orcamento

    def calcular_forca_time(self):
        """
        Calcula a média de overall de todos os jogadores no elenco do time.
        Este é um exemplo de um método que representa uma regra de negócio da classe.
        """
        # Se o time não tem jogadores, a força é 0 para evitar divisão por zero.
        if not self.jogadores:
            return 0
        
        # Usa uma "list comprehension" para somar todos os overalls de forma concisa e eficiente.
        soma_overall = sum(jogador.overall for jogador in self.jogadores)
        # Retorna a média arredondada para 2 casas decimais.
        return round(soma_overall / len(self.jogadores), 2)