# database.py
# Este arquivo é o "arquiteto" do nosso banco de dados.
# Sua única responsabilidade é definir e criar a estrutura (schema) das tabelas.

import sqlite3

# Define o nome do arquivo do nosso banco de dados como uma constante global.
DB_NAME = "sportmanager.db"

def get_db_connection():
    """
    Cria e retorna um objeto de conexão com o banco de dados.
    Esta função é usada por todos os controllers sempre que precisam falar com o banco.
    """
    # Abre ou cria o arquivo do banco de dados.
    conn = sqlite3.connect(DB_NAME)
    # Configuração de qualidade de vida: faz com que as linhas retornadas do banco
    # possam ser acessadas pelo nome da coluna (como um dicionário), e não por um índice numérico.
    # Ex: linha['nome'] em vez de linha[1].
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    """
    Contém os comandos SQL para criar todas as tabelas do sistema se elas não existirem.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tabela de Usuários: armazena as contas para login.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- Chave primária única para cada usuário.
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE, -- 'UNIQUE' impede emails duplicados.
        senha TEXT NOT NULL -- Armazenará o HASH da senha, não a senha real.
    )
    ''')

    # Tabela de Times: cada time pertence a um usuário.
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        orcamento REAL NOT NULL,
        escudo_url TEXT DEFAULT '/static/img/escudo_padrao.png',
        formacao_atual TEXT DEFAULT '4-3-3',
        usuario_id INTEGER,
        -- Chave estrangeira: cria um relacionamento com a tabela 'usuarios'.
        -- Garante que um time só pode pertencer a um usuário que existe.
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    ''')

    # Tabela de Jogadores: cada jogador pertence a um time.
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
        tipo TEXT NOT NULL, -- 'Profissional' ou 'Base'.
        status_lesao TEXT DEFAULT 'Disponível',
        tipo_lesao TEXT,
        tempo_recuperacao INTEGER,
        status_escalacao TEXT DEFAULT 'Reserva', -- 'Titular', 'Reserva'.
        posicao_indice INTEGER, -- Índice da posição (0-10) na formação.
        foto_url TEXT DEFAULT '/static/img/jogador_padrao.png',
        time_id INTEGER,
        -- Chave estrangeira que liga o jogador ao seu time.
        FOREIGN KEY (time_id) REFERENCES times(id)
    )
    ''')

    conn.commit() # Salva todas as alterações feitas.
    conn.close()  # Fecha a conexão.
    print("Tabelas criadas/atualizadas com sucesso!")

# Permite que este script seja executado diretamente com "python database.py" para criar o banco.
if __name__ == '__main__':
    create_tables()