#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('gymbuddy.db')
c = conn.cursor()

c.execute('''create table membership (name text , type text , admisson text , renual text , year real)''')

c.execute("insert into membership values('prathamesh','gain','2017-02-05','2018-02-05',2019)")
c.execute("insert into membership values('rohan','weight loss','2018-05-05','2019-01-05',2019)")
 

conn.commit()

conn.close()

