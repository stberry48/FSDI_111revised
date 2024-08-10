from flask import Flask # from the flask module import the flask class

app = Flask(__name__) # create an instance of the Flask class (an Object)

@app.get("/")       # flask decorator that "wraps" our view function
def index():        # view function
    me = {          # python 3 dictionary (key-value pairs)
        "first_name": "Sheree",
        "last_name": "Berry",
        "hobbies": "Gardening",
        "is online": True
    }
    return me       # returning a dict from a view function auto-converts to JSON!