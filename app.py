from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home/<username>')
def home(username, password=None):
    if username is None and password is None:
        return redirect('/')
    return render_template('home.html', username = username, password = password)

@app.route('/login', methods = ['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(username + " : "+password)
    return redirect(url_for("home", username = username, password = password))

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
