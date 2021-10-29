from enum import Enum
from requests_oauthlib import OAuth1, OAuth1Session

# local imports
from keys import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_VALUE, TOKEN_SECRET
from generate_encrypted_keys import ENCRYPTED_KEY_FILENAME
from generate_encrypted_keys import generate_fernet_key, encrypt_keys, write_encrypted_keys_to_file
from generate_encrypted_keys import read_encrypted_keys_from_file, read_decrypted_keys_from_file

class URLS:
    def __init__(self):
        self.bricklink_base_url = "https://api.bricklink.com/api/store/v1"
        # self.chrono24_base_url = ""
        # self.ebay_base_url = ""

class API_TYPE(Enum):
    BRICKLINK = 0
    CHRONO24  = 1
    EBAY      = 2

class Session(URLS):
    def __init__(self, session_type):
        super().__init__() # we have access now to urls specified in the URLS class

        if type(session_type) != API_TYPE:
            raise TypeError("ERR: Did not specify a correct session_type")
        
        try:
            if session_type == API_TYPE.BRICKLINK:
                self.session = self._createBricklinkSession()
            elif session_type == API_TYPE.CHRONO24:
                pass # self.session = self.createChrono24Session()
            elif session_type == API_TYPE.EBAY:
                pass # self.session = self.createEbaySession()
        except Exception as err:
            raise err
        # more to come

    def _createBricklinkSession(self):
        fernet_key = generate_fernet_key() # generate a fernet key
        encrypt_keys(fernet_key) # encrypt the oauth keys with the fernet key
        write_encrypted_keys_to_file() # write the keys to the file (binary)
    
        encrypted_list = read_encrypted_keys_from_file()
        ENCRYPTED_CONSUMER_KEY    = encrypted_list[0].strip(str.encode('\n'))
        ENCRYPTED_CONSUMER_SECRET = encrypted_list[1].strip(str.encode('\n'))
        ENCRYPTED_TOKEN_VALUE     = encrypted_list[2].strip(str.encode('\n'))
        ENCRYPTED_TOKEN_SECRET    = encrypted_list[3].strip(str.encode('\n'))
    
        _consumer_key    = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_KEY).decode())
        _consumer_secret = str(fernet_key.decrypt(ENCRYPTED_CONSUMER_SECRET).decode())
        _token_value     = str(fernet_key.decrypt(ENCRYPTED_TOKEN_VALUE).decode())
        _token_secret    = str(fernet_key.decrypt(ENCRYPTED_TOKEN_SECRET).decode())
    
        # Create a session
        try:
            _session = OAuth1Session(
                client_key            = _consumer_key,
                client_secret         = _consumer_secret,
                resource_owner_key    = _token_value,
                resource_owner_secret = _token_secret,
            )
            return _session
        except Exception as err:
            raise err

    def getRequest(self, item_num, item_type="set", guide_type="sold", new_or_used="N", country_code="US", currency_code="USD"):
        _request = "{0}/items/{1}/{2}-1/price?{3}={4}&{5}={6}&{7}={8}&{9}={10}".format(
            self.bricklink_base_url,
            item_type,
            item_num,
            'guide_type',    guide_type,
            'new_or_used',   new_or_used,
            'country_code',  country_code,
            'currency_code', currency_code,
        )
        return self.session.get(_request)








