% rebase('views/layout.tpl', title='Login')
<div class="container" style="max-width: 500px;">
  <h2>Login</h2>
  <form action="/login" method="post">
    <div class="mb-3">
      <label for="email" class="form-label">Email</label>
      <input type="email" class="form-control" id="email" name="email" required>
    </div>
    <div class="mb-3">
      <label for="senha" class="form-label">Senha</label>
      <input type="password" class="form-control" id="senha" name="senha" required>
    </div>
    <button type="submit" class="btn btn-success w-100">Entrar</button>
  </form>
  <div class="text-center mt-3">
    <a href="/register">Não tem uma conta? Registre-se</a>
  </div>
</div>