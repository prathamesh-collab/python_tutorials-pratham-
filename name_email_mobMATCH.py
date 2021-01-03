#!/usr/bin/env python3.7
import re


print("what you want to check")
print(" ")
print("1 : - your name ")
print(" ")
print("2 :- your Email address")
print(" ")
print("3 :- your mobile no ")
print(" ")

chs=int(input("enter your choice here "))
print(" ")



def name():
    print("............##...verification of first name & last name...##.........")
    print("  ")

    reg  = re.compile(r'^[A-Z]\w+\s\w+',flags=re.IGNORECASE)

    myinput = input("enter your name here \n")

    if reg.match(myinput):

        print("valid name")
    else:
        
    




        print("invalid enterd name")
def Email():
    print("...............##....verification of Email address....##..............")
    print(" ")
    reg = re.compile(r'^[A-Z-a-z-0-9]\w+\W\w+\W\w+',flags=re.IGNORECASE)
    inpu = input("Enter your Email address here \n")

    if reg.match(inpu):
        print("valid Email address")
    else:
        print("Invalid email address")


def mob():
    print("...........##....verification of mobile no....##..............")
    print(" ")
    reg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d',flags=re.IGNORECASE)
    inpus = input("enter your mobile  number here \n")
    if reg.match(inpus):
        print("valid mobile number")
    else:
        print("Invalid mobile number")


if chs==1:
    name()
elif chs==2:
    Email()
elif chs==3:
    mob()
else:
    print("somthing wrong ")

    

