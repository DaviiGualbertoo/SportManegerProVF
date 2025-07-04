# models/time.py
class Time:
    def __init__(self, nome, orcamento=5000000.0, id=None):
        self.nome = nome
        self._orcamento = orcamento  # Atributo privado/protegido (Encapsulamento)
        self.jogadores = [] # Lista de objetos Jogador
        self.id = id

    # Um "getter" para acessar o orçamento de forma segura
    def get_orcamento(self):
        return self._orcamento

    # Método para modificar o orçamento de forma controlada
    def vender_jogador(self, jogador):
        if jogador in self.jogadores:
            self._orcamento += jogador.valor_mercado
            self.jogadores.remove(jogador)
            print(f"Jogador {jogador.nome} vendido! Orçamento atual: {self._orcamento}")
            return True
        return False

    # Outro método para modificar o orçamento
    def adicionar_verba(self, valor):
        if valor > 0:
            self._orcamento += valor

    # Sua funcionalidade extra!
    def calcular_forca_time(self):
        if not self.jogadores: # Se não houver jogadores
            return 0

        soma_overall = 0
        for jogador in self.jogadores:
            soma_overall += jogador.overall

        media = soma_overall / len(self.jogadores)
        return round(media, 2) # Arredonda para 2 casas decimais