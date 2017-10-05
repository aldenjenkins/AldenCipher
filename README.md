# Alden's Custom Cipher Implementation (<=2.7.13)

### Testing practical internet-communication cipher creation and decryption

Basic useful feature list:

 * Single Encrypt/Decrypt Object
 * Socket communication between: 
 	* Client
 	* Server
 * Customize your plaintext message with both:
 	* Uppercase and
 	* Lowercase Characters with
 	* Spaces ignored
 * Randomized key length (up to 26)
 
## How to run

Open a terminal and run:

```bash
python SocketServer.py
```

This waits for communication from the 'Client' file, which we then run in a new terminal window by running 

```bash
python SocketClient.py word1 word2 word3 word4 asmanywordsasyouwant
```

While ofcourse chaning the message you want encrypted from "word1 .. wordN" to something more practical, And watch the 'Server' print the encrypted and decrypted message!

## Spice it up

While keeping the SocketServer.py running, in a different terminal run:

```bash
for i in {1..20}; do python SocketClient.py SomePlainText; done
```

And watch the randomized key change the encrypted message in the 'Server' output!

## Todo

 * Add more Ciphers than just the Caesar Cipher to the AldensEncryptions object
 * Customizable Decryption Key as a parameter in running SocketClient.py
 * Transfer key to server without any interceptor being able to use it to decrypt the encrypted message