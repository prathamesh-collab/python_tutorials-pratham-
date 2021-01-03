#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('gymbuddy.db')
c = conn.cursor()

c.execute("select * from membership")

for row in c:
    print(row)


print(c.fetchone())


a = c.fetchall()

for row in a:
    print(row)



