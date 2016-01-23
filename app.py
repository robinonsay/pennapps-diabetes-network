from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.primer
def getUsername(auth):
    if auth == "8cMySVclQw1xvhhhUm0tEIbAeVek":
        return "patient6"
    elif auth == "7amAbchQQeGWUKY4sc7AmsEMVBNA" and password == "":
        return "patient3"
    elif auth == "mGRZ93y7jIGU51BDbKIsNTpVLHEU":
        username = "mGRZ93y7jIGU51BDbKIsNTpVLHEU"
        return "patient5"
    return None

def getAuth(username):
    if username == "patient6" and password == "":
         return "8cMySVclQw1xvhhhUm0tEIbAeVek"
    elif username == "patient3" and password == "":
        return "7amAbchQQeGWUKY4sc7AmsEMVBNA"
    elif username == "patient5":
        return "mGRZ93y7jIGU51BDbKIsNTpVLHEU"
    return None

@app.route('/')
def index():
    """The inital page"""
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    """User calls this in index.html to login to app"""
    uID = getAuth(request.form['username'])
    password = request.form['password']

    else:
        redirect('/')
#User is added to database if they aren't already in the database
    if db.users is None or db.users.find({"uID":uID, "password":password}) is None:
        results = db.users.insert_one({
        "uID":uID,
        "password":password,
        })
    #After authentication, user is taken to home.html
    return redirect(url_for("home", uID = uID))

@app.route('/home/<uID>')
def home(uID):
    """Users home page"""
#if no uID is given, take back to index.html
    if uID is None:
        return redirect('/')
#list of friends is passed to poopulate the bet thing
    friends = db.friends.find({"uID":uID})
    tempList = []
    for i in range(0,len(friends)):
        tempList = getUsername(friends[i].uID)
    return render_template('home.html', uID = uID, friends = tempList)

@app.route('/profile/<uID>')
def profile(uID):
    """Users profile, they can add friends here"""
    results = db.users.find()
    users = []
    for user in results:
        users.append(getUsername(user.uID))

    return render_template('profile.html', username = getUsername(uID), users = users)

@app.route('/update/<uID>', methods = ['POST'])
def update(uID):
    """Called to update data for a user"""
    updatedResults = db.users.update_one({"uID":uID},
    {
        "$set":{
            "weight":request.form['weight'],
            "birthdate":request.form['birthdate'],
            "health-conditions":request.form['health-conditions']
        }
    })
    return redirect(url_for("home", uID = uID))

@app.route('/logout')
def logout():
    """Called to log user out by taking them to homepage"""
    return redirect('/')

@app.route('/addFriend/')
def addFriend():
    """"""
    friend = request.args.get('friend',0,type=str)
    db.friends.insert_one(
    {
        "uID":getAuth(username),
        "friend":getAuth
    })
    return redirect(url_for('/profile/', username= username)

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
