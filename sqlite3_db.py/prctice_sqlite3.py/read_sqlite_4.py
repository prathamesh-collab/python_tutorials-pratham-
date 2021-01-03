#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('workers.db')
c = conn.cursor()

c.execute("select * from workerdata ")


for row in c:
    print(row)



c.fetchone()

a=c.fetchall()
for row in a:
    print(row)

