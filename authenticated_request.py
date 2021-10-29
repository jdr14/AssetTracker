import time
import random
import json
import sys
from session import Session, API_TYPE

def main():
    bricklink_session = Session(API_TYPE.BRICKLINK) 
    bricklink_response = bricklink_session.getRequest(75255)
    
    if (bricklink_response.ok == True):
       bricklink_response = bricklink_response.json()
       # print(bricklink_response)
       print(" Average price = $ {}".format(bricklink_response['data']['avg_price']))
    else:
        print(str(bricklink_response.status_code) + " " + bricklink_response.reason)

if __name__ == '__main__':
    main()

