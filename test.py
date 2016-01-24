import urllib
import httplib
from flask import Flask
import json
app = Flask(__name__)
import requests as r
@app.route('/')
def homepage():
    text = '<a href="%s">Authenticate with reddit</a>'
    return text % make_authorization_url()

def make_authorization_url():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    from uuid import uuid4


    test_url = "https://jnj-dev.apigee.net/otr/v1/patient/-/healthdata/search?type=bloodGlucose,bolusInsulin,exercise,food&startDate=2015-12-01T00%3A00%3A00&endDate=2016-01-22T00%3A00%3A00&limit=5000&offset=0"


    header = {"Authorization": "Bearer gj2IteALaKutymp6mmMwf0hpNG7A", "Content-Type":  "application/json", "Accept": "application/json"}
    data = r.get(test_url, headers=header)
    with open("jsonOut.json", "w") as outfile:
            outfile.write(data.text)
    

# Left as an exercise to the reader.
# You may want to store valid states in a database or memcache,
# or perhaps cryptographically sign them and verify upon retrieval.
def save_created_state(state):
    pass
def is_valid_state(state):
    return True

make_authorization_url()

if __name__ == '__main__':
    app.run(debug=True, port=65010)
