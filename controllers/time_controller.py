# controllers/time_controller.py

from bottle import route, template, redirect, request
from database import get_db_connection
from models.time import Time
from models.jogador import JogadorProfissional, JogadorBase
from auth import get_current_user_id

@route('/time')
def exibir_time():
    """
    Exibe a página principal do time, com o elenco e informações.
    Esta rota é protegida e só pode ser acessada por usuários logados.
    """
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    with get_db_connection() as conn:
        time_db = conn.execute("SELECT * FROM times WHERE usuario_id = ?", (user_id,)).fetchone()

        if not time_db:
            return template('views/error.tpl', error_message="Seu usuário não possui um time associado.")

        jogadores_db = conn.execute("SELECT * FROM jogadores WHERE time_id = ?", (time_db['id'],)).fetchall()

    meu_time = Time(id=time_db['id'], nome=time_db['nome'], orcamento=time_db['orcamento'])
    
    lista_de_objetos_jogadores = []
    for j_db in jogadores_db:
        # CORREÇÃO APLICADA AQUI:
        # Garantimos que 'status_lesao' do banco (j_db) é passado
        # ao criar o objeto Jogador.
        if j_db['tipo'] == 'Profissional':
            jogador = JogadorProfissional(
                id=j_db['id'], 
                nome=j_db['nome'], 
                idade=j_db['idade'], 
                posicao=j_db['posicao'],
                altura=j_db['altura'],
                peso=j_db['peso'],
                overall=j_db['overall'], 
                valor_mercado=j_db['valor_mercado'],
                status_lesao=j_db['status_lesao']  # Esta linha é crucial
            )
        else: # 'Base'
            jogador = JogadorBase(
                id=j_db['id'], 
                nome=j_db['nome'], 
                idade=j_db['idade'], 
                posicao=j_db['posicao'],
                altura=j_db['altura'],
                peso=j_db['peso'],
                overall=j_db['overall'], 
                valor_mercado=j_db['valor_mercado'],
                status_lesao=j_db['status_lesao']  # E esta também
            )
        lista_de_objetos_jogadores.append(jogador)
    
    meu_time.jogadores = lista_de_objetos_jogadores
    forca_media = meu_time.calcular_forca_time()

    return template(
        'views/time_view.tpl', 
        time=meu_time, 
        jogadores=meu_time.jogadores, 
        forca_time=forca_media
    )


@route('/time/renomear', method='POST')
def renomear_time():
    """
    Atualiza o nome do time do usuário logado.
    """
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    novo_nome = request.forms.get('novo_nome')
    if not novo_nome:
        return template('views/error.tpl', error_message="O nome do time não pode ser vazio.")

    with get_db_connection() as conn:
        conn.execute("UPDATE times SET nome = ? WHERE usuario_id = ?", (novo_nome, user_id))
        conn.commit()

    redirect('/time')


@route('/time/orcamento', method='POST')
def gerenciar_orcamento():
    """
    Adiciona ou remove verba do orçamento do time do usuário logado.
    """
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    try:
        action = request.forms.get('action')
        valor = float(request.forms.get('valor'))

        if valor <= 0:
            return template('views/error.tpl', error_message="O valor deve ser positivo.")

        with get_db_connection() as conn:
            if action == 'add':
                conn.execute("UPDATE times SET orcamento = orcamento + ? WHERE usuario_id = ?", (valor, user_id))
            elif action == 'remove':
                conn.execute("UPDATE times SET orcamento = MAX(0, orcamento - ?) WHERE usuario_id = ?", (valor, user_id))
            
            conn.commit()

    except (ValueError, TypeError):
        return template('views/error.tpl', error_message="Valor inválido fornecido.")

    redirect('/time')