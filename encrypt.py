from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from numpy import byte


class encr : 

    def __init__(self) -> None:
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        public_kay = private_key.public_key()

        pem = private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption())
        with open('private_key.pem', 'wb') as f:
            f.write(pem)

        pem = public_kay.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)

        with open('public_key.pem', 'wb') as f:
            f.write(pem)
    
    def encryptMethod(self, message) -> byte:

        with open("public_key.pem", "rb") as key_file:
            public_kay = serialization.load_pem_public_key(key_file.read())

        encrypted = public_kay.encrypt(message, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

        return encrypted



if(__name__ == "__main__"):
    e = encr()

    e.encryptMethod(b'qwerty')

    



