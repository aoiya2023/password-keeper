# This file stores the algorithm to encrypt and decrypt global password.
# This file uses salt for encrypting/decrypting.

import bcrypt

import func

# works
# ... checks if this module was imported correctly or not.
def works():
    return True

# passwordHash
# creates the hash from password
def passwordHash(password):
    pwd_bytes = password.encode()
    # generates salt
    salt = bcrypt.gensalt(14)
    # calculate a hash as bytes
    hash_bytes = bcrypt.hashpw(pwd_bytes, salt)
    # decode bytes to a string
    hash_str = hash_bytes.decode()
    func.Log("Encrypt password request.", "passwordHash")
    return hash_str

# storeGlobal
def storeGlobal(password):
    gpFile = open("gp.txt", "w+")
    gpFile.write(passwordHash(password))
    gpFile.close()
    func.Log("GPwd stored", "storeGlobal")

# checkPassword
# return true if the password entered is a valid password
def checkPassword(password):
    try:
        with open("gp.txt", "r") as gpFile:
            hash = gpFile.read()

            pwd_bytes = password.encode()  # user input password
            hash_bytes = hash.encode()  # global password

            does_match = bcrypt.checkpw(pwd_bytes, hash_bytes)
            if does_match == False:
                func.Log("Bad Global", "checkPassword")
            return does_match
    except IOError as error:
        func.Log(error, "checkPassword")
        return False
