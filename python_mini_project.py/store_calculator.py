#!/usr/bin/env python3.7

sum = 0
print("welcome to BUY_QUICK kirana store ")
print(" ")

while(True):
    userInput = input("Enter the item price or press q to quit : \n")

    if userInput != 'q':                                 #if input is not equal to q then execute our sum statement
        sum = sum + int(userInput)
        print("order total so far: " , sum )


    else:                                              #if input is q then print total amount
        print("your bill total is " ,sum ," Thanks for shopping with us")
        break

print(" ")
print("keep shopping !  have a good day ")
