import hashlib

# class for encryption and decryption of key
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
  
    
# generate public keys and private keys for key1 and key2   
jack_public=120
jack_private=122
jill_public=124
jill_private=126
Jack = DiffieHellman(jack_public, jill_public, jack_private)
Jill = DiffieHellman(jack_public, jill_public, jill_private)

# generate message that jack send to jill
message="Hello World!"

# get partial key of jack and jill
jack_partial=Jack.generate_partial_key()
jill_partial=Jill.generate_partial_key()
print(f"jack_partial message : {jack_partial}, jill_partial message : {jill_partial}")

# get symmetric keys of jack and jill
jack_full=Jack.generate_full_key(jill_partial)
jill_full=Jill.generate_full_key(jack_partial)
print(f"jack_full message : {jack_full}, jill_full message : {jill_full}")

# get encrypted message
jill_encrypted=Jill.encrypt_message(message)
print(f"Encrypted message : {jill_encrypted}")

# get decrypted message
message_decrypt = Jack.decrypt_message(jill_encrypted)
print(f"Decrypted message : {message_decrypt}")

'''
Hash the received text and compare it with the hashed pass phase in the file.
'''
# Hash the received text
hash_message = hashlib.md5(message_decrypt.encode()).hexdigest()
print(f"The cipher text from hash function : {hash_message}")

# open text in the passphase.txt
file = open("passphase.txt")
passphase = file.read()
file.close()
print(f"The cipher text from passphase.txt :  {passphase}")

# compare the hash value
if (hash_message == passphase):
   print("Recieve Same Cipher Text")
else:
   print("Recieve Different Cipher Text")