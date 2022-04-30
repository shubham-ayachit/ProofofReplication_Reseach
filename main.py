from baseConversion import baseConversion
from linuxId import MacineId
from mysocket import mySocket


if __name__ == "__main__":
    sock = mySocket()
    bConv = baseConversion()
    id = MacineId()
    sock.mysock(bConv, id)
