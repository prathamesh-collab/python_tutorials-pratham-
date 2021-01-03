#!/usr/bin/env python3.7

while loop == 1:
    print("welcome to calculator")

    print("your choice are : " )
    print("  ")
    print("1:- addition")
    print("2:- subtraction")
    print("3:- multiplication")
    print("4:- division")
    print("5:- quit")

    choice = int(input("chose your option: "))
    if choice == 1:
        add1 = int(input("add this: " ))
        add2 = int(input("to this: "))
        print(add1, "+" , add2 , "=" , add1 + add2 )
    elif choice == 2:
        sub2 = int(input(
