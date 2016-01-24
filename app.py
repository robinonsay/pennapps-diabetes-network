from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient()
db = client.primer
def getUsername(auth):
    if auth == "8cMySVclQw1xvhhhUm0tEIbAeVek":
        return "patient6"
    elif auth == "7amAbchQQeGWUKY4sc7AmsEMVBNA":
        return "patient3"
    elif auth == "mGRZ93y7jIGU51BDbKIsNTpVLHEU":
        username = "mGRZ93y7jIGU51BDbKIsNTpVLHEU"
        return "patient5"
    else:
        return None

def getAuth(username):
    if username == "patient6":
         return "8cMySVclQw1xvhhhUm0tEIbAeVek"
    elif username == "patient3":
        return "7amAbchQQeGWUKY4sc7AmsEMVBNA"
    elif username == "patient5":
        return "mGRZ93y7jIGU51BDbKIsNTpVLHEU"
    else:
        return None

@app.route('/')
def index():
    """The inital page"""
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    """User calls this in index.html to login to app"""
    uID = getAuth(request.form['username'])
    # password = request.form['password']
    if uID is None:
        redirect('/')
#User is added to database if they aren't already in the database
    # if db.users is None or db.users.find({"uID":uID, "password":password}) is None:
    #     results = db.users.insert_one({
    #     "uID":uID,
    #     "password":password,
    #     })
    #After authentication, user is taken to home.html
    return redirect(url_for("home", uID=uID))

@app.route('/home/<uID>')
def home(uID):
    """Users home page"""
#if no uID is given, take back to index.html
    if uID is None:
        return redirect('/')
#list of friends is passed to poopulate the bet thing
    friends = db.friends.find({"uID":uID})
    tempList = []
    for friend in friends:
        tempList = getUsername(friend.uID)
    return render_template('home.html', uID=uID, friends=tempList, username = getUsername(uID))

@app.route('/profile/<uID>')
def profile(uID):
    """Users profile, they can add friends here"""
    results = db.users.find()
    users = []
    for user in results:
        users.append(getUsername(user.uID))

    return render_template('profile.html', username=getUsername(uID), users=users, uID=uID)

@app.route('/update/<uID>', methods = ['POST'])
def update(uID):
    """Called to update data for a user"""
    if request.form['time-of-day'] == 0:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "before-breakfast":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    elif request.form['time-of-day'] == 1:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "after-breakfast":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    elif request.form['time-of-day'] == 2:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "before-lunch":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    elif request.form['time-of-day'] == 3:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "after-lunch":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    elif request.form['time-of-day'] == 4:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "before-dinner":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    elif request.form['time-of-day'] == 5:
        updatedResults =  db.users.insert_one(
        {"uID":uID,
            "after-dinner":{
                "current-blood-glucose":request.form['current-blood-glucose'],
                "carbs":request.form['carbs'],
                "target-blood-glucose":request.form['target-blood-glucose'],
                "carb-ratio":request.form['carb-ratio'],
                "insulin-sensitivity":request.form['insulin-sensitivity']

            }
        })
    print(db.users.find())
    print(db.friends.find())
    return redirect(url_for("home", uID=uID))

@app.route('/logout')
def logout():
    """Called to log user out by taking them to homepage"""
    return redirect('/')

@app.route('/addFriend/<username>')
def addFriend(username):
    """"""
    friend = request.args.get('friend',0,type=str)
    db.friends.insert_one(
    {
        "uID":getAuth(username),
        "friend":getAuth(friend)
    })
    return jsonify(friend=friend)

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
