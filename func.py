# This file contains all the functions required for the main modules to work.

import os
import datetime
import json

# This function is used to check if this module was imported correctly or not.
def works():
    return True

# Log errors and records
def Log(thrown_error, by):
    log = open("logs.txt", "a+")
    log.write(str(datetime.datetime.now()) + " " + by + " " + str(thrown_error) + "\n")
    log.close()

# Log applications startups
def LogStartUp():
    log = open("logs.txt", "a+")
    log.write("====================Application Started at "+str(datetime.datetime.now())+ " ")
    log.close()

# Boolean function to check if file exists or not
def checkFileExists(path):
    if os.path.isfile(path):
        return True
    else:
        return False

# Function to write a file at a given path
def WriteFileInPath(content, path):
    try:
        with open(path, "a+") as file:
            file.write(content + "\n")  # TODO: CHECK IF NEW LINE CHARACTER IS NEEDED OR NOT
            file.close()
            return True
    except IOError as error:
        Log(error, "WriteFileInPath")
        return False

# Function to delete a file at a given path
def DeleteFilelnPath(path):
    if checkFileExists(path):
        os.remove(path)
        return True
    else:
        Log(path + " does not exist", "DeleteFileInPath")
        return False

# Function to convert a JSON to a dict
# Returns a dictionary.
def JsontoDict(content):
    return json.loads(content)


# Function to convert a dict to a JSON
# Returns a JSON String.
def DicttoJson(content):
    return json.dumps(content)

# This function creates given folders.
def installFolders(folders):
    for folder in folders:
        os.mkdirs(folder)
        Log("Created folder " + folder, "install")

# This function creates data file.
def createDataFile():
    try:
        with open("data.txt", "a+") as file:
            file.close()
            return True
    except IOError as e:
        Log(e, "createDataFile")
        return False
