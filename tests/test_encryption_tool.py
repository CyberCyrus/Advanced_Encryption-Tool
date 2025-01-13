import os
from encryption_tool.encryption_tool import encrypt_file, decrypt_file

def test_encryption_decryption():
    password = "strongpassword"
    plaintext = b"Hello, this is a test."

    input_file = "test_input.txt"
    encrypted_file = "test_encrypted.enc"
    decrypted_file = "test_decrypted.txt"

    with open(input_file, 'wb') as f:
        f.write(plaintext)

    encrypt_file(input_file, password, encrypted_file)
    decrypt_file(encrypted_file, password, decrypted_file)

    with open(decrypted_file, 'rb') as f:
        decrypted_text = f.read()

    assert plaintext == decrypted_text

    os.remove(input_file)
    os.remove(encrypted_file)
    os.remove(decrypted_file)
