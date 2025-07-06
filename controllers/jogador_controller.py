# controllers/jogador_controller.py
# Este controller gerencia todas as ações relacionadas a um jogador individual:
# criar, editar, ver detalhes, vender, promover e lesionar.

from bottle import route, template, request, redirect
from database import get_db_connection
from auth import get_current_user_id
from utils import save_image_upload

@route('/jogadores/novo')
def novo_jogador_form():
    """Exibe o formulário de cadastro de um novo jogador."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    return template('views/jogador_form.tpl')

@route('/jogadores/novo', method='POST')
def salvar_novo_jogador():
    """Processa o formulário de cadastro e salva o novo jogador no banco."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')

    # Pega os dados de texto do formulário.
    nome = request.forms.get('nome')
    nacionalidade = request.forms.get('nacionalidade')
    posicao = request.forms.get('posicao')
    tipo = request.forms.get('tipo')
    
    if not nome or not posicao or not tipo:
        return template("views/error.tpl", error_message="Nome, Posição e Tipo são campos obrigatórios.")

    try:
        # Validação separada para números inteiros para dar uma mensagem de erro clara.
        idade = int(request.forms.get('idade'))
        overall = int(request.forms.get('overall'))
    except (ValueError, TypeError):
        return template("views/error.tpl", error_message="Erro: Idade e Overall devem ser números inteiros válidos.")

    try:
        # Validação separada para números decimais.
        altura_str = request.forms.get('altura')
        altura = float(altura_str.replace(',', '.')) if altura_str else None
        peso_str = request.forms.get('peso')
        peso = float(peso_str.replace(',', '.')) if peso_str else None
        valor_mercado_str = request.forms.get('valor_mercado')
        valor_mercado_limpo = valor_mercado_str.replace('.', '').replace(',', '.')
        valor_mercado = float(valor_mercado_limpo)
    except (ValueError, TypeError):
        return template("views/error.tpl", error_message="Erro: Altura, Peso e Valor de Mercado devem ser números válidos.")

    foto_upload = request.files.get('foto')
    foto_path = save_image_upload(foto_upload, 'jogadores')

    with get_db_connection() as conn:
        time_db = conn.execute("SELECT id FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
    if not time_db: return template('views/error.tpl', error_message="Time não encontrado para este usuário.")
    time_id = time_db['id']

    with get_db_connection() as conn:
        # Monta a query SQL dinamicamente para incluir a foto apenas se ela foi enviada.
        sql_cols = "nome, nacionalidade, idade, posicao, altura, peso, overall, valor_mercado, tipo, time_id"
        sql_vals = "?, ?, ?, ?, ?, ?, ?, ?, ?, ?"
        params = [nome, nacionalidade, idade, posicao, altura, peso, overall, valor_mercado, tipo, time_id]
        if foto_path:
            sql_cols += ", foto_url"
            sql_vals += ", ?"
            params.append(foto_path)
        sql = f"INSERT INTO jogadores ({sql_cols}) VALUES ({sql_vals})"
        conn.execute(sql, tuple(params))
        conn.commit()
    
    redirect('/time')

@route('/jogador/editar/<jogador_id:int>')
def exibir_form_edicao_jogador(jogador_id):
    """Exibe o formulário de edição pré-preenchido com os dados do jogador."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        jogador_db = conn.execute("SELECT * FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
    if not jogador_db: return template('views/error.tpl', error_message="Jogador não encontrado.")
    return template('views/jogador_edit_form.tpl', jogador=jogador_db)

@route('/jogador/editar/<jogador_id:int>', method='POST')
def salvar_edicao_jogador(jogador_id):
    """Processa o formulário de edição e atualiza o jogador no banco."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    try:
        # A mesma lógica de validação e limpeza do cadastro é aplicada aqui.
        nome = request.forms.get('nome')
        nacionalidade = request.forms.get('nacionalidade')
        posicao = request.forms.get('posicao')
        idade = int(request.forms.get('idade'))
        overall = int(request.forms.get('overall'))
        altura_str = request.forms.get('altura')
        altura = float(altura_str.replace(',', '.')) if altura_str else None
        peso_str = request.forms.get('peso')
        peso = float(peso_str.replace(',', '.')) if peso_str else None
        valor_mercado_str = request.forms.get('valor_mercado')
        valor_mercado_limpo = valor_mercado_str.replace('.', '').replace(',', '.')
        valor_mercado = float(valor_mercado_limpo)
        foto_upload = request.files.get('foto')
        foto_path = save_image_upload(foto_upload, 'jogadores')

        # Monta a query de UPDATE dinamicamente.
        sql = "UPDATE jogadores SET nome = ?, nacionalidade = ?, idade = ?, posicao = ?, altura = ?, peso = ?, overall = ?, valor_mercado = ?"
        params = [nome, nacionalidade, idade, posicao, altura, peso, overall, valor_mercado]
        if foto_path:
            sql += ", foto_url = ?"
            params.append(foto_path)
        sql += " WHERE id = ?"
        params.append(jogador_id)

        with get_db_connection() as conn:
            if not verificar_posse_jogador(conn, user_id, jogador_id):
                return template('views/error.tpl', error_message="Acesso negado.")
            conn.execute(sql, tuple(params))
            conn.commit()
        redirect(f"/jogador/{jogador_id}")
    except (ValueError, TypeError):
        return template("views/error.tpl", error_message="Erro: Verifique se os valores numéricos são válidos.")

@route('/jogador/<jogador_id:int>')
def detalhes_do_jogador(jogador_id):
    """Exibe a ficha completa de um jogador específico."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        jogador_db = conn.execute("SELECT * FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
    if jogador_db:
        return template('views/detalhes_jogador.tpl', jogador=jogador_db)
    else:
        return template('views/error.tpl', error_message="Jogador não encontrado.")

def verificar_posse_jogador(conn, user_id, jogador_id):
    """Função de segurança que impede um usuário de modificar jogadores de outro time."""
    resultado = conn.execute("SELECT j.time_id FROM jogadores j INNER JOIN times t ON j.time_id = t.id WHERE j.id = ? AND t.usuario_id = ?", (jogador_id, user_id)).fetchone()
    return resultado is not None

@route('/jogador/vender/<jogador_id:int>')
def vender_jogador(jogador_id):
    """Vende um jogador, removendo-o do elenco e atualizando o orçamento."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        jogador_vendido = conn.execute("SELECT valor_mercado, time_id FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
        valor = jogador_vendido['valor_mercado']
        time_id = jogador_vendido['time_id']
        conn.execute("UPDATE times SET orcamento = orcamento + ? WHERE id = ?", (valor, time_id))
        conn.execute("DELETE FROM jogadores WHERE id = ?", (jogador_id,))
        conn.commit()
    redirect('/time')

@route('/jogador/promover/<jogador_id:int>')
def promover_jogador(jogador_id):
    """Promove um jogador da base para o time profissional."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        conn.execute("UPDATE jogadores SET tipo = 'Profissional' WHERE id = ?", (jogador_id,))
        conn.commit()
    redirect('/time')

@route('/jogador/lesao/<jogador_id:int>')
def exibir_formulario_lesao(jogador_id):
    """Exibe o formulário para registrar uma lesão."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        jogador = conn.execute("SELECT id, nome FROM jogadores WHERE id = ?", (jogador_id,)).fetchone()
    if jogador: return template('views/lesao_form.tpl', jogador=jogador)
    else: return template('views/error.tpl', error_message="Jogador não encontrado.")

@route('/jogador/lesao/<jogador_id:int>', method='POST')
def salvar_status_lesao(jogador_id):
    """Processa o formulário de lesão e atualiza o status do jogador."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    tipo_lesao = request.forms.get('tipo_lesao')
    try:
        tempo_recuperacao = int(request.forms.get('tempo_recuperacao'))
    except (ValueError, TypeError):
        return template("views/error.tpl", error_message="O tempo de recuperação deve ser um número.")
    with get_db_connection() as conn:
        if not verificar_posse_jogador(conn, user_id, jogador_id):
            return template('views/error.tpl', error_message="Acesso negado.")
        conn.execute("UPDATE jogadores SET status_lesao = 'Lesionado', tipo_lesao = ?, tempo_recuperacao = ? WHERE id = ?", (tipo_lesao, tempo_recuperacao, jogador_id))
        conn.commit()
    redirect('/time')