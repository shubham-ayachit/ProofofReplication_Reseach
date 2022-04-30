import base64
from importlib.resources import path
import subprocess as s
import hashlib as h
import json

from numpy import byte
with open('config.json', 'r') as config:
    cfg = json.load(config)


class baseConversion:

    def getFile(self) -> byte:
        f = open(cfg['path']['test'], cfg['access']['test'])
        data = f.read()
        f.close()
        return base64.b64encode(data)
        
    

if __name__ == "__main__":
    b = baseConversion()
    print(b.getFile())
