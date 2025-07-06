# main.py
# Este é o ponto de entrada da nossa aplicação. É o arquivo que executamos para ligar o servidor.

# Importa as funções essenciais da biblioteca Bottle.
from bottle import run, default_app, static_file, route
# Importa o arquivo de configurações, como a SECRET_KEY.
import config

# Importa todos os nossos arquivos de controllers.
# Esta etapa é crucial para que o Bottle "enxergue" e registre todas as rotas (@route)
# que definimos em cada um desses arquivos. Se um controller não for importado aqui,
# suas páginas não funcionarão.
import controllers.usuario_controller
import controllers.time_controller 
import controllers.jogador_controller
import controllers.escalacao_controller

@route('/static/<filepath:path>')
def server_static(filepath):
    """
    Esta rota especial é responsável por servir arquivos estáticos.
    Qualquer URL que comece com /static/ (ex: /static/img/campo.jpg)
    será tratada por esta função, que busca o arquivo correspondente na pasta './static'.
    """
    return static_file(filepath, root='./static')

# Este bloco só é executado quando rodamos o comando "python main.py" no terminal.
if __name__ == '__main__':
    # A função run inicia o servidor web do Bottle.
    run(
        host='localhost',    # O servidor só será acessível no seu próprio computador.
        port=8080,           # A porta que o servidor vai "escutar". Acesse no navegador como http://localhost:8080
        debug=True,          # Modo de depuração: mostra erros detalhados no navegador, facilitando o desenvolvimento.
        reloader=True        # Recarregador automático: reinicia o servidor toda vez que um arquivo .py é salvo.
    )

# Pega a aplicação padrão do Bottle para ser usada por servidores de produção.
app = default_app()