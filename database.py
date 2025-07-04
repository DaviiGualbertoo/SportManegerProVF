# database.py
import sqlite3

# Nome do arquivo do banco de dados
DB_NAME = "sportmanager.db"

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    # Retorna as linhas como dicionários, para facilitar o acesso por nome de coluna
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Cria as tabelas do banco de dados se elas não existirem."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tabela de Usuários (para login)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        senha TEXT NOT NULL
    )
    ''')

    # Tabela de Times
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        orcamento REAL NOT NULL DEFAULT 5000000.0,
        usuario_id INTEGER,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    ''')

    # Tabela de Jogadores
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        posicao TEXT NOT NULL,
        altura REAL,
        peso REAL,
        overall INTEGER NOT NULL,
        valor_mercado REAL NOT NULL,
        tipo TEXT NOT NULL, -- 'Profissional' ou 'Base'
        status_lesao TEXT DEFAULT 'Disponível', -- 'Disponível', 'Lesionado'
        tipo_lesao TEXT, -- 'Leve', 'Moderada', 'Grave'
        tempo_recuperacao INTEGER, -- em dias
        time_id INTEGER,
        FOREIGN KEY (time_id) REFERENCES times(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    # Se executarmos este arquivo diretamente, ele cria o banco e as tabelas.
    create_tables()