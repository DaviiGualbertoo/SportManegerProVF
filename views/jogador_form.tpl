%# Inclui o layout base (cabeçalho, rodapé, etc.)
% rebase('views/layout.tpl', title='Cadastrar Jogador')

<div class="container">
  <h2>Cadastrar Novo Jogador</h2>
  <form action="/jogadores/novo" method="post">
    <div class="mb-3">
      <label for="nome" class="form-label">Nome Completo</label>
      <input type="text" class="form-control" id="nome" name="nome" required>
    </div>
    <div class="mb-3">
      <label for="idade" class="form-label">Idade</label>
      <input type="number" class="form-control" id="idade" name="idade" required>
    </div>
    <div class="mb-3">
      <label for="posicao" class="form-label">Posição</label>
      <select class="form-select" id="posicao" name="posicao">
        <option value="Goleiro">Goleiro</option>
        <option value="Defensor">Defensor</option>
        <option value="Meio-campista">Meio-campista</option>
        <option value="Atacante">Atacante</option>
      </select>
    </div>
    <div class="row">
            <div class="col">
                <div class="mb-3">
                    <label for="altura" class="form-label">Altura (ex: 1.85)</label>
                    <input type="number" step="0.01" class="form-control" id="altura" name="altura">
                </div>
            </div>
            <div class="col">
                <div class="mb-3">
                    <label for="peso" class="form-label">Peso (kg)</label>
                    <input type="number" step="0.1" class="form-control" id="peso" name="peso">
                </div>
            </div>
    <div class="mb-3">
      <label for="overall" class="form-label">Overall (0-99)</label>
      <input type="number" class="form-control" id="overall" name="overall" min="0" max="99" required>
    </div>
    <div class="mb-3">
      <label for="valor_mercado" class="form-label">Valor de Mercado (€)</label>
      <input type="number" step="0.01" class="form-control" id="valor_mercado" name="valor_mercado" required>
    </div>
    <div class="mb-3">
        <label for="tipo" class="form-label">Categoria</label>
        <select class="form-select" id="tipo" name="tipo">
          <option value="Profissional">Profissional</option>
          <option value="Base">Base</option>
        </select>
    </div>
    <button type="submit" class="btn btn-primary">Salvar Jogador</button>
  </form>
</div>