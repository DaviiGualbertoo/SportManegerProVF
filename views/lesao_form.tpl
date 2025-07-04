% rebase('views/layout.tpl', title='Registrar Lesão')

<div class="container">
  <h2>Registrar Lesão para: {{ jogador['nome'] }}</h2>

  <form action="/jogador/lesao/{{ jogador['id'] }}" method="post">
    <div class="mb-3">
      <label for="tipo_lesao" class="form-label">Tipo de Lesão</label>
      <select class="form-select" id="tipo_lesao" name="tipo_lesao">
        <option value="Leve">Leve</option>
        <option value="Moderada">Moderada</option>
        <option value="Grave">Grave</option>
      </select>
    </div>
    <div class="mb-3">
      <label for="tempo_recuperacao" class="form-label">Tempo de Recuperação (em dias)</label>
      <input type="number" class="form-control" id="tempo_recuperacao" name="tempo_recuperacao" required min="1">
    </div>

    <button type="submit" class="btn btn-primary">Salvar Lesão</button>
    <a href="/time" class="btn btn-secondary">Cancelar</a>
  </form>
</div>