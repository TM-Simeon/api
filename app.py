#!/usr/bin/env python3
from checkuser import checkUser
from flask import Flask, render_template, request

app = Flask(__name__)

app.route('/dashboard/<email>', strick_slashes="off")
def checkemail():
    result = checkUser(email)
    if (result == "user found"):
        return render_template('dashboard.html', email=email)
    else:
        return render_template('dashboard.html')
    
app.route('/dashboard/', strick_slashes=False)
def returnvalue():
    return 8


app.run(host='0.0.0.0')

