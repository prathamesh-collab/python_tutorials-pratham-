#!/usr/bin/env python3


class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):


        print(self.firstname,self.lastname)






class student(person):
    def __init__(self,fname,lname,year):
        person.__init__(self,fname,lname)
        self.graduationyear=year
    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)


x=student("prathameh","sawant",2019)

x.welcome()








