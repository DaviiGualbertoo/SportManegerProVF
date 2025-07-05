# reset_db.py
import os
from database import create_tables, DB_NAME # Esta linha agora funciona

def reset_database_script():
    """
    Script de desenvolvimento para apagar o banco de dados e começar do zero.
    """
    confirm = input(f"Você tem CERTEZA que quer deletar o banco de dados '{DB_NAME}'? \nIsso apagará TODOS os dados. \nDigite 'sim' para continuar: ")

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