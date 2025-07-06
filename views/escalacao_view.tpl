% rebase('views/layout.tpl', title='Gerenciar Escalação')

<style>
  /* --- ESTILOS PARA O PAINEL DE CONTROLE --- */
  .escalacao-controles {
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: .5rem;
    padding: 1.5rem;
    margin-bottom: 2rem;
  }
  .escalacao-controles h2, .escalacao-controles strong {
    color: #212529; text-shadow: none;
  }

  /* --- ESTILOS PARA O CAMPO DE FUTEBOL E JOGADORES --- */
  .campo-futebol {
    background-image: url('/static/img/campo.jpg');
    background-size: cover;
    background-position: center;
    border: 2px solid #1a531d;
    height: 700px;
    width: 100%;
    position: relative;
    border-radius: 10px;
    color: white;
    text-shadow: 1px 1px 2px black;
  }
  .posicao-marcador {
    position: absolute;
    transform: translateX(-50%);
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .foto-jogador-escalacao {
      width: 50px; height: 50px;
      border-radius: 50%; object-fit: cover;
      border: 2px solid #fff; margin-bottom: 5px;
      background-color: #555;
  }
  .posicao-nome {
    font-weight: bold; font-size: 0.9rem;
    background-color: rgba(0, 0, 0, 0.6);
    padding: 2px 5px; border-radius: 3px;
    margin-bottom: 5px;
  }
  .posicao-marcador select {
    width: 180px; font-size: 0.8rem;
    text-align: center; border-radius: 5px;
  }
</style>

<div class="escalacao-controles">
    <div class="d-flex justify-content-between align-items-center mb-3">
        <h2>Gerenciar Escalação</h2>
        <a href="/time" class="btn btn-secondary">Voltar para o Elenco</a>
    </div>

    <div class="card mb-3">
        <div class="card-body">
            <div class="row align-items-center">
                <div class="col-lg-4 mb-3 mb-lg-0">
                    <form action="/escalacao/definir-formacao" method="post" class="d-flex">
                        <label for="formacao" class="form-label me-2 my-auto"><strong>Formação:</strong></label>
                        <select class="form-select" id="formacao" name="formacao">
                            % for f in formacoes:
                                <option value="{{f}}" {{'selected' if f == time['formacao_atual'] else ''}}>{{f}}</option>
                            % end
                        </select>
                        <button class="btn btn-primary ms-2" type="submit">Aplicar</button>
                    </form>
                </div>
                <div class="col-lg-8">
                    <strong>Análise do Time Titular:</strong>
                    <div class="d-flex flex-wrap justify-content-around text-center">
                        <span class="mx-2">Defesa: <span class="badge bg-primary fs-6">{{analise['forca_defesa']}}</span></span>
                        <span class="mx-2">Meio-Campo: <span class="badge bg-primary fs-6">{{analise['forca_meio']}}</span></span>
                        <span class="mx-2">Ataque: <span class="badge bg-primary fs-6">{{analise['forca_ataque']}}</span></span>
                        <span class="mx-2">Equilíbrio: <span class="badge bg-info fs-6">{{analise['equilibrio']}}</span></span>
                    </div>
                </div>
            </div>
            <hr>
            <div>
                <strong>Preencher Automaticamente:</strong><br>
                <a href="/escalacao/auto/defensivo" class="btn btn-secondary btn-sm mt-2">Time Defensivo</a>
                <a href="/escalacao/auto/equilibrado" class="btn btn-success btn-sm mt-2">Time Equilibrado</a>
                <a href="/escalacao/auto/ofensivo" class="btn btn-danger btn-sm mt-2">Time Ofensivo</a>
            </div>
        </div>
    </div>
</div>

<form action="/escalacao/salvar" method="post">
    <div class="campo-futebol mb-3">
        % formacao_atual = time['formacao_atual']
        % posicoes_formacao = formacoes.get(formacao_atual, [])
        % posicoes_css_lista = posicoes_css.get(formacao_atual, [])
        % for i, nome_posicao in enumerate(posicoes_formacao):
            <div class="posicao-marcador" style="{{posicoes_css_lista[i]}}">
                % # Pega o jogador que foi salvo neste índice de posição (ex: índice 0 = Goleiro)
                % jogador_atual = mapa_indice_jogador.get(i)
                
                <img src="{{ jogador_atual['foto_url'] if jogador_atual else '/static/img/jogador_padrao.png' }}" class="foto-jogador-escalacao" alt="Foto do jogador">
                
                <div class="posicao-nome">{{nome_posicao}}</div>
                
                <select name="posicao_{{i}}" class="form-select form-select-sm">
                    <option value="">-- Vazio --</option>
                    % for jogador in jogadores:
                        <option value="{{jogador['id']}}" {{'selected' if jogador_atual and jogador_atual['id'] == jogador['id'] else ''}}>
                            {{jogador['nome']}} ({{jogador['posicao']}}) - {{jogador['overall']}}
                        </option>
                    % end
                </select>
            </div>
        % end
    </div>
    <button type="submit" class="btn btn-success w-100 mb-4">Salvar Escalação</button>
</form>