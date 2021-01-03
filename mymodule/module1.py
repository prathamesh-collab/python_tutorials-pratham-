#!/usr/bin/env python3


def person1():
    print("hello sir good mornig \nbefore you enter here is some security check")
    a=input("enter your name here :")
    print(" ")
    b=int(input("enter your age here "))
    
    print(" ")
    if b <= 21:

        print("i am sorry !" + a +" sir you are under 21 ")
    elif  b > 21:

        print("thank-you for coprate !"+a+"sir you are ready to go inside ; please come \n have a good day")
        
    print(" ")


    print("gate-pass cahecking here ")
    c=int(input("enter gate pass value here"))
    if c < 20000:
        print("approve")
    elif c > 20000:
        print("sorry ur booking is not confrimed yet")
        return



       







    
