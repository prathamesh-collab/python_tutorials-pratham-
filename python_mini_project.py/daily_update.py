#!/usr/bin/env python3.7
import datetime
def gatetime():
    return datetime.datetime.now()

def take():


    
    c=int(input("enter 1 for linux_practice and 2 for python_practice"))
    if(c==1):

        value=input("type here \n")
        with open("linux_practice.txt","a") as op:
            op.write(str([str(gatetime())])+":"+value+"\n")
        print("sucessfully written")
    elif(c==2):

        value=input("type here\n")
        with open("python_prac.txt","a") as op:

            op.write(str([str(gatetime())])+":"+value+"\n")
        print("sucessfully written")

def retrieve():

    c=int(input("enter 1 for linux_practice and 2 for python_practice"))
    if(c==1):

        with open("linux_practice.txt") as op:
            for i in op:
                print(i,end="")
    elif(c==2):
        with open("python_prac.txt") as op:
            for i in op:
                print(i,end="")

print(" my daily update")
a=int(input("press 1 for update_data and 2 for stored__data"))

if a==1:
    b=int(input("press 1 for linux_practice and 2 for python_practice"))
    take()
else:
    b=int(input("press 1 for linux_practice and 2 for python_practice"))
    retrieve()






