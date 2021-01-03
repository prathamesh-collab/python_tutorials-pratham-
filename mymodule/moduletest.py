#!/usr/bin/env python3.7


#define some varible
numberone=1
ageofqueen=78


#define some function

def printhello():
    print("hello")

def timesfour(input):
    print("input * 4")

#define class

class piano:
    def __init__(Self):
        self.type=input("what type of piano")
        self.heigth=input("what height (in feet) ? " )
        self.price=input("how much did it cost ")
        self.age=input("how old it (in year)? ")


    def printdetail(self):
        print("this piano is an " + self.height+ "foot ")
        print("type is " ,  self.type , " piano " , self.age , "years old " , self.price ," dollars" )




