#!/usr/bin/env python3.7


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

     def printer(self):
            print("hello my name is : " + self.name)
            print("my age is : " + self.age)


person1=person('prathamesh',21)



person1.printer()




