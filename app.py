from flask import Flask, render_template, request, redirect
app = Flask(__name__)
username = None
password = None
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/')
def home():
    if username is None and username is None:
        return render_template('index.html')
    return render_template('home.html')

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username + " : "+password)
    return redirect('/home/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
