% rebase('views/layout.tpl', title='Registrar Lesão')

<div class="container" style="max-width: 600px;">
  <div class="form-dark-theme">
    <h2 class="text-center">Registrar Lesão para: {{ jogador['nome'] }}</h2>
    <form action="/jogador/lesao/{{ jogador['id'] }}" method="post" accept-charset="UTF-8">
      <div class="mb-3">
        <label for="tipo_lesao" class="form-label">Tipo de Lesão</label>
        <select class="form-select" id="tipo_lesao" name="tipo_lesao"><option value="Leve">Leve</option><option value="Moderada">Moderada</option><option value="Grave">Grave</option></select>
      </div>
      <div class="mb-3">
        <label for="tempo_recuperacao" class="form-label">Tempo de Recuperação (em dias)</label>
        <input type="number" class="form-control" id="tempo_recuperacao" name="tempo_recuperacao" required min="1">
      </div>
      <button type="submit" class="btn btn-primary">Registrar Lesão</button>
      <a href="/time" class="btn btn-secondary">Cancelar</a>
    </form>
  </div>
</div>