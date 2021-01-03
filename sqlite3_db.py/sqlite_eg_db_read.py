#!/usr/bin/env python3
#this programe is for listing , connecting or execute our example.db database

import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute("select * from stocks")

for row in c:
    print(row)   #will be a list

# to featch single matching fetchone() method

c.fetchone()

#for multiple row use fetchall() method

a=c.fetchall() # which is similar to list(cursor) method use previusly
for row in a:
    print(row)


