#!/usr/bin/env python3.7


import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("harry_ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")

            print("sucessfully written")
            
        elif(c==2):
            value=input("type here\n")
            with open("harry_food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("sucessfully written")
    elif(k==2):
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("rohan_ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("sucessfully written")
        elif(c==2):
            value=input("type here\n")
            with open("rohan_food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("sucessfully written")
    elif(k==3):
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("ruchita_ex.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("sucessfully written")
        elif(c==2):
            value=input("type here\n")
            with open("ruchita_food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("sucessfully written")
    
    else:
        print("plz enter valid input 1 :- harry , 2:-rohan , 3:-ruchita " )


def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):


            with open("harry_ex.txt") as op:

                for i in op:

                    
                    print(i,end="")
                    
        elif(c==2):
            with open("harry_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif(k==2):
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("rohan_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("rohan_food.txt") as op:
                for i in op:
                    print(i,end="")
    elif(k==3):
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("ruchita_ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("ruchita_food.txt") as op:
                for i in op:
                    print(i,end="")
    else:
        print("plz enter valid input(harry,rohan,ruchita")



print("HEALTH management system")
a=int(input("press 1 for log_data and 2 for Retrieve_data"))

if a==1:
    b=int(input("press 1 for harry 2 for rohan 3 for ruchita"))
    take(b)
else:
    b=int(input("press 1 for harry 2 for rohan 3 for ruchita"))
    retrieve(b)


    




