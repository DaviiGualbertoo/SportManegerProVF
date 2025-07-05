% rebase('views/layout.tpl', title=jogador['nome'])

<div class="content-panel">
    <div class="card border-0 bg-transparent">
        <div class="card-header bg-transparent d-flex justify-content-between align-items-center">
            <h2>Ficha do Jogador</h2>
            <img src="{{jogador['foto_url']}}" alt="Foto de {{jogador['nome']}}" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover;">
        </div>
        <div class="card-body">
            <h3 class="card-title text-dark">{{ jogador['nome'] }}</h3>
            <div class="row">
                <div class="col-md-6">
                    <p><strong>Nacionalidade:</strong> {{ jogador['nacionalidade'] or 'Não informada' }}</p>
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
                        <strong>Status Clínico:</strong>
                        % if jogador['status_lesao'] == 'Lesionado':
                            <span class="badge bg-danger">Indisponível (Lesionado)</span>
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
        <div class="card-footer bg-transparent text-muted">
            <a href="/time" class="btn btn-secondary">Voltar para o Elenco</a>
        </div>
    </div>
</div>