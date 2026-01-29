import base64
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

# Generate key from password
def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,          # 256-bit key
        salt=salt,
        iterations=100_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key
def encrypt_file(file_path: str, password: str):
    # Read file
    with open(file_path, "rb") as f:
        data = f.read()

    # Generate random salt
    salt = os.urandom(16)

    # Generate key
    key = generate_key_from_password(password, salt)

    # Create Fernet object
    fernet = Fernet(key)

    # Encrypt data
    encrypted_data = fernet.encrypt(data)

    # Save salt + encrypted data
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as f:
        f.write(salt + encrypted_data)

    return encrypted_file_path
def decrypt_file(encrypted_file_path: str, password: str):
    with open(encrypted_file_path, "rb") as f:
        file_data = f.read()

    # Extract salt and encrypted data
    salt = file_data[:16]
    encrypted_data = file_data[16:]

    # Generate key again
    key = generate_key_from_password(password, salt)

    fernet = Fernet(key)

    # Decrypt
    decrypted_data = fernet.decrypt(encrypted_data)

    # Restore original file name
    original_file_path = encrypted_file_path.replace(".enc", "")

    with open(original_file_path, "wb") as f:
        f.write(decrypted_data)

    return original_file_path
