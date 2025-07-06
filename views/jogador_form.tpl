% rebase('views/layout.tpl', title='Cadastrar Jogador')

<div class="container" style="max-width: 700px;">
  <div class="form-dark-theme">
    <h2 class="text-center">Cadastrar Novo Jogador</h2>
    <form action="/jogadores/novo" method="post" enctype="multipart/form-data" accept-charset="UTF-8">
      <div class="mb-3"><label for="nome" class="form-label">Nome Completo</label><input type="text" class="form-control" id="nome" name="nome" required></div>
      <div class="mb-3"><label for="foto" class="form-label">Foto do Jogador (Opcional)</label><input class="form-control" type="file" id="foto" name="foto" accept="image/*"></div>
      <div class="row">
          <div class="col-md-6 mb-3"><label for="idade" class="form-label">Idade</label><input type="number" class="form-control" id="idade" name="idade" required></div>
          <div class="col-md-6 mb-3"><label for="nacionalidade" class="form-label">Nacionalidade</label><input type="text" class="form-control" id="nacionalidade" name="nacionalidade"></div>
      </div>
      <div class="mb-3">
        <label for="posicao" class="form-label">Posição Principal</label>
        <select class="form-select" id="posicao" name="posicao">
          <option value="Goleiro">Goleiro</option><option value="Zagueiro">Zagueiro</option><option value="Lateral Direito">Lateral Direito</option><option value="Lateral Esquerdo">Lateral Esquerdo</option><option value="Volante">Volante</option><option value="Meia Central">Meia Central</option><option value="Meia Ofensivo">Meia Ofensivo</option><option value="Ponta Direita">Ponta Direita</option><option value="Ponta Esquerda">Ponta Esquerda</option><option value="Centroavante">Centroavante</option>
        </select>
      </div>
      <div class="row">
          <div class="col-md-6 mb-3"><label for="altura" class="form-label">Altura (ex: 1,85)</label><input type="text" inputmode="decimal" class="form-control" id="altura" name="altura"></div>
          <div class="col-md-6 mb-3"><label for="peso" class="form-label">Peso (kg)</label><input type="text" inputmode="decimal" class="form-control" id="peso" name="peso"></div>
      </div>
      <div class="mb-3"><label for="overall" class="form-label">Overall (0-99)</label><input type="number" class="form-control" id="overall" name="overall" min="0" max="99" required></div>
      <div class="mb-3">
        <label for="valor_mercado" class="form-label">Valor de Mercado (€)</label>
        <input type="text" inputmode="decimal" class="form-control" id="valor_mercado" name="valor_mercado" required>
      </div>
      <div class="mb-3">
          <label for="tipo" class="form-label">Categoria</label>
          <select class="form-select" id="tipo" name="tipo"><option value="Profissional">Profissional</option><option value="Base">Base</option></select>
      </div>
      <button type="submit" class="btn btn-primary w-100">Salvar Jogador</button>
    </form>
  </div>
</div>