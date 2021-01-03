#!/usr/bin/env python2.7

print(".................welcome to MYSQL ..............")
print(" ")
print("1 :- statement base query like >...insert , slect , alter , create , drop,delete <...")
print(" ")
print("2 :- query that use where caluse ")
print(" ")
 

print( " what type of query you want to exexute < 1 or 2 > " )
choice = int(input("press here your choice "))


def one():


    import  pymysql

    db2 = pymysql.connect("localhost","ilg","!Sep@2019","publication")
    cursor = db2.cursor()
    query = input("enter any  query here : ")
    lines = cursor.execute(query)
    data = cursor.fetchall()

    for rows in data:


        print(rows)



def two():
    import pymysql.cursors
    dbconnection = pymysql.connect("localhost","ilg","!Sep@2019","publication")
    try:
        with dbconnection.cursor() as cursor:
            sql = input("enter query with where caluse  : ")
            cursor.execute(sql,(input("value : " , )))
            result = cursor.fetchone()
            print(result)
    finally:
        dbconnection.commit()
        dbconnection.close()

if choice == 1:
    one()
elif choice == 2:
    two()
else:
    print("somthing went wrong")






