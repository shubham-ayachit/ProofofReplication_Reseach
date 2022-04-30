import socket
import hashlib as h
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

#this client requires private key to decrypt the inclomg message, that needs to be created from server node and need to put in testClient folder

with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_address = ('localhost', 16211)

key = b'xBtzb-sQeIgKKiVfL4vmBwH_V4znFRFy-r-JPFz1jOA='

fernet = Fernet(key)

sock.connect(serv_address)

message = "proof_of_replication"

sock.sendall(message.encode())

while True:
    data = sock.recv(2048)
    print(data)
    original_message = private_key.decrypt(data, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
    data = original_message.split()
    data_with_message = data[0].decode() + message
    hashed_data = h.sha256(data_with_message.encode()).hexdigest()
    print(hashed_data)
    if(data[0] == b'ffd65f5441f79689705c0d1fc03b812c41f5731141f1c23d9852338a64378d61'):
        print("File hash Verified")
    
    if(data[1] == b'a6cd2b0ab99a4eeace3b35e84e180768f86c5e80e413ac4d913608c94df1b02d'):
        print("id verified")
    


    break

sock.close