# controllers/escalacao_controller.py
# Este controller gerencia a lógica complexa da página de escalação.

from bottle import route, template, redirect, request
from database import get_db_connection
from auth import get_current_user_id
import random

# Dicionários de configuração para a lógica de escalação.
SETORES = {'Goleiro': 'Goleiro', 'Zagueiro': 'Defesa', 'Lateral Direito': 'Defesa', 'Lateral Esquerdo': 'Defesa', 'Volante': 'Meio-Campo', 'Meia Central': 'Meio-Campo', 'Meia Ofensivo': 'Meio-Campo', 'Ponta Direita': 'Ataque', 'Ponta Esquerda': 'Ataque', 'Centroavante': 'Ataque', 'Ala Direito': 'Defesa', 'Ala Esquerdo': 'Defesa', 'Meia Direita': 'Meio-Campo', 'Meia Esquerda': 'Meio-Campo', 'Atacante': 'Ataque'}

FORMACOES = {'4-4-2': ['Goleiro', 'Lateral Esquerdo', 'Zagueiro', 'Zagueiro', 'Lateral Direito', 'Meia Esquerda', 'Volante', 'Volante', 'Meia Direita', 'Atacante', 'Atacante'], '4-3-3': ['Goleiro', 'Lateral Esquerdo', 'Zagueiro', 'Zagueiro', 'Lateral Direito', 'Volante', 'Meia Central', 'Meia Ofensivo', 'Ponta Esquerda', 'Ponta Direita', 'Centroavante'], '4-2-3-1': ['Goleiro', 'Lateral Esquerdo', 'Zagueiro', 'Zagueiro', 'Lateral Direito', 'Volante', 'Volante', 'Meia Ofensivo', 'Ponta Esquerda', 'Ponta Direita', 'Centroavante'], '3-5-2': ['Goleiro', 'Zagueiro', 'Zagueiro', 'Zagueiro', 'Ala Esquerdo', 'Volante', 'Meia Central', 'Meia Central', 'Ala Direito', 'Atacante', 'Atacante'], '5-3-2': ['Goleiro', 'Zagueiro', 'Zagueiro', 'Zagueiro', 'Ala Esquerdo', 'Ala Direito', 'Volante', 'Meia Central', 'Meia Central', 'Atacante', 'Atacante']}

POSICOES_CSS = {'4-4-2': ['top: 88%; left: 50%;', 'top: 68%; left: 15%;', 'top: 75%; left: 37%;', 'top: 75%; left: 63%;', 'top: 68%; left: 85%;', 'top: 48%; left: 18%;', 'top: 55%; left: 40%;', 'top: 55%; left: 60%;', 'top: 48%; left: 82%;', 'top: 25%; left: 40%;', 'top: 25%; left: 60%;'], '4-3-3': ['top: 88%; left: 50%;', 'top: 70%; left: 15%;', 'top: 78%; left: 37%;', 'top: 78%; left: 63%;', 'top: 70%; left: 85%;', 'top: 60%; left: 50%;', 'top: 45%; left: 35%;', 'top: 45%; left: 65%;', 'top: 20%; left: 20%;', 'top: 20%; left: 80%;', 'top: 15%; left: 50%;'], '4-2-3-1': ['top: 88%; left: 50%;', 'top: 70%; left: 15%;', 'top: 78%; left: 37%;', 'top: 78%; left: 63%;', 'top: 70%; left: 85%;', 'top: 60%; left: 40%;', 'top: 60%; left: 60%;', 'top: 40%; left: 50%;', 'top: 35%; left: 20%;', 'top: 35%; left: 80%;', 'top: 15%; left: 50%;'], '3-5-2': ['top: 88%; left: 50%;', 'top: 75%; left: 30%;', 'top: 80%; left: 50%;', 'top: 75%; left: 70%;', 'top: 45%; left: 15%;', 'top: 60%; left: 50%;', 'top: 45%; left: 35%;', 'top: 45%; left: 65%;', 'top: 45%; left: 85%;', 'top: 20%; left: 40%;', 'top: 20%; left: 60%;'], '5-3-2': ['top: 88%; left: 50%;', 'top: 75%; left: 20%;', 'top: 80%; left: 37%;', 'top: 80%; left: 63%;', 'top: 75%; left: 80%;', 'top: 45%; left: 15%;', 'top: 45%; left: 85%;', 'top: 55%; left: 50%;', 'top: 40%; left: 35%;', 'top: 40%; left: 65%;', 'top: 18%; left: 40%;', 'top: 18%; left: 60%;']}

def analisar_time(jogadores_escalados):
    """Calcula a força dos setores e o equilíbrio tático do time titular."""
    analise = {'forca_defesa': 0, 'forca_meio': 0, 'forca_ataque': 0, 'equilibrio': 'Equilibrado'}
    contagem = {'Defesa': 0, 'Meio-Campo': 0, 'Ataque': 0}
    if not jogadores_escalados: return analise
    for jogador in jogadores_escalados:
        setor = SETORES.get(jogador['posicao'], None)
        if setor:
            if setor == 'Defesa' or setor == 'Goleiro':
                analise['forca_defesa'] += jogador['overall']
                contagem['Defesa'] += 1
            elif setor == 'Meio-Campo':
                analise['forca_meio'] += jogador['overall']
                contagem['Meio-Campo'] += 1
            elif setor == 'Ataque':
                analise['forca_ataque'] += jogador['overall']
                contagem['Ataque'] += 1
    if contagem['Defesa'] > 0: analise['forca_defesa'] //= contagem['Defesa']
    if contagem['Meio-Campo'] > 0: analise['forca_meio'] //= contagem['Meio-Campo']
    if contagem['Ataque'] > 0: analise['forca_ataque'] //= contagem['Ataque']
    if analise['forca_ataque'] > analise['forca_defesa'] + 5: analise['equilibrio'] = 'Ofensivo'
    elif analise['forca_defesa'] > analise['forca_ataque'] + 5: analise['equilibrio'] = 'Defensivo'
    return analise

