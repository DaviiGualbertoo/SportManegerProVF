% rebase('views/layout.tpl', title='Erro')

<div class="alert alert-danger" role="alert">
    <h4 class="alert-heading">Ocorreu um Erro!</h4>
    <p>{{ error_message }}</p>
    <hr>
    <p class="mb-0">
        <a href="javascript:history.back()" class="btn btn-primary">Voltar e Tentar Novamente</a>
    </p>
</div>