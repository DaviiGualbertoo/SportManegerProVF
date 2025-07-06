# controllers/usuario_controller.py
# Este controller gerencia tudo relacionado às contas dos usuários: registro, login e logout.

# Ferramentas importadas do Bottle para criar rotas, renderizar templates, etc.
from bottle import route, template, request, redirect, response
# Nossas funções personalizadas para interagir com o banco e a segurança.
from database import get_db_connection
from auth import hash_password, verify_password
import config
from utils import save_image_upload

@route('/register')
def register_form():
    """Esta função simplesmente exibe a página de registro (GET request)."""
    return template('views/register_form.tpl')

@route('/register', method='POST')
def process_register():
    """
    Esta função é acionada quando o usuário envia o formulário de registro (POST request).
    """
    # Pega os dados dos campos do formulário.
    nome = request.forms.get('nome')
    email = request.forms.get('email')
    senha = request.forms.get('senha')
    orcamento_str = request.forms.get('orcamento_inicial')
    
    # Validação simples para garantir que os campos principais não estão vazios.
    if not nome or not email or not senha:
        return template('views/error.tpl', error_message="Nome, email e senha são obrigatórios.")

    try:
        # Validação do orçamento com uma mensagem de erro específica.
        if orcamento_str:
            orcamento_limpo = orcamento_str.replace('.', '').replace(',', '.')
            orcamento_inicial = float(orcamento_limpo)
        else:
            orcamento_inicial = 5000000.0 # Valor padrão se o campo for deixado em branco.
    except ValueError:
        return template('views/error.tpl', error_message="O valor do Orçamento Inicial é inválido.")

    # Processa o upload do escudo do time.
    escudo_upload = request.files.get('escudo')
    escudo_path = save_image_upload(escudo_upload, 'escudos')
    
    # Usa nossa função de segurança para criar o hash da senha.
    senha_hash = hash_password(senha)

    # O 'with' garante que a conexão com o banco será fechada no final.
    with get_db_connection() as conn:
        try:
            cursor = conn.cursor()
            # Etapa 1: Insere o novo usuário na tabela 'usuarios'.
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha_hash))
            novo_usuario_id = cursor.lastrowid # Pega o ID do usuário que acabou de ser criado.

            # Etapa 2: Cria um time padrão para este novo usuário.
            nome_time = f"Time de {nome.split(' ')[0]}"
            sql = "INSERT INTO times (nome, orcamento, usuario_id, escudo_url) VALUES (?, ?, ?, ?)"
            params = (nome_time, orcamento_inicial, novo_usuario_id, escudo_path if escudo_path else '/static/img/escudo_padrao.png')
            cursor.execute(sql, params)
            
            # Se as duas operações (inserir usuário e time) deram certo, salva permanentemente.
            conn.commit()
        except conn.IntegrityError:
            # Captura o erro que acontece se o email já existir, mostrando uma mensagem amigável.
            return template('views/error.tpl', error_message="Este endereço de email já está cadastrado.")

    # Se tudo deu certo, redireciona o usuário para a página de login.
    redirect('/login')

@route('/login')
def login_form():
    """Esta função simplesmente exibe a página de login."""
    return template('views/login_form.tpl')

@route('/login', method='POST')
def process_login():
    """Processa o envio do formulário de login."""
    email = request.forms.get('email')
    senha_digitada = request.forms.get('senha')

    with get_db_connection() as conn:
        # Busca no banco um usuário com o email fornecido.
        user_db = conn.execute("SELECT * FROM usuarios WHERE email = ?", (email,)).fetchone()

    # Verificação de segurança em duas etapas:
    # 1. O usuário existe? (user_db não é None)
    # 2. A senha digitada corresponde ao hash salvo? (usando nossa função de verificação)
    if user_db and verify_password(senha_digitada, user_db['senha']):
        # Se as duas condições forem verdadeiras, o login é um sucesso.
        # Cria um cookie de sessão seguro no navegador do usuário para "lembrá-lo".
        response.set_cookie("user_id", str(user_db['id']), secret=config.SECRET_KEY)
        # Redireciona para a página principal da aplicação.
        redirect('/time')
    else:
        # Se uma das verificações falhar, mostra um erro.
        return template('views/error.tpl', error_message="Email ou senha inválidos. Tente novamente.")

@route('/logout')
def logout():
    """Faz o logout do usuário, apagando o cookie de sessão."""
    response.delete_cookie("user_id")
    # Redireciona para a tela de login.
    redirect('/login')