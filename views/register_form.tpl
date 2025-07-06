% rebase('views/layout.tpl', title=' ')

<div class="container" style="max-width: 500px;">
  <div class="form-dark-theme">
    <h2 class="text-center">Crie sua Conta</h2>
    <form action="/register" method="post" enctype="multipart/form-data" accept-charset="UTF-8">
      <div class="mb-3">
        <label for="nome" class="form-label">Seu Nome Completo</label>
        <input type="text" class="form-control" id="nome" name="nome" required>
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" name="email" required>
      </div>
      <div class="mb-3">
        <label for="senha" class="form-label">Senha</label>
        <input type="password" class="form-control" id="senha" name="senha" required>
      </div>
      <hr style="border-top: 1px solid #495057;">
      <div class="mb-3">
        <label for="escudo" class="form-label">Escudo do Time (Opcional)</label>
        <input class="form-control" type="file" id="escudo" name="escudo" accept="image/*">
      </div>
      <div class="mb-3">
          <label for="orcamento_inicial" class="form-label">Orçamento Inicial (Opcional)</label>
          <input type="text" inputmode="decimal" class="form-control" id="orcamento_inicial" name="orcamento_inicial" placeholder="Ex: 10.000.000,00">
      </div>
      <button type="submit" class="btn btn-primary w-100">Registrar</button>
    </form>
    <div class="text-center mt-3">
      <a href="/login">Já tem uma conta? Faça login</a>
    </div>
  </div>
</div>