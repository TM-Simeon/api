#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from os import sys

def courseDetails(course):
    result = ""
    mycourse = ""
    courseresult = []
    engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
    with engine.connect() as conn:
        result = conn.execute(text("select * from courses where title='{}';".format(course)))
        engine.dispose()
        for row in result:
            mycourse = row._mapping
            
    
    courseresult.append(mycourse['title'])
    courseresult.append(mycourse['number_of_modules'])
    courseresult.append(mycourse['duration'])
    
    print("course title is: "+courseresult[0]+", No of modules is: "+courseresult[1]+" and course duration is: "+courseresult[2])
    return courseresult
    
# insertCourse(sys.argv[1])