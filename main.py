# main.py
from bottle import run, default_app
import config # Mantém as configurações

# Importe todos os seus controllers aqui para que as rotas sejam registradas
import controllers.jogador_controller
import controllers.time_controller 
import controllers.usuario_controller
# import controllers.usuario_controller # quando você criar

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)

app = default_app()