import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.exceptions import InvalidTag

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path: str, password: str, output_path: str):
    try:
        salt = os.urandom(16)
        iv = os.urandom(16)
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        with open(file_path, 'rb') as f:
            plaintext = f.read()

        padded_data = PKCS7(128).padder().update(plaintext) + PKCS7(128).padder().finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()

        with open(output_path, 'wb') as f:
            f.write(salt + iv + encryptor.tag + ciphertext)
        print(f"File encrypted successfully: {output_path}")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decrypt_file(file_path: str, password: str, output_path: str):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        salt, iv, tag, ciphertext = data[:16], data[16:32], data[32:48], data[48:]
        key = derive_key(password, salt)
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        plaintext = PKCS7(128).unpadder().update(padded_data) + PKCS7(128).unpadder().finalize()

        with open(output_path, 'wb') as f:
            f.write(plaintext)
        print(f"File decrypted successfully: {output_path}")
    except InvalidTag:
        print("Decryption failed: Invalid password or corrupted file.")
    except Exception as e:
        print(f"Decryption failed: {e}")
