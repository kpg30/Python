
from getpass import getpass
from cryptography.fernet import Fernet
import logging

###########################################

format = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=format, datefmt=datefmt)
logger = logging.getLogger(__name__)

key = b'VtX1J5bX9Z3vQ8vL6H2jYkW8nF3pR9sT0uX5yZ7a8bE='  # Example key, replace with your own secure key


def encrypt_password(password: str) -> bytes:
    try:
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password.encode())
        return encrypted_password
    except Exception as e:
        logger.error(f"Encryption failed: {e}")
        raise

def decrypt_password(encrypted_password: bytes) -> str:
    try:
        fernet = Fernet(key)
        decrypted_password = fernet.decrypt(encrypted_password).decode()
        return decrypted_password
    except Exception as e:
        logger.error(f"Decryption failed: {e}")
        raise
