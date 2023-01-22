#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from os import sys

def searchCourse(email, course):
    result = ""
    courses = ""
    courseList = []
    engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
    with engine.connect() as conn:
        result = conn.execute(text("select * from courses where title like '%{}%';".format(course)))
        for row in result:
            course = row._mapping
            # print(course['title']+" "+course['duration'])
            coursesChild = "{}".format(course['title'])
            courses = courses+coursesChild
            courseList.append(coursesChild)
        # print(courses) 
        #result = result._mapping
    engine.dispose()
    if (courses==""):
        return "search not found"
    else:
        return courseList
    # print(courses) 
    
    # if (result == ""):
    #     return render_template("login.html", status="user created | proceed to login")
    # else:
    #     return render_template("createAccount.html", status="An error occured | Try again")

# searchCourse(sys.argv[1])      