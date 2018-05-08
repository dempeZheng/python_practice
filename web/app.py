from flask import Flask
from flask import request, render_template

from db import FanxingDao;

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


@app.route('/user', methods=['GET', 'POST'])
def select_user():
    users = FanxingDao.select("select * from t_user limit 3")
    return str(users)


if __name__ == '__main__':
    app.run()