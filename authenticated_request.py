import os
import requests
import oauthlib
from requests_oauthlib import OAuth1

from keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET
from generate_encrypted_keys import ENCRYPTED_KEY_FILENAME
from generate_encrypted_keys import generate_fernet_key, encrypt_keys, write_encrypted_keys_to_file
from generate_encrypted_keys import read_encrypted_keys_from_file, read_decrypted_keys_from_file

fernet_key = generate_fernet_key() # generate a fernet key
encrypt_keys(fernet_key) # encrypt the oauth keys with the fernet key
write_encrypted_keys_to_file() # write the keys to the file (binary)


print()
decrypted_list = read_decrypted_keys_from_file(fernet_key)
ENCRYPTED_CONSUMER_KEY = decrypted_list[0]
ENCRYPTED_CONSUMER_SECRET = decrypted_list[1]
ENCRYPTED_TOKEN_VALUE = decrypted_list[2]
ENCRYPTED_TOKEN_SECRET = decrypted_list[3]
print(ENCRYPTED_CONSUMER_KEY)
print(ENCRYPTED_CONSUMER_SECRET)
print(ENCRYPTED_TOKEN_VALUE)
print(ENCRYPTED_TOKEN_SECRET)


# user_auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET)

# print(type(user_auth.client_class.get_oauth_signature))
# print(type(user_auth.client_class.get_oauth_params))
# print(type(user_auth.client_class.register_signature_method))
# print(type(user_auth.client_class.sign))



# Get request
# API_BASE_URL = "https://api.bricklink.com/api/store/v1"
# response = requests.get(API_BASE_URL, params={CONSUMER_KEY: TOKEN_VALUE}, auth=user_auth)
# print(response)
# print(response.text)


# TYPE = "SET"
# SET_NUMBER = 75192
# response = requests.get("{0}?items?type={1}?no={2}/price".format(API_BASE_URL, TYPE, str(SET_NUMBER)), auth=user_auth)
# print(response)
# print(response.text)