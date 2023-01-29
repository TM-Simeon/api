#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import text

def checkStudent(email):
    engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
    myemail = ""
    with engine.connect() as conn:
        result = conn.execute(text("select * from student where email = '{}';".format(email)))
        for row in result:
            row_as_dict = row._mapping
            myemail = row_as_dict['email']
        if (myemail == ""):
            return "! user not found"
        else:
            return "user found"
    engine.dispose()
