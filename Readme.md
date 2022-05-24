
<!-- link github :  -->
# Option 1: Encryption Project

Encryption: Write two python scripts. 

Jack & Jill: Share a symmetric key secretly using either Diffie-Hellman algo. or an asymmetric encryption.

Jack: Send the cipher text of "Hello World!" using the shared key.

Jill: Using a hash function to generate a cipher text of "Hello World!" and save it in a file name called 'passphase.txt'. Decrypted the cipher text received from Jack. Hash the received text and compare it with the hashed pass phase in the file. They should be identical! 

## Explain
### In generate-passphase file

1. Set up 
```python
text = 'Hello World!'
```
2. Create text file 'passphase.txt'
3. compute the hash value of text

### In Encryption-compare file

1. Set up
```python
# Generate public keys and private keys for Jill and Jack
jack_public=120
jack_private=122
jill_public=124
jill_private=126
# Generate message that jack send to jill
message="Hello World!"
```
2. Then you will get decrypted message by using DiffieHellman Class as you can see below
```python
# Class for encryption and decryption of key
class DiffieHellman(object):
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None
        
    def generate_partial_key(self):
        '''
        compute public values of key1 and key2
        partial key = (public_key1 ^ private_key) mod public_key2
        '''
        partial_key = pow(self.public_key1, self.private_key) % self.public_key2
        return partial_key
    
    def generate_full_key(self, partial_reverse_key):
        '''
        compute symmetric keys of key1 and key2
        full key1 = (partial_key_2 ^ private_key) mod public_key2
        full key2 = (partial_key_1 ^ private_key) mod public_key2
        '''
        full_key = pow(partial_reverse_key, self.private_key) % self.public_key2
        self.full_key = full_key
        return full_key
    
    def encrypt_message(self, message):
        '''
        Each character is being encoded into an integer, 
        the key value being added 
        and then the integer being converted back into a character. 
        '''
        en_mess = ""
        for i in message:
            en_mess += chr(ord(i)+self.full_key)
        return en_mess
    
    def decrypt_message(self, en_mess):
        '''
        Reverse process of encrypt_message
        
        Each character is being encoded into an integer, 
        the key value being subtract 
        and then the integer being converted back into a character. 
        '''
        de_mess = ""
        for i in en_mess:
            de_mess += chr(ord(i)-self.full_key)
        return de_mess
```
3. Compare the hash value
```python
if (hash_message == passphase):
   print("Recieve Same Cipher Text")
else:
   print("Recieve Different Cipher Text")
```

## Authors

- [@proudtnd](https://github.com/proudtnd/)


