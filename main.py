# main.py

# Importa as funções essenciais da biblioteca Bottle para rodar o servidor
from bottle import run, default_app, static_file, route
# Importa o arquivo de configurações, como a SECRET_KEY
import config

# Importa todos os nossos arquivos de controllers.
# É crucial que eles sejam importados aqui para que o Bottle "enxergue" as rotas (@route) definidas neles.
import controllers.usuario_controller
import controllers.time_controller 
import controllers.jogador_controller
import controllers.escalacao_controller

@route('/static/<filepath:path>')
def server_static(filepath):
    """
    Esta rota especial serve arquivos estáticos (CSS, JavaScript, Imagens).
    Tudo que estiver na pasta /static será acessível pela URL /static.
    Ex: /static/img/campo.jpg
    """
    return static_file(filepath, root='./static')

# Este bloco só é executado quando o arquivo main.py é rodado diretamente
if __name__ == '__main__':
    # Inicia o servidor web do Bottle
    run(host='localhost', port=8080, debug=True, reloader=True)
    # debug=True: Mostra erros detalhados no navegador.
    # reloader=True: Reinicia o servidor automaticamente quando um arquivo .py é salvo.

# Pega a aplicação padrão do Bottle para ser usada por servidores de produção (não usado aqui, mas é boa prática)
app = default_app()