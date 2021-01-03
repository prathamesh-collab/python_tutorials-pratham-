#!/usr/bin/env python3.7


loop = 1
choice = 0
while loop == 1:
    print("1:-) addition")
    print("2:-) subtraction")
    print("3:-) multiplication")
    print("4:-) division")
    print("5:- ) exit")
    choice = int(input("enter ur choice here : "))

#a = int(input("enter 1st value here : "))
   # b = int(input("enter 2nd value here : "))

    #choice = int(input("enter ur choice here"))


    if choice == 1:


        a = int(input("enter 1st value here : "))
        b = int(input("enter 2nd value here : "))
        print("addition of ",a, " +" , b , "=" , a + b )
    elif choice == 2:

        a = int(input("enter 1st value here : "))
        b = int(input("enter 2nd value here : "))
        print(a - b )
    elif choice == 3:

        a = int(input("enter 1st value here : "))
        b = int(input("enter 2nd value here : "))
        print(a * b )
    elif choice == 4 :
        a = int(input("enter 1st value here : "))
        b = int(input("enter 2nd value here : "))
        print(a / b)
    elif choice == 5:
        loop = 0

        



