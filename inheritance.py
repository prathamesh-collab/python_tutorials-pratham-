#!/usr/bin/env python3.7

#for inheritance

class person:
    def __init__(myo,fname,lname):
        myo.fname=fname
        myo.lname=lname

    def printname(myo):
        print("hello,my name is " + myo.fname,myo.lname)

#child class ,parent is person class

class student(person):
    def __init__(self,fname,lname,year):
        person.__init__(self,fname,lname)
        self.graduationyear=year

    def welcome(self):
        print("welcome",self.fname,self.lname, "to the class of " , self.graduationyear)



x=student("pratham","sawant",2019)
x.printname()
print(x.graduationyear)
x.welcome()

