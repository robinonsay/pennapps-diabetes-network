from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.primer

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<username>')
def home(username):
    if username is None:
        return redirect('/')
    return render_template('home.html', username = username, password = password)

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if db.users is None or db.users.find({"username":username, "password":password}) is None:
        results = db.users.insert_one({
        "username":username,
        "password":password,
        })

    return redirect(url_for("home", username = username))

@app.route('/logout')
def logout():
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
