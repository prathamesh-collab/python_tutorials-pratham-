#!/usr/bin/env  python3.7

class shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.description = "this shape has not been described yet"
        self.author = "nobady has climed to make this shpe yet"

    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    def describe(self, text):
        self.description=text

    def authorname(self, text):
        self.author=text

    def scalesize(self,scale):
        self.x=self.x * scale

        self.y=self.y*scale


rectangle = shape(5,5)
print(rectangle.area())

print(rectangle.perimeter())


rectangle.describe("a wid rectangle")





