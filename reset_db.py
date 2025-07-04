# reset_db.py
import os
import sqlite3
from database import create_tables, DB_NAME

def reset_database():
    """
    Deleta o arquivo do banco de dados existente e recria as tabelas do zero.
    Inclui uma confirmação de segurança para evitar execução acidental.
    """
    # Etapa de segurança para evitar acidentes.
    confirm = input(f"Você tem CERTEZA que quer deletar o banco de dados '{DB_NAME}'? \nIsso apagará TODOS os usuários, times e jogadores. \nDigite 'sim' para continuar: ")

    if confirm.lower() != 'sim':
        print("Operação cancelada.")
        return

    # Se o arquivo do banco de dados existir, ele será deletado.
    if os.path.exists(DB_NAME):
        try:
            os.remove(DB_NAME)
            print(f"Banco de dados antigo '{DB_NAME}' deletado com sucesso.")
        except OSError as e:
            print(f"Erro ao deletar o banco de dados: {e}")
            return
    else:
        print("Nenhum banco de dados antigo encontrado para deletar.")

    # Recria o banco de dados e as tabelas vazias.
    try:
        print("Criando novo banco de dados e tabelas...")
        # A função create_tables() já está no seu arquivo database.py
        create_tables()
        print("Banco de dados resetado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar as novas tabelas: {e}")

if __name__ == "__main__":
    # Esta parte só executa quando o script é chamado diretamente.
    reset_database()