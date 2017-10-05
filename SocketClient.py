from AldenCipher import AldensEncryptions
import random, sys, socket

if len(sys.argv) > 1:
    message = " ".join(sys.argv[1:])
else:
    message = "FlavioJohnsonthreesixninedamnshefine"

random_key_length = random.randint(1,25)

Encryption = AldensEncryptions(message,"a"*random_key_length)
Encryption.encrypt_caesar()

s = socket.socket()
host = '127.0.0.1'
port = 8889

s.connect((host,port))

s.send(Encryption.get_message()+','+Encryption.get_key())
print(s.recv(1024))
s.close()