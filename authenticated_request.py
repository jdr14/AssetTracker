import os
import time
import requests
import oauthlib
from oauthlib.oauth1 import SIGNATURE_HMAC_SHA1, SIGNATURE_TYPE_AUTH_HEADER, rfc5849
import requests_oauthlib
from requests_oauthlib import OAuth1, OAuth1Session
from hashlib import sha1
import hmac
import pytz
from datetime import datetime
import random
import json
import inspect

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

# print(dir(oauthlib.oauth1))

# print(ENCRYPTED_CONSUMER_KEY)
# print(ENCRYPTED_CONSUMER_SECRET)
# print(ENCRYPTED_TOKEN_VALUE)
# print(ENCRYPTED_TOKEN_SECRET)

# print(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode())
# print(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode())
# print(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode())
# print(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode())

# tz = pytz.timezone('America/Los_Angeles')
# print(datetime.fromtimestamp(1463288494, tz).isoformat())

url = API_BASE_URL

# from oauth import OAuthRequest
# from oauth.signature_method.hmac_sha1 import OAuthSignatureMethod_HMAC_SHA1
# # params = {
# #     'oauth_nonce': str(random.getrandbits(32)),
# #     'oauth_timestamp': str(int(time.time()))
# #     'oauth_consumer_key': str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode()),
# #     'oauth_signature_method': SIGNATURE_HMAC_SHA1,
# #     'oauth_version': '1.0',
# #     'oauth_signature':
# # }
# consumer = {
#     'oauth_token': str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode()),
#     'oauth_token_secret': str(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode())
# }
# request = OAuthRequest(url)
# request.sign_request(OAuthSignatureMethod_HMAC_SHA1, consumer)
# header = request.to_header()

# user_auth = OAuth1(client_key=str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode()))
# user_auth.client_key            = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode())
# user_auth.client_secret         = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode())
# user_auth.resource_owner_key    = str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode())
# user_auth.resource_owner_secret = str(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode())
# user_auth.timestamp             = str(int(time.time())) # unix time 
# user_auth.nonce                 = str(random.getrandbits(32)) # generate random 32 bit nonce
# user_auth.encoding              = 'utf-8'
# user_auth.signature_type        = SIGNATURE_TYPE_AUTH_HEADER
# user_auth.signature_method      = SIGNATURE_HMAC_SHA1,
# print(inspect.getfullargspec(OAuth1))

# print(user_auth.client_class.get_oauth_params(user_auth,"GET"))
# user_auth.client_class.register_signature_method("sign_request", sign_request)
# print(user_auth.client_class.sign(user_auth, API_BASE_URL))
# print(user_auth.client_class.get_oauth_signature(user_auth, "GET"))

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

session = OAuth1Session(
    client_key            = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode()),
    client_secret         = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode()),
    resource_owner_key    = str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode()),
    resource_owner_secret = str(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode()),
)
url_test = "https://api.bricklink.com/api/store/v1/orders?direction=in"
# response = session.get("{}/items/part/3001old/price".format(API_BASE_URL))
response = session.get(url_test)
if (response.ok == True):
    json_response = response.json()
    print(response.text)
    print(json.dumps(json_response, indent=4, sort_keys=True))
else:
    print(str(response.status_code) + " " + response.reason)
    exit()

# response = requests.get(
#     "{}/items/part/75192".format(API_BASE_URL),
#     auth=user_auth)
# print(response)
# print(response.text)


# TYPE = "SET"
# SET_NUMBER = 75192
# response = requests.get("{0}?items?type={1}?no={2}/price".format(API_BASE_URL, TYPE, str(SET_NUMBER)), auth=user_auth)
# print(response)
# print(response.text)


