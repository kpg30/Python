import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def pad(data_to_pad):
    return data_to_pad + b"\0" * (AES.block_size - len(data_to_pad) % AES.block_size)

def aes_encrypt(key, message):
    message = pad(bytes(message, 'utf-8'))
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(bytes(key, 'utf-8'), AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(message)).decode('utf-8')

def aes_decrypt(key, ciphertext):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(bytes(key, 'utf-8'), AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0").decode('utf-8')

from pyspark.sql import functions as F
def udf_encrypt(key):
    return F.udf(lambda text: aes_encrypt(key, text))


def udf_decrypt(key):
    return F.udf(lambda text: aes_decrypt(key, text))

key = 'abcdefghijklmnop'
input_data = 'prasad karupothula'

encrypt_data = aes_encrypt(key, input_data)
print(f"encrypt data : {encrypt_data}")

decrypt_data = aes_decrypt(key, encrypt_data)
print(f"decrypt data : {decrypt_data}")