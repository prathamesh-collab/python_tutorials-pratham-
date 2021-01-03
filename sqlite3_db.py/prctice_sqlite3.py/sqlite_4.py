#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('workers.db')

c = conn.cursor()

c.execute('''create table workerdata(id integer , name text , salary real , postition text , hier_date text)''' )

c.execute("insert into workerdata values (1 ,'prathamesh', 1.5 ,'maneger','2023-01-01')")
c.execute("insert into workerdata values (2 ,'mahesh', 1 ,'caretaker','2018-01-01')")
c.execute("insert into workerdata values (3 ,'ramesh', 20 ,'maneger','2023-05-08')")
c.execute("insert into workerdata values (4 ,'jonny', 20 ,'ck','2019-05-01')")
c.execute("insert into workerdata values (5 ,'prathamesh', 1.5 ,'maneger','2023-01-01')")
c.execute("insert into workerdata values (6 ,'prathamesh', 1.5 ,'maneger','2023-01-01')")
#c.execute("PRAGMA table_info(workerdata)")
c.execute('update workerdata set name = "ruziya" where id = 2 ')


conn.commit()

conn.close()



