#!/usr/bin/env python3.7


def gatetime():


    return datetime.datetime.now()
def take():


    value=input("type here\n")
    with open("linux.txt","a") as op:

        op.write(str([str(gatetime())])+":"+value+"\n")
    print("sucessfully writteen")
def retrieve():



    with open("linux.txt") as op:


        for i in op:


            print(i,end="")
 print("my daily update")
 a=int(input("press 1 for write_data and 2 for see data"))

 if a==1:

     take()
 elif a==2:
     retrieve()




