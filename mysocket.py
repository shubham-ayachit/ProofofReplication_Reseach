import base64
import socket
import subprocess as s
import hashlib as h
import pathlib
from signal import signal, SIGPIPE, SIG_DFL

from baseConversion import baseConversion
from encrypt import encr
from linuxId import MacineId  
signal(SIGPIPE,SIG_DFL) 


class mySocket:

    def mysock(self, bConv: baseConversion, id: MacineId):
        enc = encr()
        servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_address = ('localhost', 16211)

        servsock.bind(serv_address)

        servsock.listen(1)

        while True:
            clientsock, address = servsock.accept()
            data = clientsock.recv(2048).decode()
            barray = bConv.getFile()
            print("barray", barray)
            barray = h.sha256(barray).hexdigest()
            print("withoutCode", barray)
            barray = barray+data
            print("withouthash", barray)
            barray = h.sha256(barray.encode()).hexdigest()
            print("hash", barray)
            #barray = enc.encryptMethod(barray)
            #print("enc", barray)

            uuid = id.getId()
            print("uuid", uuid)
            uuid = h.sha256(uuid).hexdigest()
            print("hash", uuid)

            reMessage = barray+'\n'+uuid

            print("withput encrypt", reMessage)

            reMessage = enc.encryptMethod(reMessage.encode('utf-8'))
            print("reMessage", reMessage)
            print("type", type(reMessage))
            #uuid = enc.encryptMethod(uuid)
            #print("enc", uuid)

            clientsock.sendall(reMessage)








