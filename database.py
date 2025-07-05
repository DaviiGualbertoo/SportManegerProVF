# database.py
import sqlite3

DB_NAME = "sportmanager.db"

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """Define e cria a estrutura de todas as tabelas do banco de dados."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        orcamento REAL NOT NULL,
        escudo_url TEXT DEFAULT '/static/img/escudo_padrao.png',
        formacao_atual TEXT DEFAULT '4-3-3',
        usuario_id INTEGER,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS jogadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        nacionalidade TEXT,
        idade INTEGER NOT NULL,
        posicao TEXT NOT NULL,
        altura REAL,
        peso REAL,
        overall INTEGER NOT NULL,
        valor_mercado REAL NOT NULL,
        tipo TEXT NOT NULL,
        status_lesao TEXT DEFAULT 'Disponível',
        tipo_lesao TEXT,
        tempo_recuperacao INTEGER,
        status_escalacao TEXT DEFAULT 'Reserva',
        posicao_indice INTEGER,
        foto_url TEXT DEFAULT '/static/img/jogador_padrao.png',
        time_id INTEGER,
        FOREIGN KEY (time_id) REFERENCES times(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Tabelas criadas/atualizadas com sucesso!")

if __name__ == '__main__':
    # Se este arquivo for executado diretamente, ele cria o banco.
    create_tables()