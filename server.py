# app.py
import json
from re import L
from flask import Flask
from requests.api import request  
from flask_restful import reqparse
from authenticated_request import createSession, getRequest, API_BASE_URL

from requests_oauthlib import OAuth1, OAuth1Session

app = Flask(__name__) # name for the Flask app (refer to output)

BRICKLINK_SESSION = createSession()


# Define the index route
@app.route("/")
def index():
    
    # default home route
    # home of web UI

    return "<h1>Hello from Flask!</h1>"



@app.route("/API/bricklink", methods=['GET']) # this route accepts get request from localhost:5000/API/bricklink?set=<setnumber>
def makeAPIReq():

    

    #grab REST variables from client request
    parser = reqparse.RequestParser()
    parser.add_argument('set', type=str)
    args = parser.parse_args()
    set_num = args['set']

    print("set num: {}".format(set_num))

    bricklink_response = getRequest(BRICKLINK_SESSION, set_num)


# make bricklink request
    
    if (bricklink_response.ok == True):
        bricklink_response = bricklink_response.json()
        print(bricklink_response)
        return " Average price = $ {}".format(bricklink_response['data']['avg_price'])

    else:
        print(str(bricklink_response.status_code) + " " + bricklink_response.reason)
        
    
    return ""

    

    
    # respond to client
    
    


    


# Run Flask if the __name__ variable is equal to __main__
if __name__ == "__main__":


    app.run()