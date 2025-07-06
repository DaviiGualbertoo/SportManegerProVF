# auth.py
# Este arquivo é o nosso módulo de segurança.
# Ele centraliza toda a lógica de autenticação e sessão.

from bottle import request
from passlib.context import CryptContext # A biblioteca principal para hashing.
from database import get_db_connection
import config

# Configura o passlib para usar o algoritmo 'bcrypt', que é o padrão da indústria para hashing de senhas.
# Ele é lento de propósito, tornando ataques de força bruta muito mais difíceis.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Recebe uma senha em texto puro e retorna seu hash seguro."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Compara uma senha em texto com um hash salvo no banco.
    Retorna True se a senha for correta, False caso contrário.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user_id():
    """
    Verifica se existe um cookie de sessão válido na requisição do navegador.
    Esta é a função que "sabe" se o usuário está logado ou não.
    """
    # Lê o cookie 'user_id' do navegador.
    # A 'secret' é usada para verificar a assinatura digital do cookie e garantir que ele não foi adulterado.
    return request.get_cookie("user_id", secret=config.SECRET_KEY)