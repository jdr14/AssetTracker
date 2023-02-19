# app.py
import json
from re import L
from flask import Flask
from requests.api import request  
from flask_restful import reqparse
from requests_oauthlib import OAuth1, OAuth1Session
from session import Session, API_TYPE

app = Flask(__name__) # name for the Flask app (refer to output)
bricklink_session = Session(API_TYPE.BRICKLINK) 

# Define the index route default home route (home of web UI)
@app.route("/")
def index():
    return "<h1>Hello from Flask!</h1>"

@app.route("/API/bricklink", methods=['GET']) # this route accepts get request from localhost:5000/API/bricklink?set=<setnumber>
def makeAPIReq():
    # grab REST variables from client request
    parser = reqparse.RequestParser()
    parser.add_argument('set', type=str)
    args = parser.parse_args()
    set_num = args['set']
    print("set num: {}".format(set_num))
    bricklink_response = bricklink_session.getRequest(set_num)

    # make bricklink request
    if (bricklink_response.ok == True):
        bricklink_response = bricklink_response.json()
        return bricklink_response #" Average price = $ {}".format(bricklink_response['data']['avg_price'])
    else:
        print(str(bricklink_response.status_code) + " " + bricklink_response.reason)
    return ""
    # respond to client
    # http://localhost:5000/API/bricklink?set=75255


# Run Flask if the __name__ variable is equal to __main__
if __name__ == "__main__":
    app.run()