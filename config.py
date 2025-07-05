# config.py
import os

# Pega o caminho absoluto da pasta onde este arquivo está. Útil para referenciar outros arquivos.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chave secreta usada para assinar os cookies de sessão de forma segura.
# Em um projeto real, esta chave seria mais complexa e viria de uma variável de ambiente.
SECRET_KEY = "minha-chave-super-secreta-e-aleatoria-12345"