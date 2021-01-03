#!/usr/bin/env python3

import sqlite3             #is module 
conn = sqlite3.connect('example.db')   #create database whos name is example.db
c = conn.cursor()                      #to check or read rows one by one


#create table
c.execute('''create table stocks (date text, trans text,symbol text , qty real ,price real)''')

#insert a row of data 
c.execute("insert into stocks values('2005-01-05','buy','RHAT',10,14)")
c.execute("insert into stocks values('2006-01-08','buy','LT',19,54)")

#save (comit) the chaanges

conn.commit()

#need to close the connection 

conn.close()
