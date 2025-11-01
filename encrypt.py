from cryptography.fernet import Fernet

def encrypt_string(plain_text: str) -> tuple[bytes, bytes]:
    key = Fernet.generate_key()
    cipher = Fernet(key)
    plain_text_bytes = plain_text.encode('utf-8')
    encrypted_blob = cipher.encrypt(plain_text_bytes)
    return encrypted_blob, key

sent_data, key = encrypt_string("Hello, World!")
print("Encrypted Data:", sent_data)
print("Encryption Key:", key)

def random_string(length: int =  7) -> str:
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

a = random_string()
print(a)