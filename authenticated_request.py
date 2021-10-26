import time
import random
import json
import sys
from requests_oauthlib import OAuth1, OAuth1Session
from PyQt5.QtWidgets import QApplication, QMainWindow

# local imports
from keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET
from generate_encrypted_keys import ENCRYPTED_KEY_FILENAME
from generate_encrypted_keys import generate_fernet_key, encrypt_keys, write_encrypted_keys_to_file
from generate_encrypted_keys import read_encrypted_keys_from_file, read_decrypted_keys_from_file

from gui import Window

API_BASE_URL = "https://api.bricklink.com/api/store/v1"

fernet_key = generate_fernet_key() # generate a fernet key
encrypt_keys(fernet_key) # encrypt the oauth keys with the fernet key
write_encrypted_keys_to_file() # write the keys to the file (binary)

encrypted_list = read_encrypted_keys_from_file()
ENCRYPTED_CONSUMER_KEY    = encrypted_list[0].strip(str.encode('\n'))
ENCRYPTED_CONSUMER_SECRET = encrypted_list[1].strip(str.encode('\n'))
ENCRYPTED_TOKEN_VALUE     = encrypted_list[2].strip(str.encode('\n'))
ENCRYPTED_TOKEN_SECRET    = encrypted_list[3].strip(str.encode('\n'))

def main():
    _consumer_key    = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode())
    _consumer_secret = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode())
    _token_value     = str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode())
    _token_secret    = str(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode())

    # Create a session
    session = OAuth1Session(
        client_key            = _consumer_key,
        client_secret         = _consumer_secret,
        resource_owner_key    = _token_value,
        resource_owner_secret = _token_secret,
    )

    query_options = {
        'guide_type': 'sold',  # stock = current items for sale, sold = last 6 months sales
        'new_or_used': 'N',    # N = new, U = used
        'country_code': 'US',  # United States
        'currency_code': 'USD' # US dollars
    }

    set_num = 75255
    item_type = "set"
    request = "{0}/items/{1}/{2}-1/price?{3}={4}&{5}={6}&{7}={8}&{9}={10}".format(
        API_BASE_URL, 
        item_type,
        set_num,
        'guide_type',    query_options['guide_type'],
        'new_or_used',   query_options['new_or_used'],
        'country_code',  query_options['country_code'],
        'currency_code', query_options['currency_code'],
    )
    response = session.get(request)

    if (response.ok == True):
        json_response = response.json()
        # print(json.dumps(json_response, indent=4, sort_keys=True))
        print(" Average price = $ {}".format(json_response['data']['avg_price']))

        # GUI
        app = QApplication(sys.argv)
        window = Window(
            window_xywh=(400, 200, 900, 600), 
            window_title="Lego price tracker",
            window_icon="mr_gold.png",
        )
        sys.exit(app.exec_())
    else:
        print(str(response.status_code) + " " + response.reason)
        exit()


if __name__ == '__main__':
    main()

