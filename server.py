# app.py
from re import L
from flask import Flask
from requests.api import request  

app = Flask(__name__) # name for the Flask app (refer to output)





# Define the index route
@app.route("/")
def index():
    return "Hello from Flask!"


@app.route("/API/bricklink", methods=['GET'])
def makeAPIReq():
    return "getPrice"

    


# Run Flask if the __name__ variable is equal to __main__
if __name__ == "__main__":
    app.run()