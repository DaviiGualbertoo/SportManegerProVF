# controllers/time_controller.py
# Este controller gerencia a página principal do time e suas configurações.

from bottle import route, template, redirect, request
from database import get_db_connection
from models.time import Time
from models.jogador import JogadorProfissional, JogadorBase
from auth import get_current_user_id
from utils import save_image_upload

@route('/time')
def exibir_time():
    """
    Exibe a página principal do time do usuário logado (o elenco).
    """
    # Proteção de Rota: a primeira coisa é verificar se o usuário está logado.
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login') # Se não estiver, é expulso para a página de login.

    with get_db_connection() as conn:
        # Busca o time que pertence ao usuário logado (usando a chave estrangeira 'user_id').
        time_db = conn.execute("SELECT * FROM times WHERE usuario_id = ?", (user_id,)).fetchone()

        if not time_db:
            return template('views/error.tpl', error_message="Seu usuário não possui um time associado.")

        # Busca todos os jogadores que pertencem a esse time específico.
        jogadores_db = conn.execute("SELECT * FROM jogadores WHERE time_id = ? ORDER BY status_escalacao, overall DESC", (time_db['id'],)).fetchall()

    # Cria um objeto da classe Time com os dados vindos do banco.
    meu_time = Time(id=time_db['id'], nome=time_db['nome'], orcamento=time_db['orcamento'], escudo_url=time_db['escudo_url'])
    
    # Transforma os dados "crus" do banco em objetos "inteligentes" das nossas classes Model.
    lista_de_objetos_jogadores = []
    for j_db in jogadores_db:
        # Usa o Polimorfismo para criar o tipo de objeto correto (Profissional ou Base).
        if j_db['tipo'] == 'Profissional':
            jogador = JogadorProfissional(id=j_db['id'], nome=j_db['nome'], idade=j_db['idade'], posicao=j_db['posicao'], overall=j_db['overall'], valor_mercado=j_db['valor_mercado'], nacionalidade=j_db['nacionalidade'], altura=j_db['altura'], peso=j_db['peso'], status_lesao=j_db['status_lesao'], status_escalacao=j_db['status_escalacao'], posicao_indice=j_db['posicao_indice'], foto_url=j_db['foto_url'])
        else:
            jogador = JogadorBase(id=j_db['id'], nome=j_db['nome'], idade=j_db['idade'], posicao=j_db['posicao'], overall=j_db['overall'], valor_mercado=j_db['valor_mercado'], nacionalidade=j_db['nacionalidade'], altura=j_db['altura'], peso=j_db['peso'], status_lesao=j_db['status_lesao'], status_escalacao=j_db['status_escalacao'], posicao_indice=j_db['posicao_indice'], foto_url=j_db['foto_url'])
        lista_de_objetos_jogadores.append(jogador)
    
    # Adiciona a lista de objetos de jogadores ao nosso objeto de time.
    meu_time.jogadores = lista_de_objetos_jogadores
    # Usa um método do nosso Model para calcular a força média.
    forca_media = meu_time.calcular_forca_time()

    # Envia todos os dados e objetos para o template renderizar a página.
    return template('views/time_view.tpl', time=meu_time, jogadores=meu_time.jogadores, forca_time=forca_media)

@route('/time/renomear', method='POST')
def renomear_time():
    """Processa o formulário para renomear o time."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')

    novo_nome = request.forms.get('nome')
    if not novo_nome: return template('views/error.tpl', error_message="O nome do time não pode ser vazio.")
    
    with get_db_connection() as conn:
        # O comando UPDATE altera uma linha existente no banco.
        conn.execute("UPDATE times SET nome = ? WHERE usuario_id = ?", (novo_nome, user_id))
        conn.commit()
        
    redirect('/time')

@route('/time/orcamento', method='POST')
def gerenciar_orcamento():
    """Adiciona ou remove verba do orçamento do time."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')

    try:
        action = request.forms.get('action')
        valor_str = request.forms.get('valor')
        if not valor_str: return template('views/error.tpl', error_message="O campo de valor não pode ser vazio.")
        
        valor_limpo = valor_str.replace('.', '').replace(',', '.')
        valor = float(valor_limpo)
        if valor <= 0: return template('views/error.tpl', error_message="O valor deve ser positivo.")

        with get_db_connection() as conn:
            if action == 'add':
                conn.execute("UPDATE times SET orcamento = orcamento + ? WHERE usuario_id = ?", (valor, user_id))
            elif action == 'remove':
                # MAX(0, ...) impede que o orçamento fique com um valor negativo.
                conn.execute("UPDATE times SET orcamento = MAX(0, orcamento - ?) WHERE usuario_id = ?", (valor, user_id))
            conn.commit()
    except (ValueError, TypeError):
        return template('views/error.tpl', error_message="Valor numérico inválido fornecido.")
    
    redirect('/time')

@route('/time/upload-escudo', method='POST')
def upload_escudo():
    """Processa o upload de um novo escudo para o time."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')

    escudo_upload = request.files.get('escudo')
    # Usa nossa função utilitária para salvar a imagem.
    escudo_path = save_image_upload(escudo_upload, 'escudos')

    if escudo_path:
        with get_db_connection() as conn:
            conn.execute("UPDATE times SET escudo_url = ? WHERE usuario_id = ?", (escudo_path, user_id))
            conn.commit()
            
    redirect('/time')