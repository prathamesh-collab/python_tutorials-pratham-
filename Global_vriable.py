#!/usr/bin/env python3.7

l = 10               #globl variable

def func1(n):
    m = 8               #local variable
    #l = 5              #local variable
    global l
    l = l + 50
    print(l,m)

func1("i")    

#if i run this script they show me 8 and 5 coz this is local variable 
#first they search in function then go to globle vriable



#use og global key word is they give us permision to use globle vriable as 10 in our function



