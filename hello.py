from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import date, datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    return '<h1>visit /user/"your name" route</h1>'

@app.route('/user/<name>')
def user(name):
    # datetime object containing current date and time
    now = datetime.now()
    return render_template('page.html', name=name, now=now)

if __name__ == '__main__':
    app.run(debug=True)