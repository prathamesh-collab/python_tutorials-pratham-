#!/usr/bin/env python3.7

class Andriod:
    def __init__(self,os,name):
        self.os=os
        self.name=name
        

    def display(self):
        print("display size of mobile is : ")
        print(" ")
        print("5.84-inch (1080x2280)")
    
    def processor(self):
        print("processor of this mobile : ")
        print(" ")
        print("Qualcomm , snapdragon 636")

    def front_cam(self):
        print("front camera is : ")
        print(" ")
        print("8MMP")

    def rear_cam(self):
        print("back camera is : ")
        print(" ")
        print("12MP + 5MP1") 
    
    def ram(self):
        print("RAM of this mobile is : ")
        print(" ")
        print("4GB")

    def storage(self):
        print("storage of mobile :")
        print(" ")
        print("64GB")

    def battery(self):
        print("battery life is : ")
        print(" ")
        print("battery capacity is 3060mAH")

    def os(self):
        print("os vesion of this mobile : ")
        print(" ")
        print("the os version is Android 8.1 ")
      
    def describe(self):
        print("this mobile description is : ")
        print(" ")
        print("the crisp and vivid hdr display is the main selling point of the nokia 7.1 , and is arguably one of the best in this price range. The display alone is worth the price jump from the likes of the Motorola One Power and Nokia 6.1 Plus. The well-optimised software package, promise of timely updates, striking looks, great build quality, and solid cameras only add to this phone’s appeal.")



mob1=Andriod('Android ','Nokia7.1')
print("mobile name is " ,mob1.name)
print(" ")
print("mobile os is : " ,mob1.os)
print(" ")
print(mob1.describe())
print(" " )
print(mob1.display())
print(" ")
print(mob1.processor())
print(" ")
print(mob1.ram())
print(" ")
print(mob1.storage())
print(" ")
print(mob1.battery())
print(" ")
print(mob1.front_cam())
print(" ")
print(mob1.rear_cam())




