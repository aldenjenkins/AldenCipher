# Alden's Custom Cipher Implementation

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
