#!/usr/bin/env python3.7

num = int(input("enter number here")) 
if num > 0:
    print("positive number ")
elif num == 0:
    print("zero ")
else:
    print("nagative number")

if (num % 2 ) == 0:
    print("{0} is even number".format(num))
else:
    print("{0} is odd number".format(num))



