import rsa
from threading import Timer 
import time

public_key = None
private_key = None

def decrypt(crypto):
    global private_key
    return rsa.decrypt(crypto, private_key)


def update_keys():
    global public_key,private_key
    public_key,private_key = rsa.newkeys(1024,poolsize=2)
    # Timer(86400,update_keys).start()


timer = Timer(0,update_keys)
timer.start()
