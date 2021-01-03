#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('workers.db')

c = conn.cursor()

c.execute('update workerdata set name = "ruchi" where id = 2 ')
#c.execute('insert into workerdata(id , name ,salary , position , hire_date ) values(?,?,?,?,?)' , entities)

entities(7 , 'rohini' , 1 ,'manager' , '2018-01-05')

conn.commit()

conn.close()


