% rebase('views/layout.tpl', title=time.nome)

<div class="container">
    <div class="card mb-4">
        <div class="card-body">
            <h2 class="card-title">{{ time.nome }}</h2>
            <p class="card-text">Orçamento: € {{ "{:,.2f}".format(time.get_orcamento()) }}</p>
            <p class="card-text"><strong>Força Média do Time: {{ forca_time }}</strong></p>

            <hr>
            <form action="/time/renomear" method="post" class="row g-3 align-items-center mb-3">
                <div class="col-auto">
                    <input type="text" class="form-control" name="novo_nome" placeholder="Novo nome para o time" required>
                </div>
                <div class="col-auto">
                    <button type="submit" class="btn btn-secondary">Renomear</button>
                </div>
            </form>

            <form action="/time/orcamento" method="post" class="row g-3 align-items-center">
                <div class="col-auto">
                    <input type="number" class="form-control" name="valor" placeholder="Valor" required>
                </div>
                <div class="col-auto">
                    <button type="submit" name="action" value="add" class="btn btn-success">Adicionar Verba</button>
                </div>
                <div class="col-auto">
                    <button type="submit" name="action" value="remove" class="btn btn-warning">Remover Verba</button>
                </div>
            </form>
        </div>
    </div>

    <div class="d-flex justify-content-between align-items-center mb-3">
        <h3>Elenco</h3>
        <a href="/jogadores/novo" class="btn btn-primary">Adicionar Jogador</a>
    </div>

    <table class="table table-striped table-hover">
        <thead>
            <tr>
                <th>Nome</th>
                <th>Posição</th>
                <th>Idade</th>
                <th>Overall</th>
                <th>Status</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            % for jogador in jogadores:
            <tr>
                <td><a href="/jogador/{{jogador.id}}">{{ jogador.nome }}</a></td>
                <td>{{ jogador.posicao }}</td>
                <td>{{ jogador.idade }}</td>
                <td><span class="badge bg-info">{{ jogador.overall }}</span></td>
                
                <td>
                    % if jogador.status_lesao == 'Lesionado':
                        <span class="badge bg-danger">Indisponível (Lesionado)</span>
                    % else:
                        <span class="badge bg-success">Disponível</span>
                    % end
                    <br>
                    <small class="text-muted">{{ jogador.descrever_status() }}</small>
                </td>
                <td>
                    <a href="/jogador/vender/{{jogador.id}}" class="btn btn-danger btn-sm" title="Vender">Vender</a>
                    <a href="/jogador/lesao/{{jogador.id}}" class="btn btn-warning btn-sm" title="Registrar Lesão">Lesão</a>
                    % if jogador.descrever_status() == 'Jogador da Base':
                        <a href="/jogador/promover/{{jogador.id}}" class="btn btn-success btn-sm" title="Promover">Promover</a>
                    % end
                </td>
            </tr>
            % end
        </tbody>
    </table>
</div>