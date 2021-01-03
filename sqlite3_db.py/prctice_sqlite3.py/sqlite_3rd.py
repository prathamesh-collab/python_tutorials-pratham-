#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

c.execute("create table employees_data(id integer , name text , salary real ,position text , hireDATE text ) ")


c.execute("insert into employees_data values(1 , 'prathamesh' , 1.5  , ' maneger','2023-01-04')")
c.execute("insert into employees_data values(2 , 'rahul' , 1  , ' maneger','2023-01-04')")


           
conn.commit()


conn.close()

