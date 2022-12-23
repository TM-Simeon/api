#!/usr/bin/env python3
from checkuser import checkUser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<email>', strict_slashes=False)
def checkemail(email):
    result = checkUser(email)
    #result = ""
    if (result == "user found"):
        return render_template('dashboard.html', mymail=email)
    else:
        return render_template('login.html', status=result)
    
@app.route('/', strict_slashes=False)
def returnvalue():
    return render_template('index.html')

@app.route('/index.html', strict_slashes=False)
def index():
    return render_template('index.html')

@app.route('/login.html', strict_slashes=False)
def login():
    return render_template('login.html')

@app.route('/createAccount.html', strict_slashes=False)
def createAccount():
    return render_template('createAccount.html')

app.run(host='0.0.0.0')

