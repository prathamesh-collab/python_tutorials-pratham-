#!/usr/bin/env python3.7


def menu():
    print("welcome")
    print(" " )
    print("1:- addition")
    print("2: subtraction")
    print("3:- multiplication")
    print("4:- division")
    print("5:- quit")
    print(" " )
    return int(input("chose your option "))

def add():
    a = int(input("enter 1st value : "))
    b = int(input("enter 2nd value : " ))
    print(a + b )
def sub():
    a = int(input("enter value :"))
    b = int(input("enter value :"))
    print(a - b )
def mul():
    a = int(input("enter value : "))
    b = int(input("enter value : "))
    print(a * b )
def div():
    a = int(input("enter value :"))
    b = int(input("enter value : "))
    print(a / b )

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        add()
    elif choice == 2:
        sub()
    elif choice == 3:
        mul()
    elif choice == 4:
        div()
    elif choice == 5:
        loop = 0 

print("thanks for using")





