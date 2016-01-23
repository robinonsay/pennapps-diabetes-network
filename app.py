from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.primer

@app.route('/')
def index():
    """The inital page"""
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    """User calls this in index.html to login to app"""
    username = request.form['username']
    password = request.form['password']
#User is added to database if they aren't already in the database
    if db.users is None or db.users.find({"username":username, "password":password}) is None:
        results = db.users.insert_one({
        "username":username,
        "password":password,
        })
    #After authentication, user is taken to home.html
    return redirect(url_for("home", username = username))

@app.route('/home/<username>')
def home(username):
    """Users home page"""
#if no username is given, take back to index.html
    if username is None:
        return redirect('/')
#list of friends is passed to poopulate the bet thing
    friends = db.friends.find({"username":username})
    return render_template('home.html', username = username, friends = friends)

@app.route('/profile/')
def profile():
    """Users profile, they can add frineds here"""
    return render_template('profile.html')

@app.route('/update/<username>', methods = ['POST'])
def update(username):
    """Called to update data for a user"""
    updatedResults = db.users.update_one({"username":username},
    {
        "$set":{
            "weight":request.form['weight'],
            "birthdate":request.form['birthdate'],
            "health-conditions":request.form['health-conditions']
        }
    })
    return redirect(url_for("home", username = username))

@app.route('/logout')
def logout():
    """Called to log user out by taking them to homepage"""
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
