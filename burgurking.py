#!/usr/bin/env python3.7

# this program is based on ( string format() ) method 

sum1 = 0
num = 0
print(" ")

while(True):

    userinput = int(input("enter the name of item or price of item here \n press q to quit"))
    if userinput != 'q':
        sum1 = sum1 + int(userinput)
        num = num + str(userinput)
        print("order total so far")
    else:
        print("your order name is " , num.format())
        print("your bill is " , sum , " thanks for shopping with us")
        break
print(" ")
print("keep shopping ! have a good day ")


