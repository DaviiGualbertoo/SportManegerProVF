<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SportManager Pro - Registrar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>

% rebase('views/layout.tpl', title='Registrar')
<div class="container" style="max-width: 500px;">
  <h2>Crie sua Conta</h2>
  <form action="/register" method="post">
    <div class="mb-3">
      <label for="nome" class="form-label">Nome Completo</label>
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

    <div class="mb-3">
        <label for="orcamento_inicial" class="form-label">Orçamento Inicial (Opcional)</label>
        <input type="number" step="1000" class="form-control" id="orcamento_inicial" name="orcamento_inicial" placeholder="Ex: 10000000">
        <div class="form-text">
            Se deixado em branco, o valor padrão será de € 5,000,000.00.
        </div>
    </div>
    <button type="submit" class="btn btn-primary w-100">Registrar</button>
  </form>
  <div class="text-center mt-3">
    <a href="/login">Já tem uma conta? Faça login</a>
  </div>
</div>

</body>
</html>