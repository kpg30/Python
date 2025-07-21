
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
password_to_encrypt=b"abavdbsks"
token = f.encrypt(password_to_encrypt)
print(f"encrypt password : {token}")

decrypt_password = f.decrypt(token)
print(f"decrypt password : {decrypt_password}")
