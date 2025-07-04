# controllers/jogador_controller.py

from bottle import route, template, request, redirect
from database import get_db_connection
from auth import get_current_user_id

# --- Funções de Cadastro de Jogador ---

@route('/jogadores/novo')
def novo_jogador_form():
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')
    return template('views/jogador_form.tpl')


@route('/jogadores/novo', method='POST')
def salvar_novo_jogador():
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    try:
        with get_db_connection() as conn:
            time_db = conn.execute("SELECT id FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
        
        if not time_db:
            return template('views/error.tpl', error_message="Time não encontrado para este usuário.")
        
        time_id = time_db['id']
        nome = request.forms.get('nome')
        idade = int(request.forms.get('idade'))
        posicao = request.forms.get('posicao')
        altura_str = request.forms.get('altura')
        altura = float(altura_str) if altura_str else None
        peso_str = request.forms.get('peso')
        peso = float(peso_str) if peso_str else None
        overall = int(request.forms.get('overall'))
        valor_mercado = float(request.forms.get('valor_mercado'))
        tipo = request.forms.get('tipo')

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO jogadores (nome, idade, posicao, altura, peso, overall, valor_mercado, tipo, time_id) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (nome, idade, posicao, altura, peso, overall, valor_mercado, tipo, time_id)
            )
            conn.commit()
        
        redirect('/time')
    
    except ValueError:
        return template("views/error.tpl", error_message="Erro: Verifique se todos os campos obrigatórios foram preenchidos e se os valores numéricos são válidos.")

# --- ROTA DE DETALHES ---
@route('/jogador/<jogador_id:int>')
def detalhes_do_jogador(jogador_id):
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado. Este jogador não pertence ao seu time.")
        
        jogador_db = conn.execute("SELECT * FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()

    if jogador_db:
        return template('views/detalhes_jogador.tpl', jogador=jogador_db)
    else:
        return template('views/error.tpl', error_message="Jogador não encontrado.")


# --- Ações em Jogadores Existentes (Vender, Promover, Lesionar) ---

def verificar_posse_jogador(conn, user_id, jogador_id):
    resultado = conn.execute("""
        SELECT j.time_id FROM jogadores j
        INNER JOIN times t ON j.time_id = t.id
        WHERE j.id = ? AND t.usuario_id = ?
    """, (jogador_id, user_id)).fetchone()
    return resultado is not None


@route('/jogador/vender/<jogador_id:int>')
def vender_jogador(jogador_id):
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado. Você não tem permissão para vender este jogador.")
        
        jogador_vendido = conn.execute("SELECT valor_mercado, time_id FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
        valor = jogador_vendido['valor_mercado']
        time_id = jogador_vendido['time_id']

        conn.execute("UPDATE times SET orcamento = orcamento + ? WHERE id = ?", (valor, time_id))
        conn.execute("DELETE FROM jogadores WHERE id = ?", (jogador_id,))
        conn.commit()

    redirect('/time')


@route('/jogador/promover/<jogador_id:int>')
def promover_jogador(jogador_id):
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado. Você não tem permissão para promover este jogador.")

        conn.execute("UPDATE jogadores SET tipo = 'Profissional' WHERE id = ?", (jogador_id,))
        conn.commit()

    redirect('/time')


@route('/jogador/lesao/<jogador_id:int>')
def exibir_formulario_lesao(jogador_id):
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        
        jogador = conn.execute("SELECT id, nome FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
        
    if jogador:
        return template('views/lesao_form.tpl', jogador=jogador)
    else:
        return template('views/error.tpl', error_message="Jogador não encontrado.")


@route('/jogador/lesao/<jogador_id:int>', method='POST')
def salvar_status_lesao(jogador_id):
    user_id = get_current_user_id()
    if not user_id:
        redirect('/login')

    tipo_lesao = request.forms.get('tipo_lesao')
    tempo_recuperacao = int(request.forms.get('tempo_recuperacao'))

    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")

        conn.execute(
            "UPDATE jogadores SET status_lesao = 'Lesionado', tipo_lesao = ?, tempo_recuperacao = ? WHERE id = ?",
            (tipo_lesao, tempo_recuperacao, jogador_id)
        )
        conn.commit()
    
    redirect('/time')