# controllers/usuario_controller.py

from bottle import route, template, request, redirect, response
from database import get_db_connection
from auth import hash_password, verify_password
import config

# --- Rotas de Registro ---

@route('/register')
def register_form():
    """Exibe o formulário de registro para um novo usuário."""
    return template('views/register_form.tpl')

@route('/register', method='POST')
def process_register():
    """Processa os dados do formulário de registro."""
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    senha = request.forms.get('senha')

    # LÓGICA DO ORÇAMENTO INICIAL
    orcamento_str = request.forms.get('orcamento_inicial')
    # Se o campo foi preenchido, converte para float. Senão, usa o valor padrão.
    orcamento_inicial = float(orcamento_str) if orcamento_str else 5000000.0

    if not nome or not email or not senha:
        return template('views/error.tpl', error_message="Todos os campos são obrigatórios.")

    senha_hash = hash_password(senha)

    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                (nome, email, senha_hash)
            )
            novo_usuario_id = cursor.lastrowid

            nome_time = f"Time de {nome.split(' ')[0]}"
            # Usamos a variável orcamento_inicial no INSERT
            cursor.execute(
                "INSERT INTO times (nome, orcamento, usuario_id) VALUES (?, ?, ?)",
                (nome_time, orcamento_inicial, novo_usuario_id)
            )
            conn.commit()

        except conn.IntegrityError:
            return template('views/error.tpl', error_message="Este endereço de email já está cadastrado.")

    redirect('/login')


# --- Rotas de Login e Logout ---

@route('/login')
def login_form():
    """Exibe o formulário de login."""
    return template('views/login_form.tpl')

@route('/login', method='POST')
def process_login():
    """Processa os dados do formulário de login."""
    email = request.forms.get('email')
    senha_digitada = request.forms.get('senha')

    with get_db_connection() as conn:
        user_db = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()

    if user_db and verify_password(senha_digitada, user_db['senha']):
        response.set_cookie("user_id", str(user_db['id']), secret=config.SECRET_KEY)
        redirect('/time')
    else:
        return template('views/error.tpl', error_message="Email ou senha inválidos. Tente novamente.")


@route('/logout')
def logout():
    """Faz o logout do usuário."""
    response.delete_cookie("user_id")
    redirect('/login')