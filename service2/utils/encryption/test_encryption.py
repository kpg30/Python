from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes 
from typing import Optional
import base64
import json

AES_BLOCK_SIZE = 32

def encrypt_data(data: str, secret_key: str) -> str:
    """
    Encrypts a string using AES-256-CBC.
    
    Args:
        data: Input string (JSON-serialized DataFrame)
        secret_key: String key (padded/truncated to 32 bytes)
    
    Returns:
        Base64-encoded encrypted string (IV + ciphertext)
    """
    try:
        key_bytes = secret_key.encode('utf-8')
        iv = get_random_bytes(16)
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        padded_data = pad(data.encode('utf-8'), AES_BLOCK_SIZE)
        encrypted = cipher.encrypt(padded_data)
        prepend_iv = iv + encrypted
        results = base64.b64encode(prepend_iv).decode('utf-8')
        
        return results
    
    except Exception as e:
        print(f"Encryption error: {str(e)}")
        exit(1)

def decrypt_data(encrypted_data: str, secret_key: str) -> Optional[str]:
    """
    Decrypts a base64-encoded string to restore the original JSON string.
    
    Args:
        encrypted_data: Base64-encoded encrypted string (IV + ciphertext)
        secret_key: String key (padded/truncated to 32 bytes)
    
    Returns:
        Decrypted JSON string
    """
    try:
        key_bytes = secret_key.encode('utf-8')
        encrypted_bytes = base64.b64decode(encrypted_data)
        iv = encrypted_bytes[:16]
        ciphertext = encrypted_bytes[16:]
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        decrypted_bytes = unpad(cipher.decrypt(ciphertext), AES_BLOCK_SIZE)
        results = decrypted_bytes.decode('utf-8')
        
        return results
    
    except Exception as e:
        print(f"Decryption error: {str(e)}")
        exit(1)
   
if __name__ == "__main__":
    
    message = "Prasad Karupothula!"
    secret_key = 'my32charsecretkey1234567890abcde'
    print(f"Secret_key Length : {len(secret_key)}")
    if len(secret_key) not in (16, 32):
        raise ValueError("Secret_key must be in 16, 32 long.")
    
    encrypt_op = encrypt_data(message, secret_key)
    print(f"Encrypt data : {encrypt_op}")
    
    decrypt_op = decrypt_data(encrypt_op, secret_key)
    print(f"Decrypt data : {decrypt_op}")

    from pyspark.sql import SparkSession
    # Initialize Spark session
    spark = SparkSession.builder.appName("DataFrameEncryption").getOrCreate()
    
    # Create sample data and save as Parquet
    data = [("John", "123-45-6789"), ("Jane", "987-65-4321")]
    df = spark.createDataFrame(data, ["name", "ssn"])
    df.show()
    df.write.mode("overwrite").parquet("sample_data.parquet")