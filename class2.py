#!/usr/bin/env python3.7

class person:
    def __init__(self , name , age):
        self.name=name
        self.age=age


    def myfunc(self):
        print("hello my name is " + self.name)

    def age(self):
        print("age is " + self .age)





p1=person("jhon",36)
print(p1.myfunc())
p1.age=36





