% rebase('views/layout.tpl', title='Elenco Principal')

<div class="content-panel">
    <div class="card mb-4 bg-transparent border-0">
        <div class="card-body">
            <div class="d-flex align-items-center mb-3">
                <img src="{{time.escudo_url}}" alt="Escudo do time" style="width: 100px; height: 100px; object-fit: cover; margin-right: 20px; border-radius: 50%;">
                <div>
                    <h2 class="card-title text-dark">{{ time.nome }}</h2>
                    <p class="card-text mb-1 text-muted">Orçamento: € {{ "{:,.2f}".format(time.get_orcamento()) }}</p>
                    <p class="card-text text-muted"><strong>Força Média do Time: {{ forca_time }}</strong></p>
                </div>
            </div>
            <hr>
            <div class="row">
                <div class="col-md-4 mb-3">
                     <form action="/time/renomear" method="post">
                        <label class="form-label"><strong>Renomear Time:</strong></label>
                        <div class="input-group"><input type="text" class="form-control" name="nome" placeholder="Novo nome" required><button class="btn btn-outline-secondary" type="submit">OK</button></div>
                    </form>
                </div>
                <div class="col-md-4 mb-3">
                    <form action="/time/upload-escudo" method="post" enctype="multipart/form-data">
                        <label class="form-label"><strong>Alterar Escudo:</strong></label>
                        <div class="input-group"><input type="file" class="form-control" name="escudo" required><button class="btn btn-outline-secondary" type="submit">Enviar</button></div>
                    </form>
                </div>
                <div class="col-md-4 mb-3">
                    <form action="/time/orcamento" method="post">
                        <label class="form-label"><strong>Gerenciar Verba:</strong></label>
                        <div class="input-group"><input type="text" inputmode="decimal" class="form-control" name="valor" placeholder="Valor" required><button type="submit" name="action" value="add" class="btn btn-outline-success" title="Adicionar">+</button><button type="submit" name="action" value="remove" class="btn btn-outline-danger" title="Remover">-</button></div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <div class="d-flex justify-content-between align-items-center mb-3">
        <h3 class="text-dark">Elenco</h3>
        <div>
            <a href="/escalacao" class="btn btn-info">Gerenciar Escalação</a>
            <a href="/jogadores/novo" class="btn btn-primary">Adicionar Jogador</a>
        </div>
    </div>
    <table class="table table-striped table-hover align-middle">
        <thead>
            <tr><th>Foto</th><th>Nome</th><th>Posição</th><th>Overall</th><th>Status Tático</th><th>Status Clínico</th><th>Ações</th></tr>
        </thead>
        <tbody>
            % for jogador in jogadores:
            <tr>
                <td><img src="{{jogador.foto_url}}" alt="Foto de {{jogador.nome}}" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"></td>
                <td><a href="/jogador/{{jogador.id}}">{{ jogador.nome }}</a></td>
                <td>{{ jogador.posicao }}</td>
                <td><span class="badge bg-primary">{{ jogador.overall }}</span></td>
                <td>
                    % if jogador.status_escalacao == 'Titular':
                        <span class="badge bg-dark">Titular</span>
                    % else:
                        <span class="badge bg-secondary">Reserva</span>
                    % end
                </td>
                <td>
                    % if jogador.status_lesao == 'Lesionado':
                        <span class="badge bg-danger">Indisponível</span>
                    % else:
                        <span class="badge bg-success">Disponível</span>
                    % end
                </td>
                <td>
                    <a href="/jogador/editar/{{jogador.id}}" class="btn btn-secondary btn-sm" title="Editar">Editar</a>
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