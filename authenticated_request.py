import os
import time
import requests
import oauthlib
from oauthlib.oauth1 import SIGNATURE_HMAC_SHA1
import requests_oauthlib
from requests_oauthlib import OAuth1, OAuth1Session
from hashlib import sha1
import hmac
import pytz
from datetime import datetime
import random

# local imports
from keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET
from generate_encrypted_keys import ENCRYPTED_KEY_FILENAME
from generate_encrypted_keys import generate_fernet_key, encrypt_keys, write_encrypted_keys_to_file
from generate_encrypted_keys import read_encrypted_keys_from_file, read_decrypted_keys_from_file

API_BASE_URL = "https://api.bricklink.com/api/store/v1"

fernet_key = generate_fernet_key() # generate a fernet key
encrypt_keys(fernet_key) # encrypt the oauth keys with the fernet key
write_encrypted_keys_to_file() # write the keys to the file (binary)

encrypted_list = read_encrypted_keys_from_file()
ENCRYPTED_CONSUMER_KEY = encrypted_list[0].strip(str.encode('\n'))
ENCRYPTED_CONSUMER_SECRET = encrypted_list[1].strip(str.encode('\n'))
ENCRYPTED_TOKEN_VALUE = encrypted_list[2].strip(str.encode('\n'))
ENCRYPTED_TOKEN_SECRET = encrypted_list[3].strip(str.encode('\n'))

# print(ENCRYPTED_CONSUMER_KEY)
# print(ENCRYPTED_CONSUMER_SECRET)
# print(ENCRYPTED_TOKEN_VALUE)
# print(ENCRYPTED_TOKEN_SECRET)

# print(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode())
# print(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET))
# print(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE))
# print(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET))


# def sign_request():
#     # key = b"CONSUMER_SECRET&" #If you dont have a token yet
#     key = b"CONSUMER_SECRET&TOKEN_SECRET" 
#     # The Base String as specified here: 
#     raw = b"BASE_STRING" # as specified by OAuth
#     hashed = hmac.new(key, raw, sha1)
#     # The signature
#     return hashed.digest().encode("base64").rstrip('\n')

tz = pytz.timezone('America/Los_Angeles')
print(datetime.fromtimestamp(1463288494, tz).isoformat())

user_auth = OAuth1(
    client_key=fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode(), 
    client_secret=fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode(), 
    resource_owner_key=fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode(), 
    resource_owner_secret=fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode(),
    signature_type='AUTH_HEADER',
    signature_method=SIGNATURE_HMAC_SHA1,
    timestamp=str(int(time.time())), # unix time 
    nonce=str(random.getrandbits(32)), # generate random 32 bit nonce
    encoding="UTF-8" # encoding must be utf-8
)

#print(user_auth.client_class.get_oauth_params(user_auth,"GET"))
# print(user_auth.client_class.register_signature_method())
print(user_auth.client_class.sign(user_auth, API_BASE_URL))
print(user_auth.client_class.get_oauth_signature(user_auth, "GET"))

# response = requests.get(API_BASE_URL, auth=user_auth)
# print(response)
# print(response.text)
#user_auth.fetch_access_token(API_BASE_URL)

# response = requests.get(
#     API_BASE_URL, 
#     # params={
#     #     "oauth_version": "1.0", 
#     #     "oauth_consumer_key": str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY)),
#     #     "oauth_token": str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE)),
#     #     "oauth_timestamp": str(time.time()),
#     #     "oauth_nonce": "3495872010",
#     #     "oauth_signature_method": "HMAC-SHA1",
#     #     "oauth_signature": str(user_auth.client_class.get_oauth_signature(user_auth, "POST"))
#     # }, 
#     auth=user_auth)

response = requests.get(
    "{}/items/part/75192".format(API_BASE_URL),
    auth=user_auth)
print(response)
print(response.text)


# TYPE = "SET"
# SET_NUMBER = 75192
# response = requests.get("{0}?items?type={1}?no={2}/price".format(API_BASE_URL, TYPE, str(SET_NUMBER)), auth=user_auth)
# print(response)
# print(response.text)


