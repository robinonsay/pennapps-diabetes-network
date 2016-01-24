import json
from bson.json_util import dumps
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(host="173.255.234.84")
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
    username = request.form['username']
    uID = getAuth(username)
    # password = request.form['password']
    if uID is None:
        redirect('/')

    rawUser = dumps(db.users.find({"uID":uID}))
    users = json.loads(rawUser)
    isInDB = False
    for user in users:
        isInDB = user["uID"] == uID

    if isInDB is not True:
        results = db.users.insert_one({"uID":uID, "username":username})
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
    # rawFriends = dumps(db.friends.find({"uID":uID}))
    rawFriends = dumps(db.users.find())
    friends = json.loads(rawFriends)
    return render_template('home.html', uID=uID, friends=friends, username = getUsername(uID))

@app.route('/profile/<uID>')
def profile(uID):
    """Users profile, they can add friends here"""
    cursor = db.users.find()
    users = dumps(cursor)
    parsedUsers = json.loads(users)
    print(users)


    return render_template('profile.html', username=getUsername(uID), users=parsedUsers, uID=uID)

@app.route('/update/<uID>', methods = ['POST'])
def update(uID):
    """Called to update data for a user"""
    print("beginning update")
    if request.form['time-of-day'] == "0":
        print("working with tod 0")
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "target-blood-glucose":request.form['target-blood-glucose'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

        print("ur pre")
        print(updatedResults)
        print("ur post")
    elif request.form['time-of-day'] == 1:
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "target-blood-glucose":request.form['target-blood-glucose'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

    elif request.form['time-of-day'] == 2:
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "target-blood-glucose":request.form['target-blood-glucose'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

    elif request.form['time-of-day'] == 3:
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "target-blood-glucose":request.form['target-blood-glucose'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

    elif request.form['time-of-day'] == 4:
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "target-blood-glucose":request.form['target-blood-glucose'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

    elif request.form['time-of-day'] == 5:
        updatedResults =  db.users.update_one(
        {"uID":uID},
        {"$set": {
        "before-breakfast":
        {"current-blood-glucose":request.form['current-blood-glucose'],
        "carbs":request.form['carbs'],
        "carb-ratio":request.form['carb-ratio'],
        "insulin-sensitivity":request.form['insulin-sensitivity']}
        }
        })

    isGood = True
    if (request.form['carbs'] == 34 or request.form['carbs'] == 244) is False:
        isGood = False
    if (request.form["current-blood-glucose"]== 102 or request.form["current-blood-glucose"]== 172) is False:
        isGood = False
    if (request.form["carb-ratio"]== 15 or request.form["carb-ratio"]== 12) is False:
        isGood = False
    if (request.form["insulin-sensitivity"]== 1.2 or request.form["insulin-sensitivity"]== 1.6) is False:
        isGood = False
    print(db.users.find())
    print(db.friends.find())
    print(isGood)
    if isGood:
        return redirect(url_for("good", uID=uID))
    else:
        return redirect(url_for("bad", uID=uID))

@app.route('/good/<uID>')
def good(uID):
    return render_template('good.html', uID=uID, username = getUsername(uID))

@app.route('/bad/<uID>')
def good(uID):
    return render_template('bad.html', uID=uID, username = getUsername(uID))

@app.route('/logout')
def logout():
    """Called to log user out by taking them to homepage"""
    return redirect('/')

@app.route('/addFriend/<username>')
def addFriend(username):
    """"""
    friend = request.args.get('friend',0,type=str)
    db.friends.insert_one(
    {"uID":getAuth(username),"friend":getAuth(friend)})
    return jsonify(friend=friend)

@app.route('/formGroup/<uID>', methods = ['POST'])
def formGroup(uID):
    listOfMembers = []
    for field in request.form:
        listOfMembers.append(getAuth(field))
    results = db.group.insert_one(
    {"members-in-group":listOfMembers})
    print(results)
    return redirect(url_for("home", uID=uID))


if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
