% rebase('views/layout.tpl', title=jogador['nome'])

<div class="container">
    <div class="card">
        <div class="card-header">
            <h2>Ficha do Jogador</h2>
        </div>
        <div class="card-body">
            <h3 class="card-title">{{ jogador['nome'] }}</h3>
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Posição:</strong> {{ jogador['posicao'] }}</p>
                    <p><strong>Idade:</strong> {{ jogador['idade'] }} anos</p>
                    <p><strong>Altura:</strong> {{ jogador['altura'] or 'Não informado' }} m</p>
                    <p><strong>Peso:</strong> {{ jogador['peso'] or 'Não informado' }} kg</p>
                </div>
                <div class="col-md-6">
                    <p><strong>Overall:</strong> <span class="badge bg-primary fs-6">{{ jogador['overall'] }}</span></p>
                    <p><strong>Valor de Mercado:</strong> € {{ "{:,.2f}".format(jogador['valor_mercado']) }}</p>
                    <p><strong>Categoria:</strong> {{ 'Profissional' if jogador['tipo'] == 'Profissional' else 'Jogador da Base' }}</p>
                    <p>
                        <strong>Status:</strong>
                        % if jogador['status_lesao'] == 'Lesionado':
                            <span class="badge bg-danger">Lesionado</span>
                        % else:
                            <span class="badge bg-success">Disponível</span>
                        % end
                    </p>
                </div>
            </div>

            % if jogador['status_lesao'] == 'Lesionado':
            <div class="alert alert-warning mt-3">
                <h5 class="alert-heading">Detalhes da Lesão</h5>
                <p><strong>Tipo:</strong> {{ jogador['tipo_lesao'] }}</p>
                <p><strong>Tempo de Recuperação Estimado:</strong> {{ jogador['tempo_recuperacao'] }} dias</p>
            </div>
            % end

        </div>
        <div class="card-footer text-muted">
            <a href="/time" class="btn btn-secondary">Voltar para o Elenco</a>
        </div>
    </div>
</div>