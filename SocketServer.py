from AldenCipher import AldensEncryptions

import socket
import sys

s = socket.socket()
print('# Socket created')
HOST = ''
PORT = 8889
s.bind((HOST, PORT))
print('# Socket bind complete')




# Start listening on socket
s.listen(5)
print('# Socket now listening')
# Receive data from client
while True:
    # Wait for client
    conn, addr = s.accept()
    print('# Connected to ' + addr[0] + ':' + str(addr[1]))
    # message = 'Alden Says Hi!'
    # line = message.decode('UTF-8')  # convert to string (Python 3 only)
    # conn.send('Alden Says Hi!')
    encrypted_message, key = conn.recv(1024).split(',')
    print("Got Message: " + encrypted_message)
    print("Using Public Key: " + key)
    MyEncryption = AldensEncryptions(encrypted_message,key)
    MyEncryption.decrypt_caesar()
    print("Decrypted plain text: " + MyEncryption.get_message())
    conn.send(MyEncryption.get_message())
    conn.close()

s.close()


