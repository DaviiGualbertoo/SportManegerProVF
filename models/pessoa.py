# models/pessoa.py
class Pessoa:
    """
    Classe base (Abstração) que representa uma Pessoa.
    Contém os atributos mais genéricos: nome e idade.
    Serve como "mãe" para outras classes mais específicas (demonstrando Herança).
    """
    def __init__(self, nome, idade):
        # O método construtor __init__ é chamado quando um novo objeto Pessoa é criado.
        # 'self' se refere à instância específica do objeto que está sendo criado.
        self.nome = nome
        self.idade = idade