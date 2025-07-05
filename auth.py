# auth.py
from bottle import request
from passlib.context import CryptContext
from database import get_db_connection
import config

# Configura o passlib para usar o algoritmo 'bcrypt', que é o padrão de mercado para hashing de senhas.
# Ele é lento de propósito para dificultar ataques.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Recebe uma senha em texto e retorna seu hash."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """
    Verifica se uma senha em texto corresponde a um hash salvo.
    Retorna True se corresponder, False caso contrário.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user_id():
    """
    Lê o cookie de sessão do navegador, verifica sua assinatura com a SECRET_KEY
    e retorna o ID do usuário se a sessão for válida.
    """
    return request.get_cookie("user_id", secret=config.SECRET_KEY)