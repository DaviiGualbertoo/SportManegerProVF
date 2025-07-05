# controllers/usuario_controller.py

from bottle import route, template, request, redirect, response
from database import get_db_connection
from auth import hash_password, verify_password
import config
from utils import save_image_upload

@route('/register')
def register_form():
    """Exibe a página com o formulário de registro."""
    return template('views/register_form.tpl')

@route('/register', method='POST')
def process_register():
    """Processa o envio do formulário de registro."""
    # Usando request.forms.get() diretamente. A codificação é tratada pelo Bottle/navegador.
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    orcamento_str = request.forms.get('orcamento_inicial')
    
    if not nome or not email or not senha:
        return template('views/error.tpl', error_message="Nome, email e senha são obrigatórios.")

    try:
        # Validação do orçamento separada para uma mensagem de erro melhor
        if orcamento_str:
            orcamento_limpo = orcamento_str.replace('.', '').replace(',', '.')
            orcamento_inicial = float(orcamento_limpo)
        else:
            orcamento_inicial = 5000000.0
    except ValueError:
        return template('views/error.tpl', error_message="O valor do Orçamento Inicial é inválido. Use apenas números, pontos e vírgulas.")

    # Processa o upload do escudo
    escudo_upload = request.files.get('escudo')
    escudo_path = save_image_upload(escudo_upload, 'escudos')
    
    # Gera o hash seguro da senha
    senha_hash = hash_password(senha)

    with get_db_connection() as conn:
        try:
            cursor = conn.cursor()
            # Insere o novo usuário
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
            novo_usuario_id = cursor.lastrowid

            # Cria um time para este novo usuário
            nome_time = f"Time de {nome.split(' ')[0]}"
            sql = "INSERT INTO times (nome, orcamento, usuario_id, escudo_url) VALUES (?, ?, ?, ?)"
            params = (nome_time, orcamento_inicial, novo_usuario_id, escudo_path if escudo_path else '/static/img/escudo_padrao.png')
            cursor.execute(sql, params)
            
            conn.commit()
        except conn.IntegrityError:
            # Captura o erro que acontece se o email já existir na tabela
            return template('views/error.tpl', error_message="Este endereço de email já está cadastrado.")

    redirect('/login')

@route('/login')
def login_form():
    """Exibe a página com o formulário de login."""
    return template('views/login_form.tpl')

@route('/login', method='POST')
def process_login():
    """Processa o envio do formulário de login."""
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
    """Faz o logout do usuário, apagando o cookie de sessão."""
    response.delete_cookie("user_id")
    redirect('/login')