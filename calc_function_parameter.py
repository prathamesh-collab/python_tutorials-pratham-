#!/usr/bin/env python3.7

def menu():
    print("welcome")
    print("your options are :")
    print(" " )
    print("1: ) addition ")
    print("2 : ) subtraction")
    print("3: ) multiplication")
    print("4: ) division ")
    print("5:) quit")
    print(" ")
    return int(input("enter your choice here : "))
def add(a,b):
    print(a,"+" , b , "=", a + b )
def sub(a,b):
    print(b, "-" , a , "=" , b - a )
def mul(a,b):
    print(a,"*",b , "=" , a * b )
def div(a,b):
    print(a, "/" , b , "=" ,a / b )

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add(input("Add this : ") , input("to this : " ))
    elif choice == 2:
        sub(input("subtract") , input("to this : "))
    elif choice == 3:
        mul(input("multiple this : ") , input("from this " ))

    elif choice == 4:
        div(input("divide :" ) , input("from this "))
    elif choice == 5:
        loop = 0 
print("thank you")




