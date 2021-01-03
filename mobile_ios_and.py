#!/usr/bin/env python3.7


def one():
    class android:
        def __init__(self,os,name):
            self.os=os
            self.name=name
        def diplay(self):
            print("display size is : ")
            print(" ")
            print("5.4inch (1080 x 2280)")
            return
        def processor(self):
            print("mobile processor is :")
            print(" ")
            print("Qualcomm snapdragon 636")
            return
        def front_camera(self):
            print("front camera is : ")
            print(" ")
            print("8 MP")
            return
        def rear_camera(self):
            print("back camrea is :")
            print(" ")
            print("12 MP + 5MP")
            return
        def ram(self):
            print("mobile RAM is :")
            print(" ")
            print("4GB")
            return
        def storage(self):
            print("storage is :")
            print(" ")
            print("64GB")
            return
        def battery(self):
            print("Battrey capacity is :")
            print(" ")
            print("3060 mAh")
            return

        def storage(self):
            print("storage is : ")
            print("64 GB")
            return

        def color(self):
            print("mobile color is :")
            print(" ")
            print("blue")
            return

    mob1=android('Andriod 8.1 ','Nokia8.1')
    print("mobile name is : ",mob1.name)
    print("version  is :",mob1.os)
    print(" ")
    print(mob1.diplay())
    print(" ")
    print(mob1.color())
    print(" ")
    print(mob1.processor())
    print(" ")
    print(mob1.front_camera())
    print(" ")
    print(mob1.rear_camera())
    print(" ")
    print(mob1.ram())
    print(" ")
    print(mob1.storage())
    print(" ")
    print(mob1.battery())





def two():
    class ios:
        def __init__(self,os,name):
            self.os=os
            self.name=name
        def display(self):
            print('disply size is :')
            print(" ")
            print('5.80-inch (1125 x 2436)')
            return
        def processor(self):
            print("processor is :")
            print(" ")
            print("Apple A11 Bionic")
        def front_camera(self):
            print("front camera is :")
            print(" ")
            print("7MP")
            return
        def rear_camera(self):
            print("back camera is : ")
            print("12MP+12MP")
            return
        def ram(self):
            print("RAM is :")
            print(" ")
            print("3GB")
            return
        def storage(self):
            print("storage is :")
            print(" " )
            print("64GB")
            return
        def battery(self):
            print("battery capacity is :")
            print(" ")
            print("2716 mAh")
            return 
        def color(self):
            print("mobile color is : ")
            print(" ")
            print("space grey")
            return
        def os(self):
            print("os is :")
            print(" ")
            print("ios 11")
            return




    mob1=ios("ios 11","iphone8plus")
    print("mobile name is :" ,mob1.name)
    print("os vesion is :" , mob1.os)
    print(mob1.color())
    print(" ")
    print(mob1.display())
    print(" ")
    print(mob1.processor())
    print(" ")
    print(mob1.front_camera())
    print(" ")
    print(mob1.rear_camera())
    print(" ")
    print(mob1.ram())
    print(" ")
    print(mob1.storage())
    print(" ")
    print(mob1.battery())
    print(" ")
    


print("there is two type of blue-print are available")
print(" ")
print("1 :- Android mobile")
print("2 :- IOS(iphone opreating sysytem")
print(" ")
choice=int(input("which type of blue-print you wants to open choice (1 or 2)"))
print(" ")
if choice==1:
    one()
elif choice==2:
    two()
else:
    print('something  wrong ')

    











