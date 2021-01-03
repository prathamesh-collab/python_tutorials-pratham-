#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

c.execute("select * from employees_data")
#c.execute('insert into employees_data(id , name , salary , position , hireDATE) values(? , ?, ?, ?, ? ,?)' , entities)
#entities = (2 , 'rahul' , 1 , 'caretaker' , '2019-01-05')


for row in c:
    print(row)


c.fetchone()

a = c.fetchall()
for row in a:
    print(row)


    
