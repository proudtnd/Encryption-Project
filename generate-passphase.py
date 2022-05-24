import hashlib

#  create passphase file and write the hash of the message
with open('passphase.txt', 'w') as f:
    text = 'Hello World!'
    # compute the hash value of text
    hash_value_from_jack = hashlib.md5(text.encode()).hexdigest()
    f.write(str(hash_value_from_jack)) 
    f.close()