% rebase('views/layout.tpl', title='Editar Jogador')

<div class="container" style="max-width: 700px;">
  <div class="form-dark-theme">
    <h2 class="text-center">Editando: {{jogador['nome']}}</h2>
    
    <div class="text-center my-3">
        <img src="{{jogador['foto_url']}}" alt="Foto de {{jogador['nome']}}" style="width: 100px; height: 100px; border-radius: 50%; object-fit: cover; border: 3px solid #495057;">
    </div>

    <form action="/jogador/editar/{{jogador['id']}}" method="post" enctype="multipart/form-data" accept-charset="UTF-8">
      
      <div class="mb-3">
        <label for="nome" class="form-label">Nome Completo</label>
        <input type="text" class="form-control" id="nome" name="nome" value="{{jogador['nome']}}" required>
      </div>

      <div class="mb-3">
          <label for="foto" class="form-label">Alterar Foto (Opcional)</label>
          <input class="form-control" type="file" id="foto" name="foto" accept="image/*">
      </div>

      <div class="row">
          <div class="col-md-6 mb-3">
              <label for="idade" class="form-label">Idade</label>
              <input type="number" class="form-control" id="idade" name="idade" value="{{jogador['idade']}}" required>
          </div>
          <div class="col-md-6 mb-3">
              <label for="nacionalidade" class="form-label">Nacionalidade</label>
              <input type="text" class="form-control" id="nacionalidade" name="nacionalidade" value="{{jogador['nacionalidade']}}">
          </div>
      </div>

      <div class="mb-3">
        <label for="posicao" class="form-label">Posição Principal</label>
        <select class="form-select" id="posicao" name="posicao">
          % posicoes = ["Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo", "Volante", "Meia Central", "Meia Ofensivo", "Ponta Direita", "Ponta Esquerda", "Centroavante"]
          % for p in posicoes:
            <option value="{{p}}" {{'selected' if p == jogador['posicao'] else ''}}>{{p}}</option>
          % end
        </select>
      </div>

      <div class="row">
          <div class="col-md-6 mb-3">
              <label for="altura" class="form-label">Altura (ex: 1,85)</label>
              <input type="text" inputmode="decimal" class="form-control" id="altura" name="altura" value="{{jogador['altura']}}">
          </div>
          <div class="col-md-6 mb-3">
              <label for="peso" class="form-label">Peso (kg)</label>
              <input type="text" inputmode="decimal" class="form-control" id="peso" name="peso" value="{{jogador['peso']}}">
          </div>
      </div>

      <div class="mb-3">
        <label for="overall" class="form-label">Overall (0-99)</label>
        <input type="number" class="form-control" id="overall" name="overall" min="0" max="99" value="{{jogador['overall']}}" required>
      </div>

      <div class="mb-3">
        <label for="valor_mercado" class="form-label">Valor de Mercado (€)</label>
        <input type="text" inputmode="decimal" class="form-control" id="valor_mercado" name="valor_mercado" value="{{ '{:_.2f}'.format(jogador['valor_mercado']).replace('.', ',').replace('_', '.') }}" required>
      </div>
      
      <div class="d-grid gap-2">
        <button type="submit" class="btn btn-primary">Salvar Alterações</button>
        <a href="/time" class="btn btn-secondary">Cancelar</a>
      </div>
    </form>
  </div>
</div>