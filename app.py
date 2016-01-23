from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/<imagelogo>')
def index(imagelogo=None):
    imagelogo = url_for('static', filename='penapps-diabetes-logo-jumbo.png')
    return render_template('index.html',imagelogo=imagelogo)

if __name__ == '__main__':
    app.debug = True
    app.run(host='173.255.234.84')