@route('/escalacao')
def escalacao():
    """Exibe a página principal de gerenciamento da escalação."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    with get_db_connection() as conn:
        time_db = conn.execute("SELECT * FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
        jogadores_disponiveis = conn.execute("SELECT * FROM jogadores WHERE time_id = ? AND status_lesao = 'Disponível' ORDER BY overall DESC", (time_db['id'],)).fetchall()
        titulares_db = conn.execute("SELECT * FROM jogadores WHERE time_id = ? AND status_escalacao = 'Titular'", (time_db['id'],)).fetchall()
    
    mapa_indice_jogador = {j['posicao_indice']: j for j in titulares_db}
    analise_time = analisar_time(titulares_db)
    
    return template('views/escalacao_view.tpl', 
                    time=time_db, 
                    jogadores=jogadores_disponiveis,
                    mapa_indice_jogador=mapa_indice_jogador,
                    formacoes=FORMACOES,
                    posicoes_css=POSICOES_CSS,
                    analise=analise_time)

@route('/escalacao/definir-formacao', method='POST')
def definir_formacao():
    """Define uma nova formação tática para o time e limpa a escalação atual."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    nova_formacao = request.forms.get('formacao')
    with get_db_connection() as conn:
        time_db = conn.execute("SELECT id FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
        conn.execute("UPDATE times SET formacao_atual = ? WHERE id = ?", (nova_formacao, time_db['id']))
        conn.execute("UPDATE jogadores SET status_escalacao = 'Reserva', posicao_indice = NULL WHERE time_id = ?", (time_db['id'],))
        conn.commit()
    redirect('/escalacao')

@route('/escalacao/salvar', method='POST')
def salvar_escalacao():
    """Salva a escalação definida pelo usuário no campo."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    
    selecoes = [request.forms.get(f'posicao_{i}') for i in range(11)]
    selecoes_validas = [s for s in selecoes if s]
    if len(selecoes_validas) != len(set(selecoes_validas)):
        return template('views/error.tpl', error_message="Erro: O mesmo jogador foi escalado em mais de uma posição.")

    with get_db_connection() as conn:
        time_db = conn.execute("SELECT * FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
        time_id = time_db['id']
        
        conn.execute("UPDATE jogadores SET status_escalacao = 'Reserva', posicao_indice = NULL WHERE time_id = ?", (time_id,))
        
        for i in range(11):
            jogador_id = request.forms.get(f'posicao_{i}')
            if jogador_id:
                conn.execute(
                    "UPDATE jogadores SET status_escalacao = 'Titular', posicao_indice = ? WHERE id = ? AND time_id = ?",
                    (i, jogador_id, time_id)
                )
        conn.commit()
        
    redirect('/escalacao')

@route('/escalacao/auto/<estilo>')
def auto_escalar(estilo):
    """Preenche a escalação automaticamente com base em um estilo de jogo."""
    user_id = get_current_user_id()
    if not user_id: redirect('/login')
    
    with get_db_connection() as conn:
        time_db = conn.execute("SELECT * FROM times WHERE usuario_id = ?", (user_id,)).fetchone()
        jogadores = conn.execute("SELECT * FROM jogadores WHERE time_id = ? AND status_lesao = 'Disponível'", (time_db['id'],)).fetchall()
    
    formacao = FORMACOES.get(time_db['formacao_atual'])
    if not formacao or not jogadores: redirect('/escalacao')

    jogadores_disponiveis = sorted(list(jogadores), key=lambda j: j['overall'], reverse=True)
    escalacao_final = {}
    ids_ja_usados = set()

    for i, pos_nome in enumerate(formacao):
        melhor_jogador = None
        for jogador in jogadores_disponiveis:
            if jogador['id'] not in ids_ja_usados and jogador['posicao'] == pos_nome:
                if not melhor_jogador or jogador['overall'] > melhor_jogador['overall']:
                    melhor_jogador = jogador
        
        if not melhor_jogador:
            setor_alvo = SETORES.get(pos_nome)
            for jogador in jogadores_disponiveis:
                if jogador['id'] not in ids_ja_usados and SETORES.get(jogador['posicao']) == setor_alvo:
                    if not melhor_jogador or jogador['overall'] > melhor_jogador['overall']:
                         melhor_jogador = jogador
        
        if not melhor_jogador:
            for jogador in jogadores_disponiveis:
                if jogador['id'] not in ids_ja_usados:
                    if not melhor_jogador or jogador['overall'] > melhor_jogador['overall']:
                        melhor_jogador = jogador
        
        if melhor_jogador:
            escalacao_final[i] = melhor_jogador['id']
            ids_ja_usados.add(melhor_jogador['id'])

    with get_db_connection() as conn:
        conn.execute("UPDATE jogadores SET status_escalacao = 'Reserva', posicao_indice = NULL WHERE time_id = ?", (time_db['id'],))
        for indice, jogador_id in escalacao_final.items():
            conn.execute("UPDATE jogadores SET status_escalacao = 'Titular', posicao_indice = ? WHERE id = ?", (indice, jogador_id))
        conn.commit()
        
    redirect('/escalacao')