# reset_db.py
# Uma ferramenta de desenvolvimento para apagar e recriar o banco de dados rapidamente.

import os
from database import create_tables, DB_NAME

def reset_database_script():
    """
    Apaga o arquivo do banco de dados e chama a função para recriar as tabelas.
    """
    # Etapa de segurança para evitar execução acidental.
    confirm = input(f"Você tem CERTEZA que quer deletar o banco de dados '{DB_NAME}'? \nIsso apagará TODOS os dados. \nDigite 'sim' para continuar: ")

    # Se a resposta não for 'sim', cancela a operação.
    if confirm.lower() != 'sim':
        print("Operação cancelada.")
        return

    # Deleta o arquivo .db se ele existir.
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Banco de dados antigo '{DB_NAME}' deletado.")
    else:
        print("Nenhum banco de dados antigo para deletar.")

    # Chama a função de database.py para recriar as tabelas vazias.
    print("Criando novo banco de dados e tabelas...")
    create_tables()

if __name__ == "__main__":
    reset_database_script()