# password-keeper
Password management system

## Features
1. Sets a global password and when the user has that password memorized, then they can store and access passwords & usernames for multiple accounts.
2. Saves
    * name (where the password is used - website name etc.)
    * user ID / account name
    * password
3. Deletes the set (name, user ID, password) when indicated. 
## Files
* crypt_ac.py... Stores the algorithm to encrypt and decrypt account passwords This file uses symmetric key method for encrypting/decrypting.
* crypt_gp.py... Stores the algorithm to encrypt and decrypt global password. This file uses salt for encrypting/decrypting.
* data.py... Used to read, write data.
* func.py... Contains all the functions required for the main modules to work.
* screen.py... Builds a screen that interacts with the user (WORK IN PROGRESS)
## How to use
