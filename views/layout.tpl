<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SportManager Pro - {{title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-image: url('/static/img/fundo_estadio.png');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        /* --- ESTILO FINAL DA FAIXA DO TOPO --- */
        .app-header {
            background-color: #1a2f44;
            height: 90px;
            padding: 0 25px;
            display: flex;
            align-items: center;
            justify-content: center; /* Centraliza o conteúdo principal */
            position: relative;
            border-bottom: 3px solid #102233;
            margin-bottom: 2rem;
        }

        .header-brand-link {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: white;
        }

        .header-icon {
            /* Aumentamos a logo para ficar proporcional ao texto */
            height: 100px; 
            width: auto;
            margin-right: 15px;
        }
        
        .header-title-text {
            font-size: 2rem; /* Aumentamos um pouco o texto para acompanhar a logo */
            font-weight: bold;
        }

        .logout-button-container {
            position: absolute; /* Posição absoluta em relação ao header */
            right: 25px; /* Alinha à direita */
        }
        
        /* --- ESTILO PARA CONTEÚDO E FORMULÁRIOS (CORRIGIDO) --- */
        main.container {
            padding-top: 1rem;
        }

        .content-panel {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: .5rem;
            padding: 2rem;
        }

        h2.page-title {
            color: white;
            text-shadow: 2px 2px 4px black;
        }

        .form-dark-theme {
            background-color: #212529;
            color: #f8f9fa;
            border-radius: .5rem;
            padding: 2rem;
        }
        .form-dark-theme .form-label, .form-dark-theme h2 {
            color: #f8f9fa;
            text-shadow: none;
        }
        .form-dark-theme .form-control, .form-dark-theme .form-select {
            background-color: #343a40;
            color: #fff;
            border-color: #495057;
        }
        .form-dark-theme .form-control:focus, .form-dark-theme .form-select:focus {
            background-color: #343a40;
            color: #fff;
            border-color: #80bdff;
        }
        .form-dark-theme a { color: #3b82f6; }
    </style>
</head>
<body>

  <header class="app-header">
    <a href="/time" class="header-brand-link">
        <img src="/static/img/icone_logo.png" alt="Logo" class="header-icon">
        <span class="header-title-text">SportManager Pro</span>
    </a>
    
    <div class="logout-button-container">
        % from auth import get_current_user_id
        % if get_current_user_id():
            <a class="btn btn-outline-light" href="/logout">Sair</a>
        % end
    </div>
  </header>

  <main class="container">
    <h2 class="page-title text-center mb-4">{{title}}</h2>
    {{!base}}
  </main>

  <footer class="text-center mt-auto py-3" style="color: #ccc; text-shadow: 1px 1px 2px black;">
    <p>&copy; 2025 SportManager Pro.</p>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>