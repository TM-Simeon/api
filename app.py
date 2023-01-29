#!/usr/bin/env python3
from checkuser import checkUser
from checkstudent import checkStudent
from flask import Flask, render_template, request
from sqlalchemy import create_engine, text
from searchCourse import searchCourse
from insertcourse import insertCourse
from courseDetails import courseDetails
import datetime

app = Flask(__name__)


@app.route('/createuser', methods=['GET'], strict_slashes=False)
def createuser():
    """if a user already exist, return the login page otherwise, insert user credentials into myusers table"""
    email = request.args.get('email')
    username = request.args.get('username')
    password = request.args.get('password')
    user = checkUser(email)
    if (user == 'user found'):
        return render_template('login.html', status='user already exist | login')
    else:
        engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
        with engine.connect() as conn:
            conn.execute(text("insert into myusers values('{}','{}','{}');".format(username, password, email)))
        engine.dispose()
            
        result = checkUser(email)
        if (result == 'user found'):
            return render_template("login.html", status="user created | proceed to login")
        else:
            return render_template("createAccount.html", status="An error occured | Try again")

@app.route('/searchCourse1', methods=['GET'], strict_slashes=False)
def searchCourse1():
    email = request.args.get('email')
    course = request.args.get('course')
    courses = searchCourse(email, course)
    return render_template("searchCourse.html", courses = courses, email = email)
            
@app.route('/login_dashboard', methods=['GET'], strict_slashes=False)
def login_dashboard():
    """check if user exist, return user's dashboard"""
    email = request.args.get('email')
    result = checkUser(email)
    #result = ""
    if (result == "user found"):
        mycourse1 = ""
        engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
        with engine.connect() as conn:
            course = conn.execute(text("select course from student where email='{}';".format(email)))
            for row in course:
                mycourse = row._mapping
                mycourse1 = mycourse['course']
            if (mycourse1 == ""):
                return render_template("default.html", mymail=email)
            else:
                return render_template(mycourse1+".html", mymail=email)
        engine.dispose()
    else:
        return render_template('login.html', status=result, mymail=email)

@app.route('/insertcourse', methods=['GET'], strict_slashes=False)
def insertcourse():
    email = request.args.get('email')
    course = request.args.get('course')
    modules_completed = 0
    start_date = datetime.datetime.now()
    coursedetails = courseDetails(course)
    alreadyStudent = checkStudent(email)
    if alreadyStudent == "user found":
        engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
        with engine.connect() as conn:
            result = conn.execute(text("select * from student where email = '{}';".format(email)))
            for row in result:
                row_as_dict = row._mapping
                registeredcourse = row_as_dict['course']
                return render_template(registeredcourse+'.html', mymail = email)
        engine.dispose()
    else:
        insertCourse(email, course, modules_completed, start_date)
        return render_template(course+'.html', mymail = email)
        
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

