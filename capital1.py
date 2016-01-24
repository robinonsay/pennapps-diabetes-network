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

def getAccounts():
    # Generate a random string for the state parameter
    # Save it for use later to prevent xsrf attacks
    from uuid import uuid4


    test_url ="http://api.reimaginebanking.com/accounts?key=69ba67f1790ec541068e389bd9624da5"

    data = r.get(test_url)
    return data.text

UUID_Test= "56241a13de4bf40b1711216e"

def add_account(UUID,  balance, name, rewards=0):
   url="http://api.reimaginebanking.com/customers/"+str(UUID)+"/accounts?key=69ba67f1790ec541068e389bd9624da5"
   d={
  "type": "Credit Card",
  "nickname": name,
  "rewards": rewards,
  "balance": balance,
  "account_number": str(UUID)
   }
   requests.post(url, d)


def pay(UUID_Payer, UUID_Reciever, amount):
   
   url="http://api.reimaginebanking.com/customers/"+str(UUID_Payer)+"/accounts?key=69ba67f1790ec541068e389bd9624da5"
   d={
  "medium": "Balance",
  "payee_id": UUID_Reciever,
  "amount": amount,
   }
   requests.post(url, d)


if __name__ == '__main__':
    app.run(debug=True, port=65010)
