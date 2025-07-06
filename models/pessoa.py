# models/pessoa.py
class Pessoa:
    """
    Classe base que representa uma Pessoa.
    Serve como ancestral para outras classes mais específicas (Herança).
    """
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade