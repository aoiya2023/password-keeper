# This file stores the algorithm to encrypt and decrypt account passwords.
# This file uses symmetric key method for encrypting/decrypting.

from cryptography.fernet import Fernet

import func

# works
# ... checks if this module was imported correctly or not.
def works():
    return True

# genKey
# ... generates a random key and store it in a file (key.txt)
# TODO: currently, it only has a single key so a bit dangerous
def genKey():
    key = Fernet.generate_key()
    keyFile = open("key.txt", "wb")
    keyFile.write(key)
    keyFile.close()
    func.Log("Key created", "genKey")

# readKey
# ... read the key from a file.
def readKey():
    global secKey  # makes secKey accessible from other functions
    try:
        with open("key.txt", "rb") as keyFile:
            secKey = keyFile.read()
            keyFile.close()
            return True
    except IOError as error:
        func.Log(error, "readKey")
        return False

# encrypt
# ... encrypt the given password (in string) and return encrypted string.
def encrypt(password):
    readKey()
    f = Fernet(secKey)
    encrypted = f.encrypt(password.encode())
    return encrypted.decode("utf-8")

# decrypt
# ... decrypt the message (in bytes) and return decrypted string.
def decrypt(encrypted):
    readKey()
    f = Fernet(secKey)
    decrypted = f.decrypt(encrypted)
    return decrypted.decode("utf-8")
