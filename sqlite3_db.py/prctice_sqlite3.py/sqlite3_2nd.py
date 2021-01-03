#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect('example.db') #create example.db fille

c = conn.cursor()


#create table

c.execute('''create table stocks(data text , trans text , symbol text , qty real , price real)''')

#insert a row of table

c.execute("insert into stocks values('2006-01-05','BUY','RHAT',100,35.14)")

conn.commit()  #save (commit) the changes

#we cam also close the connection if we done with it
#just be sure any changes have been commited or they will be lost

conn.close()


