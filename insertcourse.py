#!/usr/bin/env python3
from sqlalchemy import create_engine, text
from os import sys

def insertCourse(email, course, modules_completed, start_date):
    engine = create_engine("mysql+mysqldb://simeon:1306NaBeM3006@localhost/portfolio")
    with engine.connect() as conn:
        result = conn.execute(text("insert into student values('{}', '{}', '{}', '{}');".format(email, course, modules_completed, start_date)))
    engine.dispose()
