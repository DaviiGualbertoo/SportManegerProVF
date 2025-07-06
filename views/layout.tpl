<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SportManager Pro - {{title}}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Estilos globais aplicados a todas as páginas */
        body {
            background-image: url('/static/img/fundo_estadio.png');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }

        .app-header {
            background-color: #1a2f44;
            height: 90px;
            padding: 0 25px;
            display: flex;
            align-items: center;
            border-bottom: 3px solid #102233;
            margin-bottom: 2rem;
        }

        .header-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .header-brand-link {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: white;
        }

        .header-icon {
            height: 55px;
            width: auto;
            margin-right: 15px;
        }
        
        .header-title-text {
            font-size: 2rem;
            font-weight: bold;
        }

        .logout-button-container {
            position: relative;
        }
        
        main.container {
            padding-top: 1rem;
        }

        /* Classe para painéis com fundo branco (páginas de conteúdo) */
        .content-panel {
            background-color: rgba(255, 255, 255, 0.95);
            border-radius: .5rem;
            padding: 2rem;
        }

        /* Título da página (que fica sobre o fundo do estádio) */
        h2.page-title {
            color: white;
            text-shadow: 2px 2px 4px black;
        }

        /* Tema escuro para os formulários */
        .form-dark-theme {
            background-color: #212529;
            color: #f8f9fa;
            border-radius: .5rem;
            padding: 2rem;
        }
        .form-dark-theme .form-label, .form-dark-theme h2 {
            color: #f8f9fa; text-shadow: none;
        }
        .form-dark-theme .form-control, .form-dark-theme .form-select {
            background-color: #343a40; color: #fff; border-color: #495057;
        }
        .form-dark-theme .form-control:focus, .form-dark-theme .form-select:focus {
            background-color: #343a40; color: #fff; border-color: #80bdff;
        }
        .form-dark-theme a { color: #3b82f6; }
    </style>
</head>
<body>

  <header class="app-header">
    <div class="container-fluid header-content">
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