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
            coursesChild = "{}".format(course['title'])
            courses = courses+coursesChild
            courseList.append(coursesChild)
       
    engine.dispose()
    if (courses==""):
        return "search not found"
    else:
        return courseList
      