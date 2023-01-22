#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import text
from flask import Flask, render_template
from checkuser import checkUser

app = Flask(__name__)
@app.route('/<username>/<password>/<email>', strict_slashes=False)
def createuser(email, username, password):
    user = checkUser(email)
    if (user == 'user found'):
        return render_template('login.html', user='user already exist')
    else:
        engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
        with engine.connect() as conn:
            conn.execute(text("insert into myusers values('{}','{}','{}');".format(username, password, email)))
            result = checkUser(email)
            if (result == 'user found'):
                return render_template("login.html", status="user created, proceed to login")
            else:
                return render_template("createAccount.html", status="An error occured | Try again")
        engine.dispose()


app.run(host='0.0.0.0', port=5001)
