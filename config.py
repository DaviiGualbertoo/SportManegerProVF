# config.py
# Arquivo para guardar configurações globais da aplicação.

import os

# Define o diretório base do projeto.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chave secreta usada para assinar os cookies de sessão de forma criptográfica.
# Essencial para a segurança do sistema de login.
SECRET_KEY = "mude-esta-chave-para-algo-longo-e-dificil-de-adivinhar"