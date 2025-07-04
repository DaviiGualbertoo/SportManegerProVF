from passlib.context import CryptContext
from bottle import request
from database import get_db_connection
import config

# Configura o passlib para usar o algoritmo bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    """Transforma a senha em um hash."""
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    """Verifica se a senha digitada corresponde ao hash salvo."""
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user_id():
    """Lê o cookie e retorna o ID do usuário, se houver."""
    return request.get_cookie("user_id", secret=config.SECRET_KEY)