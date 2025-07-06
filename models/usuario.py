# models/usuario.py
class Usuario:
    """
    Representa um usuário (técnico) no sistema.
    Neste momento, é uma classe simples que serve como um "container" para os dados do usuário.
    Poderia ser expandida com mais métodos, como por exemplo, um para verificar permissões.
    """
    def __init__(self, nome, email, senha, id=None):
        self.id = id
        self.nome = nome
        self.email = email
        # Importante: na prática, este atributo 'senha' conterá o HASH da senha,
        # e não a senha em texto puro, que vem do formulário.
        self.senha = senha