import time
import random
import json
import sys
import argparse
import pandas as pd 
import numpy as np
from session import Session, API_TYPE # defined in session.py (see for more details)
from math import floor, ceil
from decimal import *

def _setupArgParser():
    parser = argparse.ArgumentParser(description="Track asset prices over time.")
    parser.add_argument("-o", "--outfile", help="save data to file",\
        nargs="?", type=argparse.FileType('w'), default=sys.stdout)
    return parser.parse_args()

def main():
    # File to be specified by user as arg or default to stdout
    args = _setupArgParser()

    bricklink_session = Session(API_TYPE.BRICKLINK) 
    writer = pd.ExcelWriter("sets.xlsx", mode='w+')
    df = pd.DataFrame()

    while True:
        set_number = input("Set Number: ")
        # set_name = input("Set Name: ")
        quantity = input("quantity: ")
        if set_number.isdigit() and quantity.isdigit():
            
            # Query Bricklink's API via RESTful GET request
            bl_resp1 = bricklink_session.getAvgPriceRequest(int(set_number))
            bl_resp2 = bricklink_session.getSetNameRequest(int(set_number))
            
            if (bl_resp1.ok and bl_resp2.ok):

               avg_price = bl_resp1.json()['data']['avg_price']
               set_name = bl_resp2.json()['data']['name']
               year_released = bl_resp2.json()['data']['year_released']
               img_url = bl_resp2.json()['data']['image_url'].replace("//img.", "")
               print(img_url)
               args.outfile.write("Average price of {0} = $ {1}\n".format(set_number, avg_price))
               
            #    print("Average price = $ {}".format(bricklink_response['data']['avg_price']))
            #    s = pd.Series({'Set Number': set_number, 
            #                   'Set Name': set_name, 
            #                   'Average Price': int(ceil(Decimal(bricklink_response['data']['avg_price']))),
            #                   'Quantity': quantity,
            #                   'Total': int(quantity) * int(ceil(Decimal(bricklink_response['data']['avg_price'])))
            #                 })
            #    df = pd.concat([df, s.to_frame().T], ignore_index=True)
            #    df.to_excel(writer, "sets")
            #    writer.save()
            else:
                print(str(bl_resp1.status_code) + " " + bl_resp1.reason)
                print(str(bl_resp2.status_code) + " " + bl_resp2.reason)
            
        elif set_number.lower() == "quit" or set_name.lower() == "quit" or quantity.lower() == "quit":
            break
        else:
            print("{} is not a valid set number, please enter a valid numver ".format(set_number))
    sys.exit(1)

if __name__ == '__main__':
    main()

