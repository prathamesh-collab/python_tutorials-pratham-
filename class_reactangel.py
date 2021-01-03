#!/usr/bin/env python3.7

class shape:
    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.description = "shape"
        self.author = "nobody"

    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self, text):
        self.description = text 
    def authoename(self,text):
        self.author = text 


rectangle = shape(100,45)

print(rectangle.area())


