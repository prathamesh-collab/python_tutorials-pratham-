#!/usr/bin/env python3.7


def add(num1,num2):
    num1=int(input("enter 1st value"))
    num2=int(input("enter 2nd value"))
    print("addition is : ",num1+num2)
    return

def sub(num1,num2):
    num1=int(input("enter 1st value"))
    num2=int(input("enter 2nd value"))
    print("subtraction  is : ",num1-num2)
    return

def mul(num1,num2):
    num1=int(input("enter 1st value"))
    num2=int(input("enter 2nd value"))
    print("multiplication  is : ",num1 * num2)
    return

def div(num1,num2):
    num1=int(input("enter 1st value"))
    num2=int(input("enter 2nd value"))
    print("division  is : ",num1/num2)
    return


print("calculator is open for you")
print("  ")
print("1 :- addition")
print("2 :- subtraction")
print("3 :- multiplication")
print("4 :- division")
print(" ")

choice=int(input("enter your choice"))
if choice==1:
    add(2,2)
elif choice==2:
    sub(2,3)
elif choice==3:
    mul(2,2)
elif choice==4:
    
    div(2,2)

else:
    print("somthing wrong")










