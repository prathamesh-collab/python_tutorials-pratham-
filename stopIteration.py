#!/usr/bin/env python3.7


class mynumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise stopIteration

myclass = mynumber()
myiter = iter(myclass)
for x in myiter:
    print(x)
    


