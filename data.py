# This file is used to access the data - read and write

import func
import crypt_ac
import crypt_gp

data_path = "data.txt"

# This function is used to check if this module was imported correctly or not.
def works():
    return True

# countAccounts()
# ... counts the number of accouts
def countAccounts():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents == "":
                func.Log("No accounts found on startup", "countAccounts")
                datafile.close()
                return 0
            else:
                contents = func.JsontoDict(crypt_ac.decrypt(contents.encode()))  # dictionary
                count=len(contents)
                func.Log("Found "+str(count)+" account(s) on startup","countAccounts")
                datafile.close()
                return count
    except IOError as e:
        func.Log(e, "countAccounts")
        return -1

# readData()
# ... reads the data from the file and returns a dictionary.
def readData():
    try:
        with open(data_path, "r", encoding='utf-8') as datafile:
            contents = datafile.read()
            if contents != "":
                contents = func.JsontoDict(crypt_ac.decrypt(contents.encode()))
            datafile.close()
            return contents

    except IOError as e:
        func.Log(e, "readData")
        return "error"

# writeData()
# ... writes the data to the file
def writeData(content):
    try:
        with open(data_path, "w+", encoding='utf-8') as file:
            file.write(crypt_ac.encrypt(str(content)))
            file.close()
            return True

    except IOError as e:
        func.Log(e, "writeData")
        return False

# addEntry()
# adds new data and returns True (if success) / False (if fail)
# name.... website, app name
# uname... user name, ID
# pwd..... password
def addEntry(name,uname,pwd):
    accounts = readData()
    password = crypt_ac.encrypt(pwd)
    entry = {"n":name,"u":uname,"p":password}

    if accounts == "error":
        return False
    else:
        if accounts == "":
            writeData(func.DicttoJson({countAccounts() + 1: entry}))
        else:
            accounts.update({str(countAccounts() + 1): entry})
            writeData(func.DicttoJson(accounts))
        func.Log("New account added: "+ name,"addEntry")
        return True

# deleteAccount
# deletes an account from data
def deleteAccount(id):
    accounts = readData()
    print(accounts) # {'1': {'n':, 'u':, 'p'}, ...} -- here, id is '1'
    if accounts == "error":
        return False
    else:
        if accounts == "":
            func.Log("No account(s) to delete.", "deleteAccount")
            return False
        else:
            accounts.pop(id,None)
            print(accounts)
            writeData(func.DicttoJson(accounts))
        func.Log("Account deleted: " + id, "deleteAccount")
        return True
