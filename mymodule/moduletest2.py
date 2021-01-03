#!/usr/bin/env python3

numberone=1
ageofqueen=78

def printhello():
    print("hello world")
def timesfour(input):
    print(input*4)


class piano:
    def __init__(self):
        self.type=input("what type of piano \n")
        self.height=input("what height \n")
        self.price=input("how much did it cost \n")
        self.age=input("how old is it \n")
        return
    def print(self):
        print("this piano is " +self.type+  "and height is " ,self.height )
        print("this piano price is " ,self.price)
        print("piano is " +self.age+ "years old ")
        

        
