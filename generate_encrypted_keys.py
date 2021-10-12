"""
Description:
    Helper API created for the encryption specific needs of the authenticated_request program.  
Author:
    Joseph Rodgers (Joey)
"""
import os

# Cyprography library
from cryptography.fernet import Fernet
# Import keys from local module
from keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET

# File to store encrypted keys
ENCRYPTED_KEY_FILENAME = "encrypted_keys.key"

ENCRYPTED_CONSUMER_KEY     = None
ENCRYPTED_CONSUMER_SECRET  = None
ENCRYPTED_TOKEN_VALUE      = None
ENCRYPTED_TOKEN_SECRET     = None

# Create an Exception class for when write is called before encrypted keys are created
class KeyExistenceError(Exception):
    pass

# Generate a key to encrypt the request auth keys with
def generate_fernet_key():
   return Fernet(Fernet.generate_key())

# Encrypt the user's API keys 
# Note: This must run before calling the write and/or function
def encrypt_keys(fernet_key):
    try:
        global ENCRYPTED_CONSUMER_KEY     
        global ENCRYPTED_CONSUMER_SECRET  
        global ENCRYPTED_TOKEN_VALUE      
        global ENCRYPTED_TOKEN_SECRET     

        ENCRYPTED_CONSUMER_KEY     = fernet_key.encrypt(CONSUMER_KEY.encode())
        ENCRYPTED_CONSUMER_SECRET  = fernet_key.encrypt(CONSUMER_SECRET.encode())
        ENCRYPTED_TOKEN_VALUE      = fernet_key.encrypt(TOKEN_VALUE.encode())
        ENCRYPTED_TOKEN_SECRET     = fernet_key.encrypt(TOKEN_SECRET.encode())
        
        return True

    except Exception as err:
        print(repr(err))
        return False

# If file does not exist, create a new one and write to it
# Note: This must run before calling either read function
def write_encrypted_keys_to_file():
    if (ENCRYPTED_CONSUMER_KEY is None) or (ENCRYPTED_CONSUMER_SECRET is None) or (ENCRYPTED_TOKEN_VALUE is None) or (ENCRYPTED_TOKEN_SECRET is None):
        raise KeyExistenceError
    with open(ENCRYPTED_KEY_FILENAME, 'wb+') as _encrypted_key_file:
        _encrypted_key_file.write(ENCRYPTED_CONSUMER_KEY + str.encode('\n'))
        _encrypted_key_file.write(ENCRYPTED_CONSUMER_SECRET + str.encode('\n'))
        _encrypted_key_file.write(ENCRYPTED_TOKEN_VALUE + str.encode('\n'))
        _encrypted_key_file.write(ENCRYPTED_TOKEN_SECRET + str.encode('\n'))

# In this case, we will return 4 key/values related to oauth packaged in a list
def read_encrypted_keys_from_file():
    with open(ENCRYPTED_KEY_FILENAME, 'rb') as _encrypted_key_file:
        return _encrypted_key_file.readlines()

# In this case, we will return 4 key/values decrypted 
def read_decrypted_keys_from_file(fernet_key):
    with open(ENCRYPTED_KEY_FILENAME, 'rb') as _encrypted_key_file:
        global ENCRYPTED_CONSUMER_KEY     
        global ENCRYPTED_CONSUMER_SECRET  
        global ENCRYPTED_TOKEN_VALUE      
        global ENCRYPTED_TOKEN_SECRET   

        encrypted_list = _encrypted_key_file.readlines()
        ENCRYPTED_CONSUMER_KEY = encrypted_list[0].strip(str.encode('\n'))
        ENCRYPTED_CONSUMER_SECRET = encrypted_list[1].strip(str.encode('\n'))
        ENCRYPTED_TOKEN_VALUE = encrypted_list[2].strip(str.encode('\n'))
        ENCRYPTED_TOKEN_SECRET = encrypted_list[3].strip(str.encode('\n'))

        return [
            fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY),
            fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET),
            fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE),
            fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET),
        ]

# Encrypt keys and write to specified file
def main(): 
    encrypt_keys()
    write_keys_to_file()

# Run program
if __name__ == '__main__':
	main()