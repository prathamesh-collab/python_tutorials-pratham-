#!/usr/bin/env python3.7

class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        return
    def printname(self):
        print(self.fname,self.lname)

x=person("prathamesh","sawant")
x.printname()


class student(person):
    pass     ##use the pass keyword when you do not want to add any properties or method




x=student("tanmay","sawant")


x.printname()
