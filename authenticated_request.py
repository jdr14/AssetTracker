import time
import random
import json
import sys
import pandas as pd 
import numpy as np
from session import Session, API_TYPE
from math import floor, ceil
from decimal import *

def main():
    bricklink_session = Session(API_TYPE.BRICKLINK) 
    writer = pd.ExcelWriter("sets.xlsx", mode='w+')
    df = pd.DataFrame()

    while True:
        set_number = input("Set Number: ")
        set_name = input("Set Name: ")
        quantity = input("quantity: ")
        if set_number.isdigit() and quantity.isdigit():
            bricklink_response = bricklink_session.getRequest(int(set_number))
            
            if (bricklink_response.ok == True):
               bricklink_response = bricklink_response.json()
               print("Average price = $ {}".format(bricklink_response['data']['avg_price']))
               s = pd.Series({'Set Number': set_number, 
                              'Set Name': set_name, 
                              'Average Price': int(ceil(Decimal(bricklink_response['data']['avg_price']))),
                              'Quantity': quantity,
                              'Total': int(quantity) * int(ceil(Decimal(bricklink_response['data']['avg_price'])))
                            })
               df = pd.concat([df, s.to_frame().T], ignore_index=True)
               df.to_excel(writer, "sets")
               writer.save()
            else:
                print(str(bricklink_response.status_code) + " " + bricklink_response.reason)
        elif set_number.lower() == "quit" or set_name.lower() == "quit" or quantity.lower() == "quit":
            break
        else:
            print("{} is not a valid set number, please enter a valid numver ".format(set_number))
    sys.exit(1)

if __name__ == '__main__':
    main()

