#!/usr/bin/env python3

import pymysql

db = pymysql.connect("localhost","pratu","Sep@2019!","publication")

cursor = db.cursor()
query = "select * from student"

lines = cursor.execute(query)
data = cursor.fetchall()

for rows in data:
    print(rows)

db.closed()




